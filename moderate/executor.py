from langgraph.graph import MessagesState
from prompts import sys_msg_moderate_executor

def moderate_executor(llm_with_tools):
    def _node(state: MessagesState):
        msg = llm_with_tools.invoke([sys_msg_moderate_executor] + state["messages"][-2:])

        content = (getattr(msg, "content", "") or "").strip()
        tool_calls = (getattr(msg, "additional_kwargs", {}) or {}).get("tool_calls")
        model = (getattr(msg, "response_metadata", {}) or {}).get("model") or \
                (getattr(msg, "response_metadata", {}) or {}).get("model_name") or "unknown_model"

        print(f"[moderate_executor] model={model} content_len={len(content)} tool_calls={bool(tool_calls)} preview={repr((msg.content or '')[:60])}")

        # Important: keep tool_calls even if content empty
        if (not content) and (not tool_calls):
            print("[moderate_executor] DROPPED empty message")
            return {"messages": []}

        return {"messages": [msg]}
    return _node
