from langgraph.graph import MessagesState
from prompts import sys_msg_moderate_verifier

def moderate_verifier(llm):
    def _node(state: MessagesState):
        return {"messages": [llm.invoke([sys_msg_moderate_verifier] + state["messages"])]}
    return _node