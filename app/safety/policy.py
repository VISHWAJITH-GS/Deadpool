class SafetyController:
    SAFE = "SAFE"
    CONFIRM = "CONFIRM"
    DANGEROUS = "DANGEROUS"

    def __init__(self):
        pass

    def get_risk_level(self, tool_name: str, args: dict = None) -> str:
        args = args or {}
        
        # Inherently Safe
        if tool_name in ["calculator", "get_time", "system_info", "file_search", "file_read", "web_search", "get_active_window_title", "get_active_window", "focus_application", "launch_application", "open_url"]:
            return self.SAFE
            
        if tool_name == "type_text":
            app = args.get("app", "").lower()
            text = args.get("text", "").lower()
            
            # Typing in terminals or browsers might be riskier than a simple text editor
            safe_editors = ["notepad", "code", "vscode", "word", "document", "editor", "paint"]
            if any(editor in app for editor in safe_editors):
                return self.SAFE
                
            if "terminal" in app or "cmd" in app or "powershell" in app or "bash" in app:
                if any(dangerous_cmd in text for dangerous_cmd in ["del", "rm", "format", "format c:", "drop", "shutdown"]):
                    return self.DANGEROUS
                return self.CONFIRM
                
            return self.CONFIRM

        if tool_name in ["press_hotkey", "mouse_click"]:
            return self.CONFIRM

        return self.CONFIRM

safety_controller = SafetyController()
