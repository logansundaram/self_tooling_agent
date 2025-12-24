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
def route(state: MessagesState) -> str:
    text = state["messages"][-1].content.strip()
    m = re.search(r"[123]", text)
    label = m.group(0) if m else "1"
    return {"1": "simple", "2": "moderate", "3": "complex"}[label]