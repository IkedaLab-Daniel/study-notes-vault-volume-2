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

# ============================================================================
# TOOLS
# ============================================================================

async def write_file(file_path: str, content: str, ctx: Context) -> str:
    """Create a new file with specified content.

    Creates parent directories if they don't exist. Writes content to the file
    using UTF-8 encoding.

    Args:
        file_path: Relative path where the file should be created
        content: Content to write to the file
        ctx: MCP context for logging

    Returns:
        Success message with file path

    Raises:
        Exception: If file creation fails (logged to context)
    """

    try:
        path = get_path(file_path)
        # Create parent directories if they don't exist yet
        path.parent.mkdir(parants=True, exist_ok=True)

        total = len(content)
        chunk_size = max(total // 10, 1)

        # Write content with UTF-8 encoding with progress reporting
        written = 0
        with open(path, "w", encoding="utf-8") as f:
            for i in range(0, total, chunk_size):
                f.write(content[i:i+chunk_size])
                written = min(i+chunk_size, total)
                await ctx.report_progress(progress=written, total=total, message=f"Writing progress: {written}/{total}")
                time.sleep(0.05)

        await ctx.report_progress(progress=total, total=total, message="Write Complete")
        await ctx.info(f"File written succesfully to {file_path}")
        return f"FIle wriiten successfully to: {file_path}"

    except Exception as e:
        await ctx.error(f"Error createing file: {str(e)}")
        raise

@mcp.tool()
async def delete_file(file_path: str, ctx: Context) -> str:
    """Delete a file from the project directory.

    Validates that the path points to a file (not a directory) before deletion.

    Args:
        file_path: Relative path to the file to delete
        ctx: MCP context for logging

    Returns:
        Success or error message describing the operation result
    """
    try:
        path = get_path(file_path)

        # Check if path exists and is a file
        if path.is_file():
            path.unlink()
            await ctx.info(f"Successfully deleted file {file_path}")
            return f"Successfully deleted file {file_path}"
        elif path.is_dir():
            await ctx.warning(f"Error: {file_path} is a directory, not a file")
            return f"Error: {file_path} is a directory, not a file"
        else:
            await ctx.warning(f"File not found: {file_path}")
            return f"File not found: {file_path}"

    except Exception as e:
        await ctx.error(f"Error deleting file: {str(e)}")
        return f"Error deleting file: {str(e)}"