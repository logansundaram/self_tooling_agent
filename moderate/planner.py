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

        msg = llm.invoke([sys_msg_moderate_planner] + state["messages"][-2:])


        content = (getattr(msg, "content", "") or "").strip()
        tool_calls = (getattr(msg, "additional_kwargs", {}) or {}).get("tool_calls")
        model = (getattr(msg, "response_metadata", {}) or {}).get("model") or \
                (getattr(msg, "response_metadata", {}) or {}).get("model_name") or "unknown_model"

        print(f"[moderate_planner] model={model} content_len={len(content)} tool_calls={bool(tool_calls)} preview={repr((msg.content or '')[:60])}")

        if (not content) and (not tool_calls):
            print("[moderate_planner] DROPPED empty message")
            return {"messages": []}
        print(plan.subtasks)
        return {
            "subtasks": plan.subtasks
            }
    
    return _node
