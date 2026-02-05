from typing import List, Optional
from pydantic import BaseModel, Field


class AgentPersona(BaseModel):
    id: Optional[str] = Field(None, description="Agent persona unique id")
    name: str = Field(..., description="Human-friendly persona name")
    role: Optional[str] = Field(None, description="Short role description")
    goals: Optional[List[str]] = Field([], description="High-level goals for this persona")
    metadata: Optional[dict] = Field({}, description="Freeform metadata")


class TaskInput(BaseModel):
    # Generic key-value input bag — specific skills can refine their own schema
    inputs: dict = Field(..., description="Input parameters for the task")


class Task(BaseModel):
    id: Optional[str] = Field(None, description="Task unique id")
    type: str = Field(..., description="Task type (e.g., download_video, transcribe)")
    created_by: Optional[str] = Field(None, description="Creator (planner/agent id)")
    created_at: Optional[str] = Field(None, description="ISO timestamp")
    payload: TaskInput = Field(..., description="Task payload according to skill schema")
    priority: Optional[int] = Field(0, description="Priority; higher means earlier execution")
    status: Optional[str] = Field("pending", description="Task status e.g. pending, running, done, failed")
    result: Optional[dict] = Field(None, description="Execution result or error details")