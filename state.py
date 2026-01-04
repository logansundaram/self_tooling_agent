from langgraph.graph import MessagesState
from pydantic import BaseModel, Field
from typing import Optional

class Subtask(BaseModel):
    task: str = Field(..., description="Instruction for executor")
    expected: str = Field(..., description="Acceptance criteria / deliverable description")
    check: str = Field(..., description="Verification rubric / tests")
    answer: Optional[str] = Field(None, description="Filled by executor")
    verdict: Optional[bool] = Field(None, description="Filled by verifier")

class AgentState(MessagesState):
    complexity: str
    query: str
    subtasks: list[Subtask]


