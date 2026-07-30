

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from llm import llm
from logger_config import logger
from models import requests
from schemas import PdfAnalysis
from tools.pdf_analysis import analyze_pdf

app = FastAPI(
    title="Envora — Structured Extraction Service",
    description="HTTP API over the sustainability agent and PDF tool.",
    version="0.1.0",
)


# ---------------------------------------------------------------
# Request / response bodies
#
# FastAPI reads these Pydantic models to validate incoming JSON and
# to auto-generate the /docs schema. Invalid input is rejected with a
# 422 before our code ever runs.
# ---------------------------------------------------------------
class ChatRequest(BaseModel):
    prompt: str


class ChatResponse(BaseModel):
    answer: str


class PdfRequest(BaseModel):
    filename: str
    max_chars: int = 12000


# ---------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------
@app.get("/health")
def health():
    """Cheap liveness check — no model call."""
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
async def chat(body: ChatRequest):
    """
    Run the full agent (with web search + PDF tools) on a prompt.

    show_output=False keeps the rich CLI panels off — the HTTP client
    gets the answer as JSON instead of it being printed to a console.
    """
    logger.info("API /chat request received")

    result = await llm(
        requests(prompt=body.prompt),
        show_output=False,
    )

    return ChatResponse(answer=result.answer)


@app.post("/analyze-pdf", response_model=PdfAnalysis)
def analyze_pdf_endpoint(body: PdfRequest):
    """
    Extract text from a PDF in src/uploads and return the validated,
    structured PdfAnalysis payload directly (no model call).
    """
    logger.info(f"API /analyze-pdf request for {body.filename}")

    result = analyze_pdf(body.filename, body.max_chars)

    # The tool returns an {"error": ...} dict when the file is missing;
    # translate that into a proper 404 for HTTP callers.
    if "error" in result:
        raise HTTPException(status_code=404, detail=result)

    return result
