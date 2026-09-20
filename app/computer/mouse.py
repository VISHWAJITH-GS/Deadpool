from app.applications.registry import tool_registry

try:
    import pyautogui
    HAS_PYAUTOGUI = True
except ImportError:
    HAS_PYAUTOGUI = False

@tool_registry.register(
    name="move_mouse",
    description="Moves the mouse cursor to absolute screen coordinates (x, y).",
    schema={
        "type": "object",
        "properties": {
            "x": {"type": "integer"},
            "y": {"type": "integer"}
        },
        "required": ["x", "y"]
    }
)
def move_mouse(x: int, y: int) -> str:
    if not HAS_PYAUTOGUI: return "Error: pyautogui not installed."
    try:
        pyautogui.moveTo(x, y, duration=0.2)
        return f"Moved mouse to ({x}, {y})."
    except Exception as e:
        return f"Failed to move mouse: {e}"

@tool_registry.register(
    name="click",
    description="Clicks the mouse at the current position.",
    schema={
        "type": "object",
        "properties": {
            "button": {"type": "string", "enum": ["left", "right", "middle"], "default": "left"},
            "clicks": {"type": "integer", "default": 1}
        }
    }
)
def click(button: str = 'left', clicks: int = 1) -> str:
    if not HAS_PYAUTOGUI: return "Error: pyautogui not installed."
    try:
        pyautogui.click(button=button, clicks=clicks)
        return f"Clicked {button} button {clicks} times."
    except Exception as e:
        return f"Failed to click: {e}"

@tool_registry.register(
    name="double_click",
    description="Double-clicks the left mouse button at the current position.",
    schema={"type": "object", "properties": {}}
)
def double_click() -> str:
    if not HAS_PYAUTOGUI: return "Error: pyautogui not installed."
    try:
        pyautogui.doubleClick()
        return "Double-clicked."
    except Exception as e:
        return f"Failed to double-click: {e}"

@tool_registry.register(
    name="right_click",
    description="Right-clicks at the current mouse position.",
    schema={"type": "object", "properties": {}}
)
def right_click() -> str:
    if not HAS_PYAUTOGUI: return "Error: pyautogui not installed."
    try:
        pyautogui.rightClick()
        return "Right-clicked."
    except Exception as e:
        return f"Failed to right-click: {e}"

@tool_registry.register(
    name="drag",
    description="Drags the mouse to absolute coordinates (x, y) holding the left button.",
    schema={
        "type": "object",
        "properties": {
            "x": {"type": "integer"},
            "y": {"type": "integer"}
        },
        "required": ["x", "y"]
    }
)
def drag(x: int, y: int) -> str:
    if not HAS_PYAUTOGUI: return "Error: pyautogui not installed."
    try:
        pyautogui.dragTo(x, y, duration=0.5, button='left')
        return f"Dragged mouse to ({x}, {y})."
    except Exception as e:
        return f"Failed to drag mouse: {e}"

@tool_registry.register(
    name="scroll",
    description="Scrolls the mouse wheel up (positive) or down (negative).",
    schema={
        "type": "object",
        "properties": {
            "clicks": {"type": "integer", "description": "Amount to scroll. Positive for up, negative for down."}
        },
        "required": ["clicks"]
    }
)
def scroll(clicks: int) -> str:
    if not HAS_PYAUTOGUI: return "Error: pyautogui not installed."
    try:
        pyautogui.scroll(clicks)
        return f"Scrolled {clicks} units."
    except Exception as e:
        return f"Failed to scroll: {e}"
