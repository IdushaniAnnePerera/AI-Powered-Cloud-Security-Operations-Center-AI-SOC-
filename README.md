# AI-Powered Cloud Security Operations Center (AI-SOC)

An end-to-end starter project for an **AI-augmented SOC** that collects multi-cloud logs, detects intrusions/suspicious behavior/malware indicators, and recommends or auto-executes response actions.

## What this project includes

- **Log ingestion API** for AWS, Azure, and local telemetry.
- **Detection engine** using practical SOC heuristics (keyword + behavior patterns).
- **Auto-response mode** for high/critical findings (agentic SOC behavior).
- **Live dashboard** to run a demo and view findings quickly.
- **Free-tier-first deployment plan** to build this with little/no cost.

---

## Architecture (industry-aligned)

1. **Collection Layer**
   - AWS CloudTrail / GuardDuty / VPC Flow Logs
   - Azure Activity Logs / Defender alerts
   - Local endpoint or SIEM-forwarded logs
2. **Detection Layer (AI + rules)**
   - Current repo: heuristic detection baseline
   - Upgrade path: LLM-assisted triage and incident summarization
3. **Response Layer**
   - Suggestions (ticket, analyst notify, forensics)
   - Automatic containment for high/critical risk
4. **Analyst UX**
   - Lightweight web dashboard for SOC workflows

---

## Quick start

### 1) Run the stack

```bash
docker compose up --build
```

- Backend API: `http://localhost:8000/docs`
- Frontend dashboard: `http://localhost:3000`

### 2) Trigger a demo detection run

- Open dashboard
- Click **Run Demo Detection**
- Findings + SOC actions will appear

### 3) API examples

Ingest logs:

```bash
curl -X POST http://localhost:8000/ingest \
  -H "Content-Type: application/json" \
  -d '{
    "events": [
      {
        "source": "aws",
        "event_type": "ConsoleLogin",
        "message": "failed login from unusual location",
        "user": "alice",
        "ip": "45.10.22.1"
      }
    ]
  }'
```

Analyze with auto-response:

```bash
curl -X POST "http://localhost:8000/analyze?auto_respond=true"
```

Get stats:

```bash
curl http://localhost:8000/stats
```

---


