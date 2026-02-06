from .planner import Planner
from .worker import Worker
from .judge import Judge


class Orchestrator:
    """Simple Planner → Worker → Judge loop."""

    def __init__(self):
        self.planner = Planner()
        self.worker = Worker()
        self.judge = Judge()

    def run(self, goal: str):
        tasks = self.planner.plan(goal)
        outputs = []

        for t in tasks:
            result = self.worker.run(t)
            if self.judge.evaluate(result):
                outputs.append(result)

        return outputs
