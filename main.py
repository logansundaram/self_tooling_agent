import re
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, MessagesState, START, END
from langchain_core.messages import HumanMessage, SystemMessage

# can pivot to learned gates at a later time
from prompts.system_prompts import sys_msg_router, sys_msg_simple

#llms
from llms import llm, router

def llm_router(state: MessagesState):
    return {"messages": [router.invoke([sys_msg_router] + state["messages"])]}

def simple(state: MessagesState):
    return {"messages": [llm.invoke([sys_msg_simple] + state["messages"])]}

def moderate(state: MessagesState):
    return {"messages": [llm.invoke([sys_msg_simple] + state["messages"])]}

def complex(state: MessagesState):
    return {"messages": [llm.invoke([sys_msg_simple] + state["messages"])]}

# routing function for conditional edges
def route(state: MessagesState) -> str:
    text = state["messages"][-1].content.strip()
    m = re.search(r"[123]", text)
    label = m.group(0) if m else "1"
    return {"1": "simple", "2": "moderate", "3": "complex"}[label]

graph = StateGraph(MessagesState)
graph.add_node("llm_router", llm_router)
graph.add_node("simple", simple)
graph.add_node("moderate", moderate)
graph.add_node("complex", complex)

graph.add_edge(START, "llm_router")

graph.add_conditional_edges(
    "llm_router",
    route,
    {
        "simple": "simple",
        "moderate": "moderate",
        "complex": "complex",
    },
)

graph.add_edge("simple", END)
graph.add_edge("moderate", END)
graph.add_edge("complex", END)

graph = graph.compile()

messages = [HumanMessage(content="say hello world")]
out = graph.invoke({"messages": messages})

for m in out["messages"]:
    m.pretty_print()