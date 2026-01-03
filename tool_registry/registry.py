from langchain.tools import tool
import os
from dotenv import load_dotenv


load_dotenv(".env.local")

tavily_api_key = os.getenv("TAVILY_API_KEY")

from langchain_tavily import TavilySearch

#@tool("calculator", description="Performs arithmetic calculations. Use this for any math problems.")
#def calc(expression: str) -> str:
#    print("tool called")
#    return str(eval(expression))

search = TavilySearch(
    max_results=5, #may be too many
    topic="general",
    # include_answer=False,
    # include_raw_content=False,
    # include_images=False,
    # include_image_descriptions=False,
    # search_depth="basic",
    # time_range="day",
    # include_domains=None,
    # exclude_domains=None
    )

#@tool("search", description="Perform an online search. Use this for any instance when specific info is necessary")
#def search(query: str) -> str:
    
    #return tool

@tool("add", description="Performs arithmetic addition. Use this for any math problems.")
def add(a: int, b : int) -> int:
    return a + b


@tool("subtract", description="Performs arithmetic subtraction. Use this for any math problems.")
def subtract(a: int, b : int) -> int:
    return a + b


@tool("multiplication", description="Performs arithmetic multiplication. Use this for any math problems.")
def multiplication(a: int, b : int) -> int:
    return a + b


@tool("division", description="Performs arithmetic division. Use this for any math problems.")
def division(a: int, b : int) -> int:
    return a/b


tools = [search, add]
tools_by_name = {tool.name: tool for tool in tools}
