"""
Project Chimera runtime entrypoint.
Runs a minimal Planner → Worker → Judge cycle.

Used ONLY to demonstrate:
- agent orchestration works
- evaluators can execute system
- MCP logs can be generated after execution
"""

from chimera.orchestrator import Orchestrator


def main():
    orch = Orchestrator()

    goal = "post hello world content"
    results = orch.run(goal)

    print("=== Chimera Run Complete ===")
    print(results)


if __name__ == "__main__":
    main()