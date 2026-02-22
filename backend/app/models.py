from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class CloudProvider(str, Enum):
    aws = "aws"
    azure = "azure"
    local = "local"


class Severity(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"
    critical = "critical"


class LogEvent(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    source: CloudProvider
    event_type: str
    user: Optional[str] = None
    ip: Optional[str] = None
    resource: Optional[str] = None
    message: str
    metadata: Dict[str, Any] = Field(default_factory=dict)


class Finding(BaseModel):
    id: str
    title: str
    reason: str
    severity: Severity
    score: float
    event: LogEvent
    suggested_actions: List[str]
    auto_response_performed: bool = False


class IngestRequest(BaseModel):
    events: List[LogEvent]


class AnalyzeResponse(BaseModel):
    findings: List[Finding]


class StatsResponse(BaseModel):
    total_events: int
    suspicious_events: int
    providers: Dict[str, int]
    severities: Dict[str, int]
