from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport, StdioTransport
import asyncio

stdio_transport = StdioTransport(
    command="npx",
    args=["-y", "@upstash/cpmtext7-mcp"]
)

print(stdio_transport)

# ? Client
stdio_client = Client(stdio_transport)


async def client_call_tool():
    async with stdio_client:
        tools = await stdio_client.list_tools()
        print("Done")
        print(len(tools))
        print(tools[0].name)

asyncio.run(client_call_tool())
