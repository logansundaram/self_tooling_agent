from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, MessagesState, START, END
from langchain_core.messages import HumanMessage, SystemMessage

#for the state of the graph
from typing import TypedDict, NotRequired
from state import AgentState

# can pivot to learned gates at a later time
from prompts import sys_msg_router, sys_msg_simple

#llms
from llms import llm, router, coder, llm_with_tools

from router import llm_router, route

from simple.node_simple import simple_node

from graphs.moderate import subgraph_moderate
from graphs.simple import subgraph_simple



def complex_node(state: MessagesState):
    return {"messages": [llm.invoke([sys_msg_simple] + state["messages"])]}


def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("llm_router", llm_router(router))
    #change to subgraph_simple if necessary
    graph.add_node("simple", subgraph_simple)
    graph.add_node("moderate", subgraph_moderate)
    graph.add_node("complex", complex_node)

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

    return graph.compile()


def run_chatbot():
    graph = build_graph()

    messages = []

    print("chatbot online\n")

    while True:
        try:
            user_text = input("you> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nbye")
            break

        if not user_text:
            continue

        if user_text.lower() in {"exit", "quit"}:
            print("bye")
            break

        if user_text.lower() == "reset":
            messages = []
            print("(history cleared)\n")
            continue

        prev_len = len(messages)

        messages.append(HumanMessage(content=user_text))
        out = graph.invoke({"messages": messages})

        messages = out["messages"]

        
        for m in messages[prev_len:]:
            m.pretty_print()

if __name__ == "__main__":
    run_chatbot()
