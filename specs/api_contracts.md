# API Contract: Human-in-the-Loop (HITL) Orchestrator

**Document Status:** PROPOSED (Ratification Pending)
**Version:** 1.0.0
**Project:** Chimera Autonomous Influencer Network
**Source of Truth:** This document defines the schemas for agent-human interaction and system state monitoring.

---

## 1. System Architecture Context
This API serves as the bridge between the **Autonomous Agent Swarm** (Backend) and the **Command Center** (Frontend). It ensures that no agent performs a high-consequence action (e.g., wallet transaction, public post) without a cryptographic "Human Gate."

## 2. Base Configuration
- **Host:** `http://localhost:8000`
- **Base Path:** `/api/v1`
- **Protocol:** REST / JSON

## 3. Core Endpoints

### [GET] /swarm/status
Fetches the telemetry and health status of all agents in the network.
- **Access Level:** Observer
- **Success Response (200 OK):**
```json
{
  "timestamp": "2026-02-06T12:00:00Z",
  "system_health": "healthy",
  "active_agents": [
    {
      "agent_id": "CHIMERA-ALPHA-01",
      "role": "Trend Analyst",
      "status": "observing",
      "last_mcp_call": "fetch_crypto_trends"
    },
    {
      "agent_id": "CHIMERA-BETA-02",
      "role": "Content Creator",
      "status": "awaiting_approval",
      "current_task": "TASK-778"
    }
  ]
}
```
### [GET] /tasks/pending
Lists all tasks requiring a Human-in-the-Loop decision.

**Success Response (200 OK):**

``` JSON
  {
    "task_id": "TASK-778",
    "agent_id": "CHIMERA-BETA-02",
    "content": "Why SOL is the future of Agentic Commerce. #Crypto #AI",
    "platform": "X",
    "risk_score": 0.15,
    "timestamp": "2026-02-06T12:05:00Z"
  }
``` 
### [POST] /tasks/{task_id}/decision
Submits the human's choice for a specific task.

Payload Schema:

 ```JSON
[{
  "decision": "string", 
  "enum": ["approved", "rejected", "regenerate"],
  "feedback": "string (optional)",
  "governance_sig": "string (OpenClaw Signature)"
}]
```
 Success Response (200 OK): {"status": "success", "message": "Decision propagated to agent."}

## 4. Error Standards
**400 Bad Request: Payload does not match Pydantic schema.**

**403 Forbidden: OpenClaw signature invalid.**

**404 Not Found: Task ID expired or does not exist.**