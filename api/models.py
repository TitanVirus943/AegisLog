# api/models.py
from pydantic import BaseModel, constr, validator
from typing import Optional

SEVERITY_CHOICES = {"Low", "Medium", "High", "Critical"}
STATUS_CHOICES = {"Open", "Fixed", "Accepted", "False Positive"}

class Vulnerability(BaseModel):
    id: Optional[int] = None
    title: constr(strip_whitespace=True, min_length=1)
    severity: str
    asset: constr(strip_whitespace=True, min_length=1)
    description: str = ""
    steps: str = ""
    mitigation: str = ""
    status: str = "Open"

    @validator("severity")
    def check_severity(cls, v):
        v = v.title()
        if v not in SEVERITY_CHOICES:
            raise ValueError(f"severity must be one of {sorted(SEVERITY_CHOICES)}")
        return v

    @validator("status")
    def check_status(cls, v):
        v = v.title()
        if v not in STATUS_CHOICES:
            raise ValueError(f"status must be one of {sorted(STATUS_CHOICES)}")
        return v

