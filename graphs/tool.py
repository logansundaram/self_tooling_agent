from langgraph.graph import START, END, StateGraph
from state import AgentState


from tool_calling.node_tool_decide import tool_node_decide
from tool_calling.node_tool_execute import tool_node_execute
from tool_calling.node_tool_synthesize import tool_node_synthesize

from llms import llm_with_tools, llm

tool_graph = StateGraph(AgentState)
tool_graph.add_node("decide", tool_node_decide(llm_with_tools))
tool_graph.add_node("execute", tool_node_execute())
tool_graph.add_node("synthesize", tool_node_synthesize(llm))

tool_graph.add_edge(START, "decide")
tool_graph.add_edge("decide", "execute")
tool_graph.add_edge("exectue", "synthesize")
tool_graph.add_edge("synthesize", END)


tool_graph.compile()