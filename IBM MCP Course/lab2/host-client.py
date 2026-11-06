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