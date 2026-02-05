#!/usr/bin/env python3
"""
Export JSON schemas from pydantic models to specs/schemas/
Run with: python scripts/export_schemas.py
"""

import os
import json
from pathlib import Path

# Ensure repo paths
ROOT = Path(__file__).resolve().parents[1]
SCHEMAS_DIR = ROOT / "specs" / "schemas"
SCHEMAS_DIR.mkdir(parents=True, exist_ok=True)

# Import models (import here so script is still a file even if pydantic missing for now)
try:
    from common.models import AgentPersona, Task, TaskInput
except Exception as e:
    print("ERROR importing models:", e)
    print("If pydantic is not installed, run: pip install pydantic")
    raise

def write_schema(model, name):
    schema = model.schema()
    path = SCHEMAS_DIR / f"{name}.json"
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(schema, fh, indent=2, ensure_ascii=False)
    print("Wrote", path)

def main():
    write_schema(AgentPersona, "agent_persona")
    write_schema(TaskInput, "task_input")
    write_schema(Task, "task")

if __name__ == "__main__":
    main()