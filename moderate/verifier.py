from state import AgentState
from prompts import sys_msg_moderate_verifier
from pydantic import Field, BaseModel
from typing import List


class Check(BaseModel):
    valid: bool = Field(..., description="Return a true or false bool if the output matches the requierments of the check. Return true if in doubt")

def moderate_verifier(llm):
    def _node(state: AgentState):
        structured_llm = llm.with_structured_output(Check)

        updated = state["subtasks"]
        for subtask in updated:
            check = structured_llm.invoke([sys_msg_moderate_verifier] + [subtask.check] + [subtask.answer])
            subtask.check = check

        return {"subtasks" : updated}
    return _node
