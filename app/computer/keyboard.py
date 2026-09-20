from app.applications.registry import tool_registry

try:
    import pyautogui
    HAS_PYAUTOGUI = True
except ImportError:
    HAS_PYAUTOGUI = False

@tool_registry.register(
    name="type_text",
    description="Types text into the currently active window.",
    schema={
        "type": "object",
        "properties": {
            "text": {
                "type": "string",
                "description": "The exact text to type"
            }
        },
        "required": ["text"]
    }
)
def type_text(text: str) -> str:
    if not HAS_PYAUTOGUI:
        return "Error: pyautogui is not installed. Keyboard actions are unavailable."
    try:
        pyautogui.write(text, interval=0.05)
        return f"Successfully typed text: {text}"
    except Exception as e:
        return f"Failed to type text: {e}"

@tool_registry.register(
    name="hotkey",
    description="Presses a combination of keys (e.g., ['ctrl', 'c']) in the currently active window.",
    schema={
        "type": "object",
        "properties": {
            "keys": {
                "type": "array",
                "items": {"type": "string"},
                "description": "List of keys to press together"
            }
        },
        "required": ["keys"]
    }
)
def hotkey(keys: list) -> str:
    if not HAS_PYAUTOGUI:
        return "Error: pyautogui is not installed."
    try:
        pyautogui.hotkey(*keys)
        return f"Successfully pressed hotkey: {'+'.join(keys)}"
    except Exception as e:
        return f"Failed to press hotkey: {e}"

@tool_registry.register(
    name="press_key",
    description="Presses a single key (e.g., 'enter', 'tab', 'esc').",
    schema={
        "type": "object",
        "properties": {
            "key": {
                "type": "string",
                "description": "The key to press"
            }
        },
        "required": ["key"]
    }
)
def press_key(key: str) -> str:
    if not HAS_PYAUTOGUI:
        return "Error: pyautogui is not installed."
    try:
        pyautogui.press(key)
        return f"Successfully pressed key: {key}"
    except Exception as e:
        return f"Failed to press key: {e}"
