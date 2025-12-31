from langchain.tools import tool

#@tool("calculator", description="Performs arithmetic calculations. Use this for any math problems.")
#def calc(expression: str) -> str:
#    print("tool called")
#    return str(eval(expression))

@tool("search", description="Perform an online search. Use this for any ionstance when specific info is necessary")
def search(expression: str) -> str:
    return expression

@tool("add", description="Performs arithmetic additions. Use this for any math problems.")
def add(a: int, b : int) -> int:
    return a + b


tools = [search, add]
tools_by_name = {tool.name: tool for tool in tools}
