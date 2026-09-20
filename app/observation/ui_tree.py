import json
import time
from app.tools.registry import tool_registry

# Global cache for UI elements to map IDs back to actual automation objects
_ui_element_cache = {}

@tool_registry.register(
    name="get_ui_tree",
    description="Gets a semantic representation of the active window's UI elements (buttons, inputs, etc.)",
    schema={
        "type": "object",
        "properties": {},
        "required": []
    }
)
def get_ui_tree() -> str:
    """Scans the active window using uiautomation and returns a semantic JSON tree."""
    try:
        import uiautomation as auto
    except ImportError:
        return json.dumps({"error": "uiautomation library is not installed. UI observation is unavailable."})

    global _ui_element_cache
    _ui_element_cache.clear()

    try:
        window = auto.GetForegroundControl()
        if not window:
            return json.dumps({"error": "No active window found."})

        # We only want to compress the UI tree to semantic elements to save tokens
        semantic_roles = [
            auto.ControlType.ButtonControl,
            auto.ControlType.EditControl,
            auto.ControlType.DocumentControl,
            auto.ControlType.ListItemControl,
            auto.ControlType.MenuItemControl,
            auto.ControlType.TabItemControl,
            auto.ControlType.CheckBoxControl,
            auto.ControlType.HyperlinkControl
        ]

        elements = []
        element_id = 0

        # Walk the tree for the active window, up to a certain depth to prevent hanging
        for control, depth in auto.WalkControl(window, maxDepth=4):
            if control.ControlType in semantic_roles and control.Name:
                eid = f"e{element_id}"
                _ui_element_cache[eid] = control
                
                role_name = control.ControlTypeName.replace("Control", "").lower()
                elements.append({
                    "id": eid,
                    "role": role_name,
                    "name": control.Name,
                    "enabled": control.IsEnabled
                })
                element_id += 1
                
                # Limit to 50 elements to avoid context bloat
                if element_id >= 50:
                    break

        return json.dumps({
            "window": {
                "application": window.Name
            },
            "elements": elements
        }, indent=2)

    except Exception as e:
        return json.dumps({"error": f"Failed to get UI tree: {str(e)}"})


@tool_registry.register(
    name="click_element",
    description="Clicks a UI element by its ID (obtained from get_ui_tree).",
    schema={
        "type": "object",
        "properties": {
            "element_id": {
                "type": "string",
                "description": "The ID of the element to click (e.g., 'e1')."
            }
        },
        "required": ["element_id"]
    }
)
def click_element(element_id: str) -> str:
    global _ui_element_cache
    
    if element_id not in _ui_element_cache:
        return json.dumps({"error": f"Element {element_id} not found in current UI cache. Call get_ui_tree() first."})
        
    try:
        control = _ui_element_cache[element_id]
        control.Click(simulateMove=False)
        time.sleep(0.5)
        return json.dumps({"status": "Success", "message": f"Clicked '{control.Name}'."})
    except Exception as e:
        return json.dumps({"error": f"Failed to click element: {str(e)}"})
