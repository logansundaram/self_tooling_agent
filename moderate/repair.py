from state import AgentState
from prompts import sys_msg_moderate_repair

def repair_routing_function(state: AgentState) -> bool:
    for subtask in state["subtasks"]:
        if not subtask.verdict:
            return False
    return True

def moderate_repair(llm_with_tools):
    def _node(state: AgentState):
        updated = state["subtasks"]
        for subtask in updated:
                if not subtask.verdict:
                    subtask.answer = llm_with_tools.invoke([sys_msg_moderate_repair] + [subtask.check] + [subtask.task]).content
        return {"subtasks": updated}
    return _node
