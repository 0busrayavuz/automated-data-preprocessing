from __future__ import annotations
import pandas as pd
from ..analysis.missing_values import apply_simple_imputer, apply_knn_imputer
from ..reporting.metrics import data_quality_metrics


# 🔹 1️⃣ ESKİ FONKSİYON – routes.py BUNU BEKLİYOR
def run_pipeline(df: pd.DataFrame, selected_actions: list[dict]) -> pd.DataFrame:
    out = df.copy()

    for action in selected_actions:
        aid = action.get("id")

        if aid == "simple_imputer_mean":
            out = apply_simple_imputer(out, strategy="mean")

        elif aid == "simple_imputer_median":
            out = apply_simple_imputer(out, strategy="median")

        elif aid == "knn_imputer":
            out = apply_knn_imputer(out, n_neighbors=5)

        # (ileride outlier actions buraya eklenecek)

    return out


# 🔹 2️⃣ YENİ FONKSİYON – RAPORLAMA İÇİN
def run_pipeline_with_metrics(df: pd.DataFrame, selected_actions: list[dict]):
    before = data_quality_metrics(df)
    cleaned = run_pipeline(df, selected_actions)
    after = data_quality_metrics(cleaned)

    return cleaned, {
        "before": before,
        "after": after
    }
