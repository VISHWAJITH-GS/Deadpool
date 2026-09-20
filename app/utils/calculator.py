from app.applications.registry import tool_registry

@tool_registry.register(
    name="calculator",
    description="Evaluates a mathematical expression.",
    schema={
        "type": "object",
        "properties": {
            "expression": {
                "type": "string",
                "description": "The mathematical expression to evaluate (e.g., '2 + 2 * 4')"
            }
        },
        "required": ["expression"]
    }
)
def calculator(expression: str) -> str:
    """Safe evaluation of basic math."""
    allowed_chars = set("0123456789+-*/(). ")
    if not all(c in allowed_chars for c in expression):
        return "Error: Invalid characters in expression."
    try:
        # Using eval with no builtins for basic safety
        result = eval(expression, {"__builtins__": None}, {})
        return str(result)
    except Exception as e:
        return f"Error: {e}"
