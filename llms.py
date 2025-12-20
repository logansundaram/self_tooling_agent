from langchain_ollama import ChatOllama

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