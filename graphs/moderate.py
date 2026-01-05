from moderate.planner import moderate_planner
from moderate.router import moderate_router
from moderate.executor import moderate_executor
from moderate.repair import moderate_repair
from moderate.repair import repair_routing_function
from moderate.verifier import moderate_verifier
from moderate.synthesizer import moderate_synthesizer

from langgraph.graph import StateGraph, START, END
from state import AgentState


from llms import llm, llm_with_tools

subgraph_moderate_builder = StateGraph(AgentState)

subgraph_moderate_builder.add_node("moderate_planner", moderate_planner(llm))
#subgraph_moderate_builder.add_node("moderate_router", moderate_router(llm))
subgraph_moderate_builder.add_node("moderate_executor", moderate_executor(llm_with_tools))
subgraph_moderate_builder.add_node("moderate_repair", moderate_repair(llm_with_tools))
subgraph_moderate_builder.add_node("moderate_verifier", moderate_verifier(llm))
subgraph_moderate_builder.add_node("moderate_synthesizer", moderate_synthesizer(llm))

subgraph_moderate_builder.add_edge(START, "moderate_planner")
#subgraph_moderate_builder.add_edge("moderate_router", "moderate_executor")



subgraph_moderate_builder.add_edge("moderate_planner", "moderate_executor")
#need a react loop here
subgraph_moderate_builder.add_edge("moderate_executor", "moderate_verifier")

#need a loop here to check robustness
subgraph_moderate_builder.add_conditional_edges("moderate_verifier", repair_routing_function,
                                                {
                                                    True: "moderate_synthesizer",
                                                    False: "moderate_repair",
                                                })
subgraph_moderate_builder.add_edge("moderate_repair", "moderate_synthesizer")
subgraph_moderate_builder.add_edge("moderate_synthesizer", END)
 
subgraph_moderate = subgraph_moderate_builder.compile()  

