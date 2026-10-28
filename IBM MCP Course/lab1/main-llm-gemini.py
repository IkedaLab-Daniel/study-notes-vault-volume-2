import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver


load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    google_api_key=os.environ["GEMINI_API_KEY"],
)

response = llm.invoke("Hello, Gemini!")

async def main():
    """
    Main function that sets up and runs an AI agent with access to multiple MCP servers
    The agent can access context7 library documentation and Met Museum collections.
    """

    # Configure MCP servers
    # These servers provide tools that the AI Agente can use
    client = MultiServerMCPClient(
        {
            "context7": {
                "url": "https://mcp.context7.com/mcp",
                "transport": "streamable_http",
            },
            "met-museum": {
                "command": "npx",
                "args": ["-y", "metmuseum-mcp"],
            }
        }
    )
