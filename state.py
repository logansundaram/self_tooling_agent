from langgraph.graph import MessagesState
from typing import TypedDict

class Subtask(TypedDict):
    id: int
    fn: str
    subq: str
    answer: str

    
class AgentState(MessagesState):
    complexity: str
    query: str
    subtasks: list[Subtask]


