from state import AgentState
from prompts import sys_msg_moderate_repair

def repair_routing_function(state: AgentState) -> bool:
    for subtask in state["subtasks"]:
        if not subtask.verdict:
            return False
    return True

def moderate_repair(llm):
    def _node(state: AgentState):
        msg = llm.invoke([sys_msg_moderate_repair] + state["messages"][-2:])
        return {"messages": [msg]}
    return _node
