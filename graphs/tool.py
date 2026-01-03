from langgraph.graph import START, END, StateGraph
from state import AgentState


from tool_calling.node_tool_decide import tool_node_decide
from tool_calling.node_tool_execute import tool_node_execute
from tool_calling.node_tool_synthesize import tool_node_synthesize

from llms import llm_with_tools, llm

graph = StateGraph(AgentState)
graph.add_node("decide", tool_node_decide(llm_with_tools))
graph.add_node("execute", tool_node_execute())
graph.add_node("synthesize", tool_node_synthesize(llm))

graph.add_edge(START, "decide")
graph.add_edge("decide", "execute")
graph.add_edge("exectue", "synthesize")
graph.add_edge("synthesize", END)


graph.compile()