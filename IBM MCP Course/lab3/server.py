from pathlib import Path
from datetime import datetime
from pydantic import BaseModel
import time

from fastmcp import FastMCP, Context

BASE_DIR = Path.cwd()

class DocumentGeneratorSchema(BaseModel):
    """Pydantic model for documentation filename schema.

    Used in elicitation to capture user input for documentation file names.

    Attributes:
        file_path: Path of the file we want to generate document on
        name: The name of the documentation file to create
    """
    file_path: str
    name: str

mcp = FastMCP("File Operations MCP Server")
print(mcp)

# ============================================================================
# Helper Functions
# ============================================================================

def get_path(relative_path: str) -> Path:
    """Convert relative path to absolute path within project directory.

    Ensures the path is within BASE_DIR for security. Resolves the path
    and validates it's relative to the base directory.

    Args:
        relative_path: Relative path string to convert

    Returns:
        Absolute Path object within BASE_DIR

    Raises:
        ValueError: If path is outside BASE_DIR    
    """

    rel = Path(relative_path).resolve().relative_to(BASE_DIR)
    return rel

