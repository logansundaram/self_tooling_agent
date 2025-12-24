from langgraph.graph import StateGraph, MessagesState, START, END
from llms import llm
from prompts import sys_msg_simple

def moderate(state: MessagesState):
    return {"messages": [llm.invoke([sys_msg_simple] + state["messages"])]}