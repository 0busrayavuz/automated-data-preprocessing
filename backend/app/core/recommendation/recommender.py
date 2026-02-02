from __future__ import annotations
import pandas as pd
from ..analysis.missing_values import missing_summary
from ..data_loader.schema_analyzer import infer_column_types
from ..analysis.outliers import detect_outliers_isolation_forest


def build_recommendations(df: pd.DataFrame) -> dict:
    schema = infer_column_types(df)
    ms = missing_summary(df)

    recs = []

    # 1️⃣ Missing value recommendations
    for col, r in ms["missing_ratio"].items():
        if r and r > 0:
            recs.append({
                "column": col,
                "type": schema.get(col),
                "problem": "missing_values",
                "missing_ratio": r,
                "missing_count": ms["missing_count"][col],
                "suggestions": [
                    {"id": "simple_imputer_mean", "label": "SimpleImputer (mean / most frequent)"},
                    {"id": "knn_imputer", "label": "KNN Imputer (numeric only)"}
                ]
            })

    # 2️⃣ OUTLIER recommendations (BURASI YENİ)
    outliers = detect_outliers_isolation_forest(df)

    for col, info in outliers.items():
        recs.append({
            "column": col,
            "type": schema.get(col),
            "problem": "outlier",
            "outlier_count": info["outliers"],
            "method": info["method"],
            "suggestions": [
                {"id": "remove_outliers", "label": "Remove outliers"},
                {"id": "cap_outliers", "label": "Cap values (winsorize)"}
            ]
        })

    return {
        "dataset": {
            "rows": len(df),
            "columns": df.shape[1]
        },
        "schema": schema,
        "recommendations": recs
    }
