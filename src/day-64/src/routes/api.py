from fastapi import APIRouter, UploadFile, File
from pathlib import Path
import shutil

from src.extractor.extractor import extract
from src.schemas.sustainability import SustainabilityReport

router = APIRouter()


@router.get("/")
async def home():
    return {
        "message": "Structured Extraction Service is running."
    }


@router.post(
    "/extract",
    response_model=SustainabilityReport
)
async def extract_pdf(file: UploadFile = File(...)):

    # Save uploaded PDF
    upload_path = Path("uploads") / file.filename

    with open(upload_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Call your existing extraction pipeline
    report = await extract(str(upload_path))

    # Return the Pydantic object
    return report