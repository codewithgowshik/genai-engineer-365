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