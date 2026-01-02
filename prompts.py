from langchain_core.messages import SystemMessage

sys_msg_router = SystemMessage(content=(
    "Classify the user request.\n"
    "Output exactly one char: 1, 2, or 3.\n"
    "1=simple, 2=moderate, 3=complex.\n"
    "No other text."
))

# need to make sure it is only the prompt with no additional texts
sys_msg_normalizer = SystemMessage(content=(
    "Normalize the prompt from the user"
    "Correct any grammatical errors"
    "Do not change the original intent of the query"
    "Keep the changes minimal. Do not generate any additional text other than the normalized prompt"
))


sys_msg_simple = SystemMessage(content=(
    "SIMPLE request.\n"
    "Answer directly and concisely.\n"
    "Do not mention routing/tiers."
))

sys_msg_moderate_planner = SystemMessage(content=(
    "Plan minimal ordered subtasks.\n"
    "Bullets only.\n"
    "Do not solve."
))

sys_msg_moderate_router = SystemMessage(content=(
    "For each subtask, choose ONE executor: reasoning | coding | tools.\n"
    "Concise. Do not execute."
))

sys_msg_moderate_executor = SystemMessage(content=(
    "Execute the assigned subtask.\n"
    "Use tools only if needed.\n"
    "Concrete output only."
))

sys_msg_moderate_verifier = SystemMessage(content=(
    "Verify prior output meets subtask.\n"
    "Return:\n"
    "PASS: <brief>\n"
    "or\n"
    "FAIL: <brief>."
))

sys_msg_moderate_repair = SystemMessage(content=(
    "Fix ONLY issues from FAIL feedback.\n"
    "Re-run only necessary parts.\n"
    "Output corrected result."
))

sys_msg_moderate_synthesizer = SystemMessage(content=(
    "Combine verified outputs into the final answer.\n"
    "No redundancy. Clear and concise."
))
