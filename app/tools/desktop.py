from app.tools.registry import tool_registry
from app.tools.registry_db import app_web_registry
import webbrowser
import os
import subprocess
import time
import ctypes

try:
    import pyautogui
    HAS_PYAUTOGUI = True
except ImportError:
    HAS_PYAUTOGUI = False

@tool_registry.register(
    name="get_active_window",
    description="Gets detailed information about the currently active window, including the application executable name and window title.",
    schema={
        "type": "object",
        "properties": {},
        "required": []
    }
)
def get_active_window() -> str:
    """Uses ctypes to get the active window details."""
    import win32process
    try:
        hwnd = ctypes.windll.user32.GetForegroundWindow()
        if not hwnd:
            return json.dumps({"error": "No active window found."})
            
        length = ctypes.windll.user32.GetWindowTextLengthW(hwnd)
        buf = ctypes.create_unicode_buffer(length + 1)
        ctypes.windll.user32.GetWindowTextW(hwnd, buf, length + 1)
        title = buf.value
        
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        
        # Try to get process name
        process_name = "unknown"
        try:
            import psutil
            process_name = psutil.Process(pid).name()
        except:
            pass
            
        return json.dumps({
            "application": process_name,
            "title": title,
            "focused": True
        })
    except Exception as e:
        return json.dumps({"error": f"Failed to get active window: {e}"})

@tool_registry.register(
    name="open_url",
    description="Opens a website. Pass the raw URL or a known alias (e.g., 'leetcode').",
    schema={
        "type": "object",
        "properties": {
            "url": {
                "type": "string",
                "description": "The URL or known website alias."
            }
        },
        "required": ["url"]
    }
)
def open_url(url: str) -> str:
    """Opens a URL, checking the registry first."""
    # Check registry for alias
    resolved_url = app_web_registry.find_website(url)
    final_url = resolved_url if resolved_url else url
    
    if not final_url.startswith("http"):
        final_url = "https://" + final_url

    try:
        webbrowser.open(final_url)
        return f"Successfully opened URL: {final_url}"
    except Exception as e:
        return f"Failed to open URL: {str(e)}"

import shutil
import glob
import difflib

SPECIAL_APPS = {
    "settings": "ms-settings:",
    "setting": "ms-settings:",
}

def find_start_menu_shortcut(app_name: str) -> str:
    search_dirs = [
        os.path.expandvars(r"%APPDATA%\Microsoft\Windows\Start Menu\Programs"),
        os.path.expandvars(r"%PROGRAMDATA%\Microsoft\Windows\Start Menu\Programs")
    ]
    
    shortcuts = {}
    for d in search_dirs:
        for filepath in glob.glob(os.path.join(d, "**", "*.lnk"), recursive=True):
            name = os.path.splitext(os.path.basename(filepath))[0]
            shortcuts[name] = filepath
            
    if not shortcuts:
        return None
        
    # First check exact substring (case-insensitive)
    app_lower = app_name.lower().replace(" ", "")
    for name, path in shortcuts.items():
        if app_lower in name.lower().replace(" ", ""):
            return path
            
    # Then fuzzy matching
    matches = difflib.get_close_matches(app_name.lower(), [n.lower() for n in shortcuts.keys()], n=1, cutoff=0.5)
    if matches:
        match_lower = matches[0]
        # find original case
        for name, path in shortcuts.items():
            if name.lower() == match_lower:
                return path
                
    return None

@tool_registry.register(
    name="launch_application",
    description="Launches an application by name or alias.",
    schema={
        "type": "object",
        "properties": {
            "app_name": {
                "type": "string",
                "description": "The name or alias of the app to launch."
            }
        },
        "required": ["app_name"]
    }
)
def launch_application(app_name: str) -> str:
    """Launches an application, checking the registry first, then fuzzy searching."""
    app_lower = app_name.lower().replace(" ", "")
    if app_lower in SPECIAL_APPS:
        executable = SPECIAL_APPS[app_lower]
        try:
            os.startfile(executable)
            return f"Successfully launched {app_name} ({executable})."
        except Exception as e:
            return f"Failed to open special app '{app_name}': {e}"
            
    resolved_exe = app_web_registry.find_app(app_name)
    executable = resolved_exe if resolved_exe else app_name
    
    try:
        os.startfile(executable)
        return f"Successfully launched {app_name} ({executable})."
    except FileNotFoundError:
        # Check if it's in PATH before trying Popen
        if shutil.which(executable) is not None:
            try:
                subprocess.Popen([executable])
                return f"Successfully launched {app_name} via subprocess."
            except Exception as e:
                return f"Failed to launch application '{app_name}': {str(e)}"
                
        # Fallback to Start Menu fuzzy search
        shortcut = find_start_menu_shortcut(app_name)
        if shortcut:
            try:
                os.startfile(shortcut)
                return f"Successfully launched {app_name} via Start Menu shortcut ({os.path.basename(shortcut)})."
            except Exception as e:
                return f"Failed to launch shortcut '{shortcut}': {str(e)}"
                
        return f"Error: Application '{app_name}' not found in registry, PATH, or Start Menu."
    except Exception as e:
        return f"Failed to launch application '{app_name}': {str(e)}"

