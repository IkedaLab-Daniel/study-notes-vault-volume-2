
from fastmcp import FastMCP

mcp = FastMCP(
    name="CalculatorMCPServer",  # Fixed: added missing comma
    instructions="""
        This server provides data analysis tools.
        Call add() to add two numbers.
    """
)

@mcp.tool
def add(a: int, b: int) -> int:
    """Adds two integer numbers together."""
    return a + b

@mcp.tool
def subtract(a:int, b:int) -> int:
    """Subtracts b from a"""
    return a - b

@mcp.resource("file://documents/{name}")
def read_document(name: str) -> str:
    """Read a document by name"""
    return "Document contents of {name"

@mcp.prompt(title="Code Review")
def review_code(code: str) -> str:
    return f"Please review this code: {code}"

if __name__ == "__main__":
    mcp.run()
