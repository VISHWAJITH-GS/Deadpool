from app.applications.registry import tool_registry
import platform
import os

@tool_registry.register(
    name="system_info",
    description="Gets basic system information.",
    schema={
        "type": "object",
        "properties": {},
        "required": []
    }
)
def system_info() -> str:
    """Returns basic OS and hardware info."""
    uname = platform.uname()
    return f"System: {uname.system} {uname.release}, CPU: {uname.processor}, Cores: {os.cpu_count()}"
