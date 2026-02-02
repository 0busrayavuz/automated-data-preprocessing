from pydantic import BaseModel
from typing import Any


class UploadResponse(BaseModel):
    file_id: str
    filename: str
    columns: list[str]


class AnalyzeResponse(BaseModel):
    file_id: str
    results: dict[str, Any]


class CleanRequest(BaseModel):
    file_id: str
    actions: list[dict]


class CleanResponse(BaseModel):
    file_id: str
    cleaned_file_id: str
    output_path: str
