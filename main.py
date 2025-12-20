import re
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, MessagesState, START, END
from langchain_core.messages import HumanMessage, SystemMessage

# can pivot to learned gates at a later time
sys_msg_router = SystemMessage(content=(
    "You are a routing module in a larger AI agent.\n"
    "Return ONLY a single character: 1, 2, or 3.\n"
    "1 = simple request (direct answer, no tools, no multi-step planning)\n"
    "2 = moderate (some structure, a few steps, light tool use)\n"
    "3 = complex (multi-component system design, many constraints, code, evaluation, self-repair loops)\n"
    "No words, no punctuation, no explanation."
))

sys_msg_simple = SystemMessage(content=(
    "You are a Tier-1 execution model in a multi-tier AI agent.\n"
    "This request has already been classified as SIMPLE.\n\n"
    "Rules:\n"
    "- Answer directly and concisely.\n"
    "- Do NOT use tools.\n"
    "- Do NOT plan or decompose the task.\n"
    "- Do NOT mention routing, tiers, or internal agent structure.\n"
    "- Do NOT ask follow-up questions.\n"
    "- If formatting is requested, follow it exactly.\n"
    "Goal:\n"
    "Provide a correct, helpful response in a single pass."
))

router = ChatOllama(
    model="ministral-3:8b",
    temperature=0,
)

llm = ChatOllama(
    model="gpt-oss:20b",
    temperature=0,
)

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