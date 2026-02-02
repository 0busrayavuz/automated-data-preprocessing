from __future__ import annotations
import pandas as pd


def infer_column_types(df: pd.DataFrame) -> dict:
    """
    Returns a simple schema summary:
    numeric / categorical / datetime / boolean / text
    """
    schema = {}
    for col in df.columns:
        s = df[col]
        dtype = s.dtype

        if pd.api.types.is_bool_dtype(dtype):
            schema[col] = "boolean"
        elif pd.api.types.is_numeric_dtype(dtype):
            schema[col] = "numeric"
        elif pd.api.types.is_datetime64_any_dtype(dtype):
            schema[col] = "datetime"
        else:
            # try parse datetime for object columns (lightweight)
            parsed = pd.to_datetime(s, errors="coerce", utc=False)
            if parsed.notna().mean() > 0.8:
                schema[col] = "datetime"
            else:
                # heuristic: if unique ratio is low, categorical
                nunique = s.nunique(dropna=True)
                ratio = nunique / max(len(s), 1)
                schema[col] = "categorical" if ratio < 0.2 else "text"

    return schema
