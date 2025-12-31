from langgraph.graph import MessagesState

class AgentState(MessagesState):
    complexity: str
    query: str
    #subtasks: need to have a list of in which the planner node can fill
