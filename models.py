from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class SensorData(BaseModel):
    device_id: str
    location: str
    temperature: float
    air_quality: float
    timestamp: datetime


class Alert(BaseModel):
    id: str
    device_id: str
    location: str
    alert_type: str
    message: str
    severity: str
    timestamp: datetime
    resolved: bool = False
