import os
import glob
import json
import difflib
import win32com.client
from typing import Optional, Dict, Any, List

class AppDiscovery:
    def __init__(self, cache_file: str = "data/applications.json"):
        self.cache_file = os.path.abspath(cache_file)
        self.registry = {}
        
        # Ensure data dir exists
        os.makedirs(os.path.dirname(self.cache_file), exist_ok=True)
        
        if os.path.exists(self.cache_file):
            self.load_cache()
        else:
            self.scan_applications()

    def load_cache(self):
        try:
            with open(self.cache_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.registry = {app['id']: app for app in data.get("applications", [])}
        except Exception as e:
            print(f"Failed to load application cache: {e}")
            self.registry = {}

    def save_cache(self):
        data = {
            "version": 1,
            "applications": list(self.registry.values())
        }
        try:
            with open(self.cache_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Failed to save application cache: {e}")

    def scan_applications(self):
        print("Scanning installed applications...")
        search_dirs = [
            os.path.expandvars(r"%APPDATA%\Microsoft\Windows\Start Menu\Programs"),
            os.path.expandvars(r"%PROGRAMDATA%\Microsoft\Windows\Start Menu\Programs")
        ]
        
        try:
            shell = win32com.client.Dispatch("WScript.Shell")
        except Exception as e:
            print(f"Warning: Could not init WScript.Shell ({e}). Paths will not be extracted from .lnk.")
            shell = None
        
        new_registry = {}
        for d in search_dirs:
            for filepath in glob.glob(os.path.join(d, "**", "*.lnk"), recursive=True):
                target = filepath
                if shell:
                    try:
                        shortcut = shell.CreateShortCut(filepath)
                        target = shortcut.Targetpath
                        if not target:
                            target = filepath
                    except:
                        pass

                name = os.path.splitext(os.path.basename(filepath))[0]
                
                # Normalize ID
                app_id = name.lower().replace(" ", "")
                
                if app_id not in new_registry:
                    new_registry[app_id] = {
                        "id": app_id,
                        "name": name,
                        "executable": target,
                        "aliases": [name.lower(), app_id]
                    }
        
        # Add some hardcoded safe defaults
        defaults = {
            "notepad": {"id": "notepad", "name": "Notepad", "executable": "notepad.exe", "aliases": ["notepad"]},
            "calc": {"id": "calc", "name": "Calculator", "executable": "calc.exe", "aliases": ["calculator", "calc"]},
            "explorer": {"id": "explorer", "name": "File Explorer", "executable": "explorer.exe", "aliases": ["explorer", "file explorer"]},
            "settings": {"id": "settings", "name": "Settings", "executable": "ms-settings:", "aliases": ["settings", "setting"]},
        }
        for k, v in defaults.items():
            if k not in new_registry:
                new_registry[k] = v

        self.registry = new_registry
        self.save_cache()
        print(f"Application registry updated. Found {len(self.registry)} applications.")

    def resolve_app(self, query: str) -> Optional[Dict[str, Any]]:
        query_lower = query.lower().strip()
        query_normalized = query_lower.replace(" ", "")

        # 1. & 2. Exact alias or Normalized
        for app_id, app_data in self.registry.items():
            if query_lower in app_data["aliases"] or query_normalized == app_id:
                return app_data

        # 3. Fuzzy Matching
        all_aliases = []
        alias_to_app = {}
        for app_id, app_data in self.registry.items():
            for alias in app_data["aliases"]:
                all_aliases.append(alias)
                alias_to_app[alias] = app_data
                
        matches = difflib.get_close_matches(query_lower, all_aliases, n=3, cutoff=0.6)
        
        if not matches:
            return None
            
        if len(matches) == 1:
            return alias_to_app[matches[0]]
            
        if matches[0] == query_lower:
            return alias_to_app[matches[0]]

        unique_matches = []
        seen_ids = set()
        for m in matches:
            app = alias_to_app[m]
            if app["id"] not in seen_ids:
                unique_matches.append(app)
                seen_ids.add(app["id"])
                
        if len(unique_matches) == 1:
            return unique_matches[0]
            
        return {"ambiguous": True, "matches": unique_matches}

app_discovery = AppDiscovery()
