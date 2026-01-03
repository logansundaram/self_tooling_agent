from state import AgentState
from prompts import sys_msg_simple
#needs new systemprompts

def tool_node_decide(llm_with_tools):
    def _node(state: AgentState):
        return {"messages": [llm_with_tools.invoke([sys_msg_simple] + state["messages"])]}
    return _node