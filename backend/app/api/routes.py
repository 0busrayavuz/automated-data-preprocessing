from __future__ import annotations

import uuid
from pathlib import Path
from fastapi import APIRouter, UploadFile, File, HTTPException

from .schemas import UploadResponse, AnalyzeResponse, CleanRequest, CleanResponse
from ..core.data_loader.loader import load_dataset
from ..core.recommendation.recommender import build_recommendations
from ..core.pipeline.cleaning_pipeline import run_pipeline

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parents[3]  
DATA_RAW = BASE_DIR / "data" / "raw"
DATA_PROCESSED = BASE_DIR / "data" / "processed"
DATA_RAW.mkdir(parents=True, exist_ok=True)
DATA_PROCESSED.mkdir(parents=True, exist_ok=True)


REGISTRY: dict[str, dict] = {}


@router.post("/upload", response_model=UploadResponse)
async def upload(file: UploadFile = File(...)):
    file_id = str(uuid.uuid4())
    filename = file.filename or "uploaded"
    save_path = DATA_RAW / f"{file_id}_{filename}"

    content = await file.read()
    save_path.write_bytes(content)

    # quick load to validate
    try:
        df = load_dataset(save_path)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"File could not be read: {e}")

    REGISTRY[file_id] = {"path": str(save_path), "filename": filename}
    return UploadResponse(file_id=file_id, filename=filename, columns=list(df.columns))


@router.post("/analyze", response_model=AnalyzeResponse)
def analyze(file_id: str):
    meta = REGISTRY.get(file_id)
    if not meta:
        raise HTTPException(status_code=404, detail="file_id not found")

    df = load_dataset(meta["path"])
    results = build_recommendations(df)
    return AnalyzeResponse(file_id=file_id, results=results)


@router.post("/clean", response_model=CleanResponse)
def clean(payload: CleanRequest):
    meta = REGISTRY.get(payload.file_id)
    if not meta:
        raise HTTPException(status_code=404, detail="file_id not found")

    df = load_dataset(meta["path"])
    cleaned = run_pipeline(df, payload.actions)

    cleaned_id = str(uuid.uuid4())
    out_path = DATA_PROCESSED / f"{cleaned_id}_cleaned.csv"
    cleaned.to_csv(out_path, index=False)

    REGISTRY[cleaned_id] = {"path": str(out_path), "filename": out_path.name}
    return CleanResponse(file_id=payload.file_id, cleaned_file_id=cleaned_id, output_path=str(out_path))
