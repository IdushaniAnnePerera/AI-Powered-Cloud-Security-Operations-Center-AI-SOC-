from __future__ import annotations

import uuid
from collections import Counter
from typing import Dict, List

from .models import Finding, LogEvent, Severity

KEYWORD_SEVERITY: Dict[str, Severity] = {
    "malware": Severity.critical,
    "ransomware": Severity.critical,
    "credential stuffing": Severity.high,
    "brute force": Severity.high,
    "impossible travel": Severity.high,
    "privilege escalation": Severity.high,
    "suspicious": Severity.medium,
    "failed login": Severity.medium,
    "port scan": Severity.medium,
    "policy changed": Severity.medium,
}

SEVERITY_SCORE = {
    Severity.low: 0.25,
    Severity.medium: 0.55,
    Severity.high: 0.8,
    Severity.critical: 0.95,
}

ACTION_LIBRARY = {
    Severity.medium: [
        "Create SOC ticket",
        "Notify on-call analyst",
        "Collect related logs for 1 hour",
    ],
    Severity.high: [
        "Create incident in incident management",
        "Enforce MFA challenge",
        "Block source IP in cloud firewall",
    ],
    Severity.critical: [
        "Isolate affected workload",
        "Rotate potentially compromised keys",
        "Trigger malware containment playbook",
    ],
}


def detect_findings(events: List[LogEvent], auto_respond: bool = False) -> List[Finding]:
    findings: List[Finding] = []
    ip_counter = Counter(event.ip for event in events if event.ip)

    for event in events:
        message = event.message.lower()
        matched_severity = Severity.low
        matched_reason = "No suspicious pattern detected"

        for keyword, sev in KEYWORD_SEVERITY.items():
            if keyword in message:
                matched_severity = sev
                matched_reason = f"Keyword match: '{keyword}'"
                break

        if event.ip and ip_counter[event.ip] >= 10 and matched_severity in {Severity.low, Severity.medium}:
            matched_severity = Severity.high
            matched_reason = "Possible brute-force or spray attack from repeated IP"

        if matched_severity == Severity.low:
            continue

        actions = ACTION_LIBRARY.get(matched_severity, ["Investigate manually"])
        findings.append(
            Finding(
                id=str(uuid.uuid4())[:8],
                title=f"{matched_severity.value.title()} risk from {event.source.value.upper()}",
                reason=matched_reason,
                severity=matched_severity,
                score=SEVERITY_SCORE[matched_severity],
                event=event,
                suggested_actions=actions,
                auto_response_performed=auto_respond and matched_severity in {Severity.high, Severity.critical},
            )
        )

    return findings
