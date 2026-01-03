from state import AgentState
from prompts import sys_msg_simple_synthesize
#needs new systemprompts


def tool_node_synthesize(llm):
    def _node(state: AgentState):
        return {"messages": [llm.invoke([sys_msg_simple_synthesize] + state["messages"])]}
    return _node