from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport, StdioTransport

stdio_transport = StdioTransport(
    command="npx",
    args=["-y", "@upstash/cpmtext7-mcp"]
)

print(stdio_transport)

# ? Client
stdio_client = Client(stdio_transport)


async def client_call_tool():
    # list of tools the server provides
    tools = await stdio_client.list_tools()
    print("Done")
    len(tools)
    print(tools[0].name)

client_call_tool()