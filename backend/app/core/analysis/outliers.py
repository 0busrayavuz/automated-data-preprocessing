from __future__ import annotations
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor


def detect_outliers_isolation_forest(df: pd.DataFrame, contamination=0.05) -> dict:
    results = {}
    num_cols = df.select_dtypes(include=["number"]).columns

    for col in num_cols:
        values = df[[col]].dropna()
        if len(values) < 10:
            continue

        model = IsolationForest(contamination=contamination, random_state=42)
        preds = model.fit_predict(values)

        outlier_count = (preds == -1).sum()
        if outlier_count > 0:
            results[col] = {
                "method": "IsolationForest",
                "outliers": int(outlier_count)
            }

    return results
