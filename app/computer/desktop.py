from app.applications.registry import tool_registry
from app.applications.resolver import app_web_registry
import os
import subprocess
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
