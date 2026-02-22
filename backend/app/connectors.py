from __future__ import annotations

from datetime import datetime
from typing import List

from .models import CloudProvider, LogEvent


def sample_events() -> List[LogEvent]:
    now = datetime.utcnow()
    return [
        LogEvent(
            timestamp=now,
            source=CloudProvider.aws,
            event_type="ConsoleLogin",
            user="alice",
            ip="45.10.22.1",
            resource="aws-console",
            message="failed login from unusual location",
            metadata={"region": "us-east-1"},
        ),
        LogEvent(
            timestamp=now,
            source=CloudProvider.azure,
            event_type="RoleAssignmentWrite",
            user="svc-backup",
            ip="185.11.32.4",
            resource="subscription-01",
            message="privilege escalation attempt detected by policy",
            metadata={"subscription": "prod"},
        ),
        LogEvent(
            timestamp=now,
            source=CloudProvider.local,
            event_type="EDR_ALERT",
            user="host-21",
            ip="10.0.2.15",
            resource="workstation-21",
            message="malware behavior found in powershell process",
            metadata={"agent": "osquery"},
        ),
    ]
