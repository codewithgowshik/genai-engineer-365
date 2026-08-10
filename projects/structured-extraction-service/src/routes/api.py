from pathlib import Path
import shutil

from fastapi import APIRouter, UploadFile, File, HTTPException

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
    response_model=SustainabilityReport,
    summary="Extract sustainability information from a PDF",
    description="Upload a sustainability report in PDF format and receive structured JSON."
)
async def extract_pdf(file: UploadFile = File(...)):

    # Make sure a filename was provided
    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No file was provided."
        )

    # Only PDF files are supported
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Invalid file type. Please upload a PDF file."
        )

    # Create the upload path
    upload_path = Path("uploads") / file.filename

    try:

        # Save the uploaded file
        with open(upload_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Run the extraction pipeline
        report = await extract(str(upload_path))

        # Return structured response
        return report

    except ValueError as e:

        raise HTTPException(
            status_code=422,
            detail=str(e)
        )

    except Exception:

        raise HTTPException(
            status_code=500,
            detail="Unable to process the PDF. Please try again."
        )