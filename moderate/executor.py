from state import AgentState
from langchain_core.messages import HumanMessage

from state import Subtask

from prompts import sys_msg_moderate_executor

def moderate_executor(llm_with_tools):
    def _node(state: AgentState):
        updated = state["subtasks"]
    
        #i = 0
        for subtask in updated:
            subtask.answer = llm_with_tools.invoke([sys_msg_moderate_executor] + [HumanMessage(content=subtask.task)]).content
            #print(f"task\n{i}")
            #i=i+1
            #print(subtask.answer)
            # + state["messages"][-2:] 
        return {"subtasks": updated}
    return _node