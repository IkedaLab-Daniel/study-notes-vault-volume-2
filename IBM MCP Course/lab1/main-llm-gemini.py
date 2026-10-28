import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()

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

    # Init Gemini language Model
    # this model will power the AI agent's reasoning and responses
    gemini_model = ChatGoogleGenerativeAI(
        model="gemini-3-flash-preview",
        google_api_key=os.environ["GEMINI_API_KEY"],
    )

    # ? 1 - Retrieve all available tools from the configured MCP servers
    tools = await client.get_tools()

    # ? 2 - Set up conversation memory
    checkpointer = InMemorySaver()

    # ? 3 - Configure for conversation persistence
    # ? The thread_id ensure all messages in this sessions are grouped together
    config = {"configurable": {"thread_id": "conversation_id"}}


