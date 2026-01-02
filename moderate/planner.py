from state import AgentState, Subtask
from prompts import sys_msg_moderate_planner
from pydantic import BaseModel, Field

class SubtaskPlanning(BaseModel):
    #search_query: str = Field(None, description="Query that is optimized web search.")
    subtasks: list[Subtask] = Field(
        None, description="Output a list of independent subtasks"
    )

def moderate_planner(llm):
    def _node(state: AgentState):

        #normalized query to be worked on
        #query = state["query"]

        structured_llm = llm.with_structured_output(SubtaskPlanning)

        output = structured_llm.invoke([sys_msg_moderate_planner] + state["messages"][-2:])

        msg = llm.invoke([sys_msg_moderate_planner] + state["messages"][-2:])


        content = (getattr(msg, "content", "") or "").strip()
        tool_calls = (getattr(msg, "additional_kwargs", {}) or {}).get("tool_calls")
        model = (getattr(msg, "response_metadata", {}) or {}).get("model") or \
                (getattr(msg, "response_metadata", {}) or {}).get("model_name") or "unknown_model"

        print(f"[moderate_planner] model={model} content_len={len(content)} tool_calls={bool(tool_calls)} preview={repr((msg.content or '')[:60])}")

        if (not content) and (not tool_calls):
            print("[moderate_planner] DROPPED empty message")
            return {"messages": []}

        return {
            "messages": [msg],
            "subtasks": output
            }
    return _node
