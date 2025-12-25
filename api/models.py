from typing import Optional
from pydantic import BaseModel


class Asset(BaseModel):
    id: Optional[int] = None
    name: str
    ip: str
    os: str


class Vulnerability(BaseModel):
    id: Optional[int] = None
    title: str
    severity: str
    asset_id: int
    description: str
    status: str
