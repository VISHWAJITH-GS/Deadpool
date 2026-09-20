from app.tools.registry import tool_registry
from datetime import datetime

@tool_registry.register(
    name="get_time",
    description="Gets the current date and time.",
    schema={
        "type": "object",
        "properties": {},
        "required": []
    }
)
def get_time() -> str:
    """Returns current date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
