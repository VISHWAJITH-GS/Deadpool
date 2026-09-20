from app.applications.registry import tool_registry
import ctypes
import json
import time

try:
    import pyautogui
    HAS_PYAUTOGUI = True
except ImportError:
    HAS_PYAUTOGUI = False

def _find_window_by_title(target_title: str) -> int:
    hwnds = []
    def callback(hwnd, extra):
        if ctypes.windll.user32.IsWindowVisible(hwnd):
            length = ctypes.windll.user32.GetWindowTextLengthW(hwnd)
            if length > 0:
                buf = ctypes.create_unicode_buffer(length + 1)
                ctypes.windll.user32.GetWindowTextW(hwnd, buf, length + 1)
                title = buf.value
                if target_title.lower() in title.lower():
                    # Ignore IDE windows to prevent accidental focus
                    if "antigravity ide" not in title.lower() and "visual studio code" not in title.lower():
                        hwnds.append((hwnd, title))
        return True
    
    WNDENUMPROC = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_int, ctypes.c_int)
    ctypes.windll.user32.EnumWindows(WNDENUMPROC(callback), 0)
    
    if hwnds:
        for h, t in hwnds:
            if target_title.lower() == t.lower():
                return h
        return hwnds[0][0]
    return 0

@tool_registry.register(
    name="get_active_window",
    description="Gets information about the currently active window.",
    schema={"type": "object", "properties": {}}
)
def get_active_window() -> str:
    import win32process
    try:
        hwnd = ctypes.windll.user32.GetForegroundWindow()
        if not hwnd: return json.dumps({"error": "No active window found."})
            
        length = ctypes.windll.user32.GetWindowTextLengthW(hwnd)
        buf = ctypes.create_unicode_buffer(length + 1)
        ctypes.windll.user32.GetWindowTextW(hwnd, buf, length + 1)
        title = buf.value
        
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        process_name = "unknown"
        try:
            import psutil
            process_name = psutil.Process(pid).name()
        except:
            pass
            
        return json.dumps({"application": process_name, "title": title, "focused": True})
    except Exception as e:
        return json.dumps({"error": f"Failed to get active window: {e}"})

@tool_registry.register(
    name="get_windows",
    description="Lists all visible windows and their titles.",
    schema={"type": "object", "properties": {}}
)
def get_windows() -> str:
    windows = []
    def callback(hwnd, extra):
        if ctypes.windll.user32.IsWindowVisible(hwnd):
            length = ctypes.windll.user32.GetWindowTextLengthW(hwnd)
            if length > 0:
                buf = ctypes.create_unicode_buffer(length + 1)
                ctypes.windll.user32.GetWindowTextW(hwnd, buf, length + 1)
                title = buf.value
                if title:
                    windows.append(title)
        return True
    
    WNDENUMPROC = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_int, ctypes.c_int)
    ctypes.windll.user32.EnumWindows(WNDENUMPROC(callback), 0)
    return json.dumps({"windows": windows})

@tool_registry.register(
    name="focus_window",
    description="Brings a window to the foreground by its title.",
    schema={
        "type": "object",
        "properties": {"title": {"type": "string"}},
        "required": ["title"]
    }
)
def focus_window(title: str) -> str:
    hwnd = _find_window_by_title(title)
    if not hwnd:
        return f"Error: No visible window found containing '{title}'."
    
    if HAS_PYAUTOGUI: pyautogui.press('alt')
    ctypes.windll.user32.ShowWindow(hwnd, 9)
    time.sleep(0.1)
    ctypes.windll.user32.SetForegroundWindow(hwnd)
    time.sleep(0.2)
    return f"Successfully focused window '{title}'."

@tool_registry.register(
    name="maximize_window",
    description="Maximizes a specific window by title or the currently active window.",
    schema={
        "type": "object",
        "properties": {"title": {"type": "string", "default": ""}}
    }
)
def maximize_window(title: str = "") -> str:
    hwnd = _find_window_by_title(title) if title else ctypes.windll.user32.GetForegroundWindow()
    if not hwnd: return "Error: Window not found."
    ctypes.windll.user32.ShowWindow(hwnd, 3)
    return "Maximized window."

@tool_registry.register(
    name="minimize_window",
    description="Minimizes a specific window by title or the currently active window.",
    schema={
        "type": "object",
        "properties": {"title": {"type": "string", "default": ""}}
    }
)
def minimize_window(title: str = "") -> str:
    hwnd = _find_window_by_title(title) if title else ctypes.windll.user32.GetForegroundWindow()
    if not hwnd: return "Error: Window not found."
    ctypes.windll.user32.ShowWindow(hwnd, 6)
    return "Minimized window."

@tool_registry.register(
    name="close_window",
    description="Closes a specific window by title or the currently active window.",
    schema={
        "type": "object",
        "properties": {"title": {"type": "string", "default": ""}}
    }
)
def close_window(title: str = "") -> str:
    hwnd = _find_window_by_title(title) if title else ctypes.windll.user32.GetForegroundWindow()
    if not hwnd: return "Error: Window not found."
    ctypes.windll.user32.PostMessageW(hwnd, 0x0010, 0, 0)
    return "Closed window."
