# Project Chimera: Autonomous Influencer Infrastructure

**Author:** [Your Name/GitHub Handle]
**Role:** Forward Deployed Engineer (FDE)
**Architecture:** Swarm-based HITL (Human-in-the-Loop)

##  Governance & Engineering Depth (The "Distance")
This repository is not just code; it is a **Spec-Driven Development (SDD)** environment. I have prioritized "Distance" (Engineering Depth) over mere "Velocity" by establishing a robust governance pipeline before feature implementation.

### 1. Executable Specifications (`/specs`)
- **API Contracts:** Defined in `specs/api_contracts.md` with Pydantic-validated JSON schemas.
- **UI Flow:** State machine logic defined via Mermaid.js in `specs/ui_flow.md`.
- **OpenClaw Integration:** Every human approval triggers a cryptographic signature requirement.

### 2. True TDD Strategy (`/tests`)
- I have implemented **Failing Tests** for all core skills and API endpoints *prior* to implementation.
- This defines the "Goal Posts" for the AI agents, preventing hallucination during the build phase.

### 3. CI/CD & Automation
- **Dockerfile:** Full environment encapsulation ensuring "It works on every machine."
- **Makefile:** Standardized entry points:
  - `make setup`: Dependency installation.
  - `make test`: Runs the TDD suite inside the Docker container.
  - `make spec-check`: Custom script to verify alignment between specs and code.
- **GitHub Actions:** Automated linting and testing on every push.

##  How to Run
1. **Install Dependencies:** `make setup`
2. **Run Tests (Docker):** `make test`
3. **Launch Backend:** `python -m uvicorn backend.main:app --reload`
4. **Launch Frontend:** `streamlit run frontend/app.py`

##  IDE Agent Context
The `.cursor/rules` file governs the behavior of AI agents within this repo, enforcing:
- Spec-first development (No code without a ratified spec).
- Test-driven workflows.
- Security-first skill implementation.