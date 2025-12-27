from langgraph.graph import MessagesState
from prompts import sys_msg_moderate_executor

def moderate_executor(llm_with_tools):
    def _node(state: MessagesState):
        return {"messages": [llm_with_tools.invoke([sys_msg_moderate_executor] + state["messages"])]}
    return _node