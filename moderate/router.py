from state import AgentState
from prompts import sys_msg_moderate_router

#router node will be work on later
def moderate_router(llm):
    def _node(state: AgentState):
        msg = llm.invoke([sys_msg_moderate_router] + state["messages"][-2:])

        return {"messages": [msg]}
    return _node
