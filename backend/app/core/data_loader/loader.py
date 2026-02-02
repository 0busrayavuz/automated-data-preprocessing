from __future__ import annotations
import pandas as pd
from pathlib import Path


SUPPORTED_EXT = {".csv", ".xlsx", ".xls", ".txt"}


def load_dataset(file_path: str | Path, sep: str = ",") -> pd.DataFrame:
    """
    Loads CSV/TXT/XLSX into a pandas DataFrame.
    TXT is assumed to be delimited (default comma, you can change sep).
    """
    file_path = Path(file_path)
    ext = file_path.suffix.lower()

    if ext not in SUPPORTED_EXT:
        raise ValueError(f"Unsupported file type: {ext}. Supported: {SUPPORTED_EXT}")

    if ext == ".csv":
        return pd.read_csv(file_path)
    if ext in {".xlsx", ".xls"}:
        return pd.read_excel(file_path)
    if ext == ".txt":
        # user may upload tab-separated txt; change sep in config if needed
        return pd.read_csv(file_path, sep=sep)

    raise ValueError(f"Unhandled file extension: {ext}")
