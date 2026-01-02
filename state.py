from langgraph.graph import MessagesState
from typing import TypedDict

class Subtask(TypedDict):
    task: str
    answer: str
    check: str = ""


class AgentState(MessagesState):
    complexity: str
    query: str
    subtasks: list[Subtask]


