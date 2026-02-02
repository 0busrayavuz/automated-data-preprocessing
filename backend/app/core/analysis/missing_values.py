from __future__ import annotations
import pandas as pd
from sklearn.impute import SimpleImputer, KNNImputer


def missing_summary(df: pd.DataFrame) -> dict:
    total = len(df)
    miss = df.isna().sum()
    ratio = (miss / max(total, 1)).round(4)
    return {
        "rows": total,
        "missing_count": miss.to_dict(),
        "missing_ratio": ratio.to_dict(),
    }


def apply_simple_imputer(df: pd.DataFrame, strategy: str = "mean") -> pd.DataFrame:
    """
    Applies SimpleImputer to numeric columns (mean/median) and categorical (most_frequent).
    """
    out = df.copy()
    num_cols = out.select_dtypes(include=["number"]).columns.tolist()
    cat_cols = [c for c in out.columns if c not in num_cols]

    if num_cols:
        imp = SimpleImputer(strategy=strategy)
        out[num_cols] = imp.fit_transform(out[num_cols])

    if cat_cols:
        imp = SimpleImputer(strategy="most_frequent")
        out[cat_cols] = imp.fit_transform(out[cat_cols])

    return out


def apply_knn_imputer(df: pd.DataFrame, n_neighbors: int = 5) -> pd.DataFrame:
    """
    Applies KNNImputer only to numeric columns (KNN can't directly handle strings).
    """
    out = df.copy()
    num_cols = out.select_dtypes(include=["number"]).columns.tolist()
    if not num_cols:
        return out

    imp = KNNImputer(n_neighbors=n_neighbors)
    out[num_cols] = imp.fit_transform(out[num_cols])
    return out
