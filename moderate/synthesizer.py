from state import AgentState
from prompts import sys_msg_moderate_synthesizer
from langchain_core.messages import HumanMessage
from state import Subtask

def moderate_synthesizer(llm):
    def _node(state: AgentState):

        combined_tasks = ""
        for subtask in state["subtasks"]:
            combined_tasks += subtask.answer
           


        msg = llm.invoke([sys_msg_moderate_synthesizer] + [combined_tasks])

        return {"messages": [msg]}
    return _node

