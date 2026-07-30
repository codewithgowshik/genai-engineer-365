from enum import Enum
from pydantic import BaseModel


class SustainabilityAnalysis(BaseModel):
    topic: str
    summary: str
    recommendations: list[str]


class Category(str, Enum):
    ENVIRONMENT = "ENVIRONMENT"
    SOCIAL = "SOCIAL"
    GOVERNANCE = "GOVERNANCE"


class ESGClassification(BaseModel):
    category: Category


# ---------------------------------------------------------------
# PDF analysis tool output
#
# The analyze_pdf tool builds and validates against these before
# handing the result back to the agent loop, so the payload Gemini
# receives always has a known, well-typed shape.
# ---------------------------------------------------------------
class PdfPage(BaseModel):
    page: int
    text: str


class PdfAnalysis(BaseModel):
    filename: str
    page_count: int
    char_count: int
    truncated: bool
    text: str
    pages: list[PdfPage]