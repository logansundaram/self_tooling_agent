from state import AgentState, Subtask
from typing import List
from prompts import sys_msg_moderate_planner
from pydantic import BaseModel, Field

class Plan(BaseModel):
    subtasks: List[Subtask] = Field(default_factory=list)

def moderate_planner(llm):
    def _node(state: AgentState):

        #normalized query to be worked on
        #query = state["query"]

        structured_llm = llm.with_structured_output(Plan)

        plan = structured_llm.invoke([sys_msg_moderate_planner] + state["messages"][-2:])

        return {
            "subtasks": plan.subtasks
            }
    
    return _node
