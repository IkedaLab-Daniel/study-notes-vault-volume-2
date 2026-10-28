import asyncio
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

    # ? 4 - ReAct Agent
    agent = create_react_agent(
        model=gemini_model,             # language model
        tools=tools,                    # tools in the MCP
        checkpointer=checkpointer       # memory
    )

    # -- Initial message

    response = await agent.invoke(
        {"messages": [
            # ? System
            {"role": "system",
             "content": "You are a smart, useful agent with tools to access code library documentation and the Met Museum collection."},
            # ? user message
            {"role": "user",
             "content": "Give a brief introduction of what you do and the tools you can access."}
        ]},
        config=config
    )

    print(response['messages'][-1].content)

    	# Main interaction loop - allows continuous conversation with the agent
    while True:
        # Display menu options to the user
        choice = input("""
Menu:
1. Ask the agent a question
2. Quit
Enter your choice (1 or 2): """)

        if choice == "1":
            # Get user's question
            print("Your question")
            query = input("> ")

            # Send the user's question to the agent
            # The agent will have access to the full conversation history
            response = await agent.ainvoke(
                {"messages": query},        # User's current question
                config=config              # Maintains conversation thread
            )
            # Display the agent's response
            print(response['messages'][-1].content)
        else:
            # Exit the program for any choice other than "1"
            print("Goodbye!")
            break

# Entry point - runs the main function when script is executed directly
if __name__ == "__main__":
    # Use asyncio to run the async main function
    asyncio.run(main())
