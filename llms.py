from langchain_ollama import ChatOllama
from tool_registry.registry import tools

router = ChatOllama(
    model="ministral-3:8b",
    temperature=0,
)

coder = ChatOllama(
    model="devstral-small-2:24b",
    temperature=0,
)

llm = ChatOllama(
    model="gpt-oss:20b",
    temperature=0,
)

llm_with_tools = ChatOllama(
    model="gpt-oss:20b",
    temperature=0,
    streaming = False,
)

llm_with_tools = llm_with_tools.bind_tools(tools)