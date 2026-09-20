from app.tools.registry import tool_registry
import os

@tool_registry.register(
    name="file_search",
    description="Searches for a file by name in the current directory.",
    schema={
        "type": "object",
        "properties": {
            "filename": {
                "type": "string",
                "description": "The name of the file to search for"
            }
        },
        "required": ["filename"]
    }
)
def file_search(filename: str) -> str:
    """Basic file search."""
    results = []
    for root, dirs, files in os.walk("."):
        if filename in files:
            results.append(os.path.join(root, filename))
    return f"Found files: {results}" if results else "File not found."

@tool_registry.register(
    name="file_read",
    description="Reads the contents of a text file.",
    schema={
        "type": "object",
        "properties": {
            "path": {
                "type": "string",
                "description": "The path to the file"
            }
        },
        "required": ["path"]
    }
)
def file_read(path: str) -> str:
    """Basic file reader."""
    if not os.path.exists(path):
        return "Error: File not found."
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read(2000) # Read up to 2000 chars for safety
            if len(content) == 2000:
                content += "... [TRUNCATED]"
            return content
    except Exception as e:
        return f"Error reading file: {e}"
