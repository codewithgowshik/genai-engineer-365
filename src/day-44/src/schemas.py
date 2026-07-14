from pydantic import BaseModel


class SustainabilityAnalysis(BaseModel):
    topic: str
    summary: str
    recommendations: list[str]