from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI(title="Chimera Orchestrator API")

# --- Schemas (Matching api_contracts.md) ---
class AgentStatus(BaseModel):
    agent_id: str
    role: str
    status: str
    last_mcp_call: Optional[str]

class SwarmStatusResponse(BaseModel):
    timestamp: datetime
    system_health: str
    active_agents: List[AgentStatus]

class PendingTask(BaseModel):
    task_id: str
    agent_id: str
    content: str
    platform: str
    risk_score: float

# --- Mock Data (Simulating the Swarm) ---
MOCK_TASKS = [
    {
        "task_id": "TASK-778",
        "agent_id": "CHIMERA-BETA-02",
        "content": "Why SOL is the future of Agentic Commerce. #Crypto #AI",
        "platform": "X",
        "risk_score": 0.15
    }
]

@app.get("/api/v1/swarm/status", response_model=SwarmStatusResponse)
async def get_status():
    return {
        "timestamp": datetime.now(),
        "system_health": "healthy",
        "active_agents": [
            {"agent_id": "CHIMERA-ALPHA-01", "role": "Trend Analyst", "status": "observing", "last_mcp_call": "fetch_trends"},
            {"agent_id": "CHIMERA-BETA-02", "role": "Content Creator", "status": "awaiting_approval"}
        ]
    }

@app.get("/api/v1/tasks/pending", response_model=List[PendingTask])
async def get_pending():
    return MOCK_TASKS

@app.post("/api/v1/tasks/{task_id}/decision")
async def post_decision(task_id: str, decision: dict):
    # In a real app, this would trigger the OpenClaw signing skill
    return {"status": "success", "message": f"Decision '{decision['decision']}' processed for {task_id}"}