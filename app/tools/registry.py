from typing import Callable, Dict, Any, List
import inspect

class ToolRegistry:
    def __init__(self):
        self._tools: Dict[str, Callable] = {}
        self._schemas: List[Dict[str, Any]] = []

    def register(self, name: str, description: str, schema: Dict[str, Any]):
        def decorator(func: Callable):
            self._tools[name] = func
            self._schemas.append({
                "name": name,
                "description": description,
                "parameters": schema
            })
            return func
        return decorator

    def get_schemas(self) -> List[Dict[str, Any]]:
        return self._schemas

    def execute(self, name: str, kwargs: Dict[str, Any]) -> str:
        if name not in self._tools:
            return f"Error: Tool '{name}' not found."
        try:
            return str(self._tools[name](**kwargs))
        except Exception as e:
            return f"Error executing '{name}': {str(e)}"

tool_registry = ToolRegistry()
