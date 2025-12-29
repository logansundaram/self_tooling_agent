from moderate.planner import moderate_planner
from moderate.router import moderate_router
from moderate.executor import moderate_executor
from moderate.repair import moderate_repair
from moderate.verifier import moderate_verifier
from moderate.synthesizer import moderate_synthesizer

from langgraph.graph import StateGraph, MessagesState, START, END


from llms import llm, llm_with_tools

subgraph_moderate_builder = StateGraph(StateGraph)

subgraph_moderate_builder.add_node(moderate_planner(llm))
subgraph_moderate_builder.add_node(moderate_router(llm))
subgraph_moderate_builder.add_node(moderate_executor(llm_with_tools))
subgraph_moderate_builder.add_node(moderate_repair(llm))
subgraph_moderate_builder.add_node(moderate_verifier(llm))
subgraph_moderate_builder.add_node(moderate_synthesizer(llm))

subgraph_moderate_builder.add_edge(START, "moderate_planner")
subgraph_moderate = subgraph_moderate_builder.compile()  