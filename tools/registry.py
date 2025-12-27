from langchain.tools import tool

@tool("calculator", description="Performs arithmetic calculations. Use this for any math problems.")
def calc(expression: str) -> str:
    return str(eval(expression))

@tool("search", description="Perform an online search. Use this for any ionstance when specific info is necessary")
def search(expression: str) -> str:
    return expression

tools = [calc, search]