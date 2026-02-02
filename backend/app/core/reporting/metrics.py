import pandas as pd

def data_quality_metrics(df: pd.DataFrame) -> dict:
    return {
        "rows": len(df),
        "columns": df.shape[1],
        "missing_total": int(df.isna().sum().sum()),
        "missing_ratio": round(df.isna().mean().mean(), 4)
    }
