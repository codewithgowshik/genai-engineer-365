from typing import Optional
from pydantic import BaseModel


class SustainabilityReport(BaseModel):

    company_name: Optional[str] = None
    industry: Optional[str] = None
    country: Optional[str] = None

    report_year: Optional[int] = None

    revenue: Optional[str] = None

    employees: Optional[int] = None

    carbon_reduction_target: Optional[str] = None

    net_zero_target: Optional[int] = None

    renewable_energy_percentage: Optional[float] = None