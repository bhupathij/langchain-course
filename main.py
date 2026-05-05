from dotenv import load_dotenv
from typing import List
from pydantic import BaseModel, Field

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch

class Source(BaseModel):
    url:str = Field(description="The url of the source")

class AgentResponse(BaseModel):
    answer:str = Field(description="The answer to the user's question")
    sources:List[Source] = Field(default_factory=list, description="List of sources used to answer the question")

llm = ChatOllama(model="gpt-oss:20b")
tools = [TavilySearch()]
agent = create_agent(model=llm,tools=tools,response_format=AgentResponse)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": [HumanMessage(content="Search for 3 job postings for AI Engineer in the Pune, Hyderabad on linkedin and list their details")]})
    print(result)

if __name__ == "__main__":
    main()