@tool_registry.register(
    name="focus_application",
    description="Brings an application's window to the foreground by name.",
    schema={
        "type": "object",
        "properties": {
            "app_name": {
                "type": "string",
                "description": "The name of the app to focus."
            }
        },
        "required": ["app_name"]
    }
)
def focus_application(app_name: str) -> str:
    hwnd = find_window_by_title(app_name)
    if not hwnd:
        return f"Error: No visible window found containing '{app_name}' in title."
    
    if HAS_PYAUTOGUI:
        pyautogui.press('alt') # Windows focus trick
    ctypes.windll.user32.ShowWindow(hwnd, 9) # Restore if minimized
    time.sleep(0.1)
    ctypes.windll.user32.SetForegroundWindow(hwnd)
    time.sleep(0.2)
    return f"Successfully focused {app_name}."

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
    name="press_hotkey",
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
def press_hotkey(keys: list) -> str:
    if not HAS_PYAUTOGUI:
        return "Error: pyautogui is not installed. Keyboard actions are unavailable."
    try:
        pyautogui.hotkey(*keys)
        return f"Successfully pressed hotkey: {'+'.join(keys)}"
    except Exception as e:
        return f"Failed to press hotkey: {e}"

def find_window_by_title(target_title: str) -> int:
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
        # Prioritize exact matches
        for h, t in hwnds:
            if target_title.lower() == t.lower():
                return h
        return hwnds[0][0]
    return 0

@tool_registry.register(
    name="manage_window",
    description="Manages window states (minimize, maximize, close, split screen) for a specific app or all windows.",
    schema={
        "type": "object",
        "properties": {
            "action": {
                "type": "string",
                "enum": ["minimize", "maximize", "close", "minimize_all", "split_left", "split_right"],
                "description": "The action to perform on the window."
            },
            "app_name": {
                "type": "string",
                "description": "Optional name of the app to target. If empty and action requires it, targets active window."
            }
        },
        "required": ["action"]
    }
)
def manage_window(action: str, app_name: str = "") -> str:
    if action == "minimize_all":
        if not HAS_PYAUTOGUI:
            return "Error: pyautogui is required for minimize_all."
        pyautogui.hotkey('win', 'd')
        return "Minimized all windows (Show Desktop toggle applied)."

    hwnd = 0
    if app_name:
        hwnd = find_window_by_title(app_name)
        if not hwnd:
            return f"Error: No visible window found containing '{app_name}' in title."
    else:
        hwnd = ctypes.windll.user32.GetForegroundWindow()
        if not hwnd:
            return "Error: No active window found to manage."

    if action in ["split_left", "split_right"]:
        if not HAS_PYAUTOGUI:
            return "Error: pyautogui is required for split screen actions."
        # Focus window first
        ctypes.windll.user32.ShowWindow(hwnd, 9) # Restore if minimized
        time.sleep(0.1)
        ctypes.windll.user32.SetForegroundWindow(hwnd)
        time.sleep(0.2)
        direction = 'left' if action == 'split_left' else 'right'
        pyautogui.hotkey('win', direction)
        return f"Split window to the {direction}."

    if action == "maximize":
        ctypes.windll.user32.ShowWindow(hwnd, 3) # SW_MAXIMIZE
        return f"Maximized window."
    elif action == "minimize":
        ctypes.windll.user32.ShowWindow(hwnd, 6) # SW_MINIMIZE
        return f"Minimized window."
    elif action == "close":
        ctypes.windll.user32.PostMessageW(hwnd, 0x0010, 0, 0) # WM_CLOSE
        return f"Closed window."
        
    return f"Error: Unknown action '{action}'."
