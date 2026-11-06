import asyncio
from fastmcp import Client
from fastmcp.client.transports import StdioTransport, StreamableHttpTransport

PORT = 8000
transport_http = StreamableHttpTransport(
    url = f"http://127.0.0.1:{PORT}/mcp"
)

http_client = Client(transport_http)
print('http_client', http_client)

async def test_client_http(client: Client, a: int, b: int) -> int:
    async with client:
        result = await client.call_tool("add", {"a": a, "b": b})
        return result

response = asyncio.run(test_client_http(http_client, 4, 5))
print(response.content[0].text)

## -- Get tools --
async def get_tool_list(client: Client):
    async with client:
        return await client.list_tools()

response = asyncio.run(get_tool_list(http_client))
for tool in response:
    print(f"\n{'=' * 60}")
    print(f"🔧 Tool: {tool.name}")
    print(f"{'=' * 60}")
    print(f"Description : {tool.description}")
    print(f"Input Schema: {tool.inputSchema}")
    print(f"Output Schema: {tool.outputSchema}")

# ———— LangChain Tools with HTTP MCP Servers —————
import os
from dotenv import load_dotenv
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client

# !!!
from server import print_stream_info


load_dotenv()
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    google_api_key=os.environ["GEMINI_API_KEY"],
)

async def main():
    async with streamable_http_client(f"http://127.0.0.1:{PORT}/mcp") as (read, write, _sid):
        print_stream_info(read, write, _sid, verbose=True)


if __name__ == "__main__":
    asyncio.run(main())