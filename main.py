import re
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, MessagesState, START, END
from langchain_core.messages import HumanMessage, SystemMessage

# can pivot to learned gates at a later time
from prompts import sys_msg_router, sys_msg_simple

#llms
from llms import llm, router, coder

from router import llm_router, route

from simple.node_simple import simple_node

from graphs.moderate import subgraph_moderate

def complex(state: MessagesState):
    return {"messages": [llm.invoke([sys_msg_simple] + state["messages"])]}


graph = StateGraph(MessagesState)
graph.add_node("llm_router", llm_router(router))
graph.add_node("simple", simple_node(llm))
graph.add_node("moderate", subgraph_moderate)
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

messages = [HumanMessage(content="write me a python script that uses dynamic programming")]
out = graph.invoke({"messages": messages})

for m in out["messages"]:
    m.pretty_print()