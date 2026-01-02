from langchain_core.messages import SystemMessage

sys_msg_router = SystemMessage(content=(
    "Classify the user request.\n"
    "Output exactly one char: 1, 2, or 3.\n"
    "1=simple, 2=moderate, 3=complex.\n"
    "No other text."
))

# double check this prompt
sys_msg_normalizer = SystemMessage(content=(
    "You are a text normalizer.\n"
    "\n"
    "TASK:\n"
    "- Return the user's prompt with ONLY minimal grammar/spelling fixes.\n"
    "- Preserve meaning exactly. Do not rephrase.\n"
    "\n"
    "ALLOWED EDITS (ONLY):\n"
    "- Fix typos and misspellings.\n"
    "- Fix obvious grammar that does NOT change meaning.\n"
    "- Fix spacing.\n"
    "\n"
    "FORBIDDEN:\n"
    "- Do NOT add or remove words (except to fix a typo).\n"
    "- Do NOT change tone, emphasis, or punctuation style (no adding '!').\n"
    "- Do NOT add any preface like \"Sure\" or \"Here is\".\n"
    "- Do NOT add quotes, labels, markdown, or extra lines.\n"
    "\n"
    "OUTPUT FORMAT:\n"
    "- Output EXACTLY the normalized prompt and nothing else.\n"
    "- Single line if possible."
))


sys_msg_simple = SystemMessage(content=(
    "SIMPLE request.\n"
    "Answer directly and concisely.\n"
    "Do not mention routing/tiers."
))

sys_msg_moderate_planner = SystemMessage(content=(
    "You are a PARALLEL subtask decomposer for an AI agent.\n"
    "\n"
    "PRIMARY RULE (MOST IMPORTANT):\n"
    "- If the user's request can be completed accurately as a SINGLE task, output ONE subtask.\n"
    "- Only decompose when it is NECESSARY to improve accuracy or to produce multiple independent deliverables.\n"
    "- Do NOT break tasks down for the sake of decomposition.\n"
    "\n"
    "SECONDARY RULE (ALSO IMPORTANT):\n"
    "- Every subtask MUST be an execution brief (even if there is only one).\n"
    "- A subtask like \"Do X\" is invalid unless it specifies what artifact to produce.\n"
    "\n"
    "CONTEXT AVAILABLE TO EACH SUBTASK:\n"
    "- Original user prompt\n"
    "- Conversation message context\n"
    "- The subtask brief you output\n"
    "\n"
    "WHAT A VALID SUBTASK IS:\n"
    "- One node-sized deliverable completed in a single execution.\n"
    "- Produces a concrete artifact (spec, table, schema, checklist, decision record, test cases).\n"
    "- Answerable without implementing code or choosing tools unless explicitly requested.\n"
    "\n"
    "FORBIDDEN:\n"
    "- Generic project phases/checklists.\n"
    "- Vague bullets without an output artifact.\n"
    "- Solution content, how-to steps, or implementation details.\n"
    "\n"
    "OUTPUT FORMAT (MUST FOLLOW EXACTLY):\n"
    "- Output ONLY bullet points.\n"
    "- Output 1 to 4 bullets total.\n"
    "- EACH bullet MUST follow this template:\n"
    "  <Deliverable>: Use the original prompt + conversation context to produce <format>. "
    "Include: <3–8 essential fields>. Guardrails: <constraints>.\n"
    "- No nesting, numbering, headers, or extra text.\n"
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
