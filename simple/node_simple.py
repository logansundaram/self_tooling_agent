from state import AgentState
from prompts import sys_msg_simple

def simple_node(llm_with_tools):
    def _node(state: AgentState):
        return {"messages": [llm_with_tools.invoke([sys_msg_simple] + state["messages"])]}
    return _node