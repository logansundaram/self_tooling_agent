from langgraph.graph import MessagesState

class AgentState(MessagesState):
    complexity: str
    query: str
