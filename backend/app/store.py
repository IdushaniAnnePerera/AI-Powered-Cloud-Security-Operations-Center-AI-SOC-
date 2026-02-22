from __future__ import annotations

from collections import Counter
from typing import List

from .models import Finding, LogEvent, StatsResponse


class MemoryStore:
    def __init__(self) -> None:
        self.events: List[LogEvent] = []
        self.findings: List[Finding] = []

    def add_events(self, events: List[LogEvent]) -> None:
        self.events.extend(events)

    def add_findings(self, findings: List[Finding]) -> None:
        self.findings.extend(findings)

    def stats(self) -> StatsResponse:
        provider_counter = Counter(event.source.value for event in self.events)
        severity_counter = Counter(f.severity.value for f in self.findings)
        return StatsResponse(
            total_events=len(self.events),
            suspicious_events=len(self.findings),
            providers=dict(provider_counter),
            severities=dict(severity_counter),
        )


store = MemoryStore()
