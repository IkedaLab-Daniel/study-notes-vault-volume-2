import os
import time
import socket
import asyncio
from dotenv import load_dotenv
from fastmcp import FastMCP, Client

from langchain_core.tools import tool
from fastmcp import FastMCP

def make_dir():
    if os.path.exists("path"):
        print("PAth directory already exists")
    else:
        print("✗ Path directory doesn't exist - creating it...")
        os.makedirs("path")
        print("✓ Path directory created")

PORT = 8000

def test_port(port=PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(('127.0.0.1', port))
            return True
        except socket.error:
            return False

print(f"Port {PORT} is available: {test_port()}")

def print_stream_info(read, write, _sid, verbose=False):
    """Print information about the read/write streams and session ID"""

    if verbose:
        print("READ (receives FROM server):")
        print(read)
        print()
        
        print("WRITE (sends TO server):")
        print(write)
        print()
        
        print("SESSION ID:")
        print(_sid())

@tool
def multiply(a: int, b: int) -> int:
    """Multiple two numbers"""
    return a * b

# print(multiply.name)
# print(multiply.description)
# print(multiply.args)

# print("What is 2 x 3?")
# print("Answer: " + str(multiply.invoke({"a": 2, "b": 3})))


mcp = FastMCP(
    name="CalculatorMCPServer",
    instructions="""
This server provides data analysis tools.
Call get_average() to analyze numberical data.
"""
)

# print("mcp object", mcp)

@mcp.tool
def add(a: int, b: int) -> int:
    """
    Add two integers together.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of `a` and `b`.

    Example:
        >>> add(3, 5)
        8
    """
    return a + b


@mcp.tool
def subtract(a: int, b: int) -> int:
    """
    Subtract one integer from another.

    Args:
        a (int): The number to subtract from.
        b (int): The number to subtract.

    Returns:
        int: The result of `a - b`.

    Example:
        >>> subtract(10, 4)
        6
    """
    return a - b

@mcp.resource("file:///endpoint/{name}")
def return_template_document(name: str) -> str:
    """Read a document by name"""
    return f"Docuemnt contents of {name}"

make_dir()

@mcp.resource("file://endpoint2/{name}")
def read_document(name: str) -> str:
    """Read a document by name from the path directory"""
    try:
        # Read from the actual file system path
        with open(f"path/{name}", "r") as f:
            return f.read()
    except FileNotFoundError:
        return f"Document '{name}' not found in path directory"
    except Exception as e:
        return f"Error reading document: {str(e)}"

@mcp.prompt(title="Code Review")
def review_code(code: str) -> str:
    return f"Please review this code:\n\n{code}"

## -- Creating a Clinet - In-memory Transport ———————————
print("—————————— Creating a Clinet - In-memory Transport ——————————")

client = Client(mcp)
print(f"client: {client}")

async def call_add_tool(a: int, b: int):
    async with client:
        result = await client.call_tool("add", {"a": a, "b": b})
        return result

response = call_add_tool(4,5)
print(response)
