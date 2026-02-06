# Project Chimera — Copilot / IDE Agent Instructions

## Project Context
This repository is **Project Chimera**: an autonomous influencer system built around a hierarchical swarm of agents (Planner → Worker → Judge) that use MCP-backed tools/skills. The canonical specs live in `specs/` and the exported JSON schemas are in `specs/schemas/`. All runtime logging must go to `mcp_sense.log`.

## Prime Directive (MUST follow)
- **NEVER** generate, modify, or commit implementation code without first:
  1. Reading the relevant spec files in `specs/` (start with `specs/_meta.md`, then `specs/technical.md`).
  2. Producing a concise **written plan** that exactly states which spec(s) it follows, which files will be changed, and what the expected tests are.
  3. Waiting for the human to confirm the plan before writing any code.

## Traceability Rule
- For every proposed code change, provide a short "Trace" block that includes:
  - `Spec references:` list of spec file paths and JSON schema names used
  - `Planned files:` list of repo file paths you will modify/create
  - `Tests to run:` exact pytest files or commands to validate changes
- Example trace format:
```
TRACE:
Spec references: specs/technical.md, specs/schemas/task.json
Planned files: skills/download_video/__init__.py, tests/test_skills_interface.py
Tests to run: pytest tests/test_skills_interface.py -q
```

## Required pre-checks before any code generation
- Confirm the current branch is not `main` (create a feature branch).
- Confirm `make test` (or `pytest -q`) has been run and failing tests captured to `tests/failing_output.txt`.
- Confirm `mcp_sense.log` was updated from VS Code integrated terminal after the last agent action.

## Agent Interaction — EXACT PROMPT TO USE (in VS Code)
When you ask the IDE agent to make a change, use this exact template (copy-paste):

```
TASK REQUEST:
1) Read these specs: specs/_meta.md and specs/technical.md
2) Produce a concise plan (max 8 lines) using the TRACE format below
3) Wait for human confirmation (do NOT write code yet)

TRACE:
Spec references: <list>
Planned files: <list>
Tests to run: <pytest command>
```

## Response Handling Rules (what the agent must output)
- The agent must always output a `PLAN` section (max 8 lines) and a `TRACE` block before any code.
- The agent must then wait for the human to confirm by replying `CONFIRM`.
- If the agent produces code without a confirmed PLAN, that is a violation.

## Logging & Telemetry
- After any agent-driven action, the agent (or the human operator) must run or trigger `scripts/mcp_client.py` to emit MCP telemetry and append the entry to `mcp_sense.log`.
- The agent should include the exact command to run the telemetry client in its plan (e.g., `python scripts/mcp_client.py`).

## Security & Safety
- Never include secrets, API keys, or personal tokens in code or logs.
- If a change touches external integrations, the agent must flag it and require explicit human sign-off.

## Example human/agent interaction (succinct)
1. Human pastes the TASK REQUEST template into Copilot chat.
2. Agent replies with PLAN + TRACE.
3. Human types `CONFIRM`.
4. Agent writes code into a new feature branch and shows modified file list.
5. Human runs `make test` and `python scripts/mcp_client.py` to produce logs and failing/passing outputs.

## Contact
If uncertain, always stop and ask: "Do you want me to propose a plan or implement it now?"