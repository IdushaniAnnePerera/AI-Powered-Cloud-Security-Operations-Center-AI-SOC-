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

## Free-tier build guide (what to do next)

### Phase 1: Free local MVP (today)

- Use this repo as your SOC core.
- Run everything locally via Docker.
- Generate synthetic attacks with test events.

### Phase 2: Connect real cloud logs (free-friendly)

#### AWS free-tier options

- Enable CloudTrail management events.
- Use CloudWatch Logs + EventBridge for routing.
- Optionally add GuardDuty trial detections.

#### Azure free-tier options

- Use Azure Activity Logs and Defender recommendations.
- Route alerts through Azure Monitor / Event Hub.

#### Local / hybrid

- Use Wazuh OSS, osquery, or Sysmon + OpenTelemetry collector.
- Forward to this API endpoint (`/ingest`).

### Phase 3: Agentic SOC automation (still low-cost)

- Add playbooks:
  - Isolate host
  - Disable user/session
  - Block IP in security groups/NSGs
- Add approvals:
  - Auto for critical
  - Human-in-the-loop for high

### Phase 4: AI enhancement

- Add an LLM for:
  - Alert deduplication
  - Incident summarization
  - Suggested remediation narratives
- Keep deterministic security controls in place (never LLM-only enforcement).

---

## Suggested free stack

- **Backend**: FastAPI (this repo)
- **Frontend**: Static HTML/JS (this repo)
- **Queue (optional)**: Redis free tier or local container
- **Storage**: SQLite local, then PostgreSQL free tier
- **LLM**:
  - Local model (Ollama) for zero API cost, or
  - Generous free API tiers for prototyping
- **Ticketing**:
  - GitHub Issues or Jira free plan

---

## Security and production hardening checklist

- Add authN/authZ for API endpoints.
- Sign and validate log sources.
- Store immutable audit trails.
- Add rate limiting + schema validation.
- Separate detection from response execution with approval policy.

---

## Repo layout

- `backend/app/main.py` - API routes and SOC workflow.
- `backend/app/detector.py` - detection and action logic.
- `backend/app/connectors.py` - sample AWS/Azure/local events.
- `frontend/` - minimal SOC dashboard.
- `docker-compose.yml` - local deployment.

---

## Next extensions you can ask me to build

1. Real AWS CloudTrail puller (boto3) and Azure Graph/Monitor collector.
2. MITRE ATT&CK mapping and kill-chain tags.
3. Slack/Teams incident bot + auto ticket creation.
4. SOAR playbook runner with approval matrix.
5. Multi-tenant SOC with RBAC and case management.

