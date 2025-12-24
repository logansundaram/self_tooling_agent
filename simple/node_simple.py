from langgraph.graph import MessagesState
from prompts import sys_msg_simple

def simple_node(llm):
    def _node(state: MessagesState):
        return {"messages": [llm.invoke([sys_msg_simple] + state["messages"])]}
    return _node