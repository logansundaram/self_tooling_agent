from state import AgentState
from prompts import sys_msg_moderate_synthesizer

def moderate_synthesizer(llm):
    def _node(state: AgentState):
        msg = llm.invoke([sys_msg_moderate_synthesizer] + state["messages"][-2:])

        content = (getattr(msg, "content", "") or "").strip()
        tool_calls = (getattr(msg, "additional_kwargs", {}) or {}).get("tool_calls")
        model = (getattr(msg, "response_metadata", {}) or {}).get("model") or \
                (getattr(msg, "response_metadata", {}) or {}).get("model_name") or "unknown_model"

        print(f"[moderate_synthesizer] model={model} content_len={len(content)} tool_calls={bool(tool_calls)} preview={repr((msg.content or '')[:60])}")

        if (not content) and (not tool_calls):
            print("[moderate_synthesizer] DROPPED empty message")
            return {"messages": []}

        return {"messages": [msg]}
    return _node

