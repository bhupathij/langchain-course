from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from tavily import TavilyClient

tavily = TavilyClient()

@tool
def search(query:str) -> str:
    """
    Tool that searches over the internet
    Args: 
        query: The query to search for
    Returns:
        The search result
    """

    print(f"Searching for {query}")
    return tavily.search(query=query)

llm = ChatOllama(model="gpt-oss:20b")
tools = [search]
agent = create_agent(model=llm,tools=tools)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": [HumanMessage(content="Search for 3 job postings for AI Engineer in the Pune, Hyderabad on linkedin and list their details")]})
    print(result)

if __name__ == "__main__":
    main()
