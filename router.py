import re
from langgraph.graph import MessagesState
from prompts import sys_msg_router


def llm_router(router):
    def _node(state: MessagesState):
        return {
            "messages": [router.invoke([sys_msg_router] + state["messages"])]
        }
    return _node


# routing function for conditional edges
import re

def route(state):
    raw = getattr(state["messages"][-1], "content", "")
    raw = (raw or "").strip()

    m = re.search(r"[123]", raw)
    digit = m.group(0) if m else "2"

    return {"1": "simple", "2": "moderate", "3": "complex"}[digit]
