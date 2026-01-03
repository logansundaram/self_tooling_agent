from langgraph.graph import START, END, StateGraph

from simple.node_simple import simple_node
from simple.node_simple_tool import simple_node_tool
from simple.node_simple_synthesis import simple_node_synthesis

from state import AgentState

from llms import llm_with_tools
from llms import llm


graph = StateGraph(AgentState)
graph.add_node("simple", simple_node(llm_with_tools))
graph.add_node("tool", simple_node_tool())
graph.add_node("synthesize", simple_node_synthesis(llm))

graph.add_edge(START, "simple")
graph.add_edge("simple", "tool")
graph.add_edge("tool", "synthesize")
graph.add_edge("synthesize", END)
subgraph_simple = graph.compile()