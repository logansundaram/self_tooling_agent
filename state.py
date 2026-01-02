from langgraph.graph import MessagesState
from typing import TypedDict

class Subtask(TypedDict):
    id: str
    goal: str
    outcome: str

class AgentState(MessagesState):
    complexity: str
    query: str
    subtasks: list[Subtask]


