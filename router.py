import re
from langgraph.graph import MessagesState
from prompts import sys_msg_router, sys_msg_normalizer
from state import AgentState


def llm_router(router):
    def _node(state: AgentState):
        
        return {
            "complexity": router.invoke([sys_msg_router] + state["messages"]).content,
            "query": router.invoke([sys_msg_normalizer] + state["messages"]).content
        }
    return _node


# routing function for conditional edges
import re

def route(state: AgentState):
    raw = state["complexity"]
    raw = (raw or "").strip()

    m = re.search(r"[123]", raw)
    digit = m.group(0) if m else "2"

    return {"1": "simple", "2": "moderate", "3": "complex"}[digit]
