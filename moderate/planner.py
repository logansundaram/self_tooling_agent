from langgraph.graph import MessagesState
from prompts import sys_msg_moderate_planner

def moderate_planner(llm):
    def _node(state: MessagesState):
        return {"messages": [llm.invoke([sys_msg_moderate_planner] + state["messages"])]}
    return _node