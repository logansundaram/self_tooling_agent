from langgraph.graph import MessagesState
from prompts import sys_msg_moderate_router

def moderate_router(llm):
    def _node(state: MessagesState):
        return {"messages": [llm.invoke([sys_msg_moderate_router] + state["messages"])]}
    return _node