from backend.app.detector import detect_findings
from backend.app.models import CloudProvider, LogEvent


def test_detects_malware_and_auto_response():
    events = [
        LogEvent(source=CloudProvider.local, event_type="EDR", message="malware detected", ip="1.1.1.1")
    ]
    findings = detect_findings(events, auto_respond=True)
    assert len(findings) == 1
    assert findings[0].severity.value == "critical"
    assert findings[0].auto_response_performed is True
