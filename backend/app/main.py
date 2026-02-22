from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .connectors import sample_events
from .detector import detect_findings
from .models import AnalyzeResponse, IngestRequest, StatsResponse
from .store import store

app = FastAPI(title="AI-SOC", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/ingest")
def ingest(payload: IngestRequest) -> dict:
    store.add_events(payload.events)
    return {"ingested": len(payload.events)}


@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(auto_respond: bool = False) -> AnalyzeResponse:
    findings = detect_findings(store.events, auto_respond=auto_respond)
    store.add_findings(findings)
    return AnalyzeResponse(findings=findings)


@app.post("/demo/run", response_model=AnalyzeResponse)
def demo_run(auto_respond: bool = True) -> AnalyzeResponse:
    events = sample_events()
    store.add_events(events)
    findings = detect_findings(events, auto_respond=auto_respond)
    store.add_findings(findings)
    return AnalyzeResponse(findings=findings)


@app.get("/stats", response_model=StatsResponse)
def stats() -> StatsResponse:
    return store.stats()
