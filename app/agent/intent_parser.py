import re
from typing import Optional, Dict, Any, List

class IntentParser:
    def __init__(self):
        # Matches: "open <app> and type <text>", "open <app> then type <text>", "open <app>, then type <text>"
        self.type_patterns = [
            re.compile(r"^(?:open|launch|start)\s+(.+?)\s+(?:and|then)\s+(?:type|write)\s+(.+)$", re.IGNORECASE),
            re.compile(r"^(?:open|launch|start)\s+(.+?),\s*(?:then\s+)?(?:type|write)\s+(.+)$", re.IGNORECASE)
        ]
        
        # Matches: "type <text> in <app>", "write <text> into <app>"
        self.type_in_patterns = [
            re.compile(r"^(?:type|write)\s+(.+?)\s+(?:in|into)\s+(.+)$", re.IGNORECASE)
        ]
        
        # Matches: "type <text>", "write <text>"
        self.type_only_patterns = [
            re.compile(r"^(?:type|write)\s+(.+)$", re.IGNORECASE)
        ]
        
        # Matches: "open <app> and go to <url>", "open <app> then go to <url>"
        self.url_patterns = [
            re.compile(r"^(?:open|launch|start)\s+(.+?)\s+(?:and|then)\s+(?:go to|navigate to)\s+(.+)$", re.IGNORECASE)
        ]
        
        # Matches: "open <app>, go to <url> and search for <query>"
        self.url_search_patterns = [
            re.compile(r"^(?:open|launch|start)\s+(.+?)(?:,|\s+(?:and|then))\s+(?:go to|navigate to)\s+(.+?)\s+(?:and|then)\s+search\s+(?:for\s+)?(.+)$", re.IGNORECASE)
        ]
        
        # Matches: "open <app>", "launch <app>"
        self.open_patterns = [
            re.compile(r"^(?:open|launch|start)\s+(.+?)(?:\s+app)?$", re.IGNORECASE)
        ]

    def parse_intent(self, user_input: str) -> Optional[Dict[str, Any]]:
        """
        Parses a user string into a multi-step execution plan if it matches deterministic patterns.
        """
        user_input = user_input.strip()
        
        # 1. Try URL + Search pattern
        for pattern in self.url_search_patterns:
            match = pattern.match(user_input)
            if match:
                app, url, search_query = match.groups()
                return {
                    "goal": user_input,
                    "steps": [
                        {"action": "open_app", "app": app.strip()},
                        {"action": "open_url", "url": url.strip()},
                        {"action": "search", "query": search_query.strip()}
                    ]
                }
                
        # 2. Try Open + Type pattern
        for pattern in self.type_patterns:
            match = pattern.match(user_input)
            if match:
                app, text = match.groups()
                return {
                    "goal": user_input,
                    "steps": [
                        {"action": "open_app", "app": app.strip()},
                        {"action": "type_text", "text": text}
                    ]
                }
                
        # 3. Try Type In pattern
        for pattern in self.type_in_patterns:
            match = pattern.match(user_input)
            if match:
                text, app = match.groups()
                return {
                    "goal": user_input,
                    "steps": [
                        {"action": "type_text", "text": text, "target_app": app.strip()}
                    ]
                }
                
        # 4. Try Open + URL pattern
        for pattern in self.url_patterns:
            match = pattern.match(user_input)
            if match:
                app, url = match.groups()
                return {
                    "goal": user_input,
                    "steps": [
                        {"action": "open_app", "app": app.strip()},
                        {"action": "open_url", "url": url.strip()}
                    ]
                }
                
        # 5. Try Type Only pattern
        for pattern in self.type_only_patterns:
            match = pattern.match(user_input)
            if match:
                text = match.group(1)
                return {
                    "goal": user_input,
                    "steps": [
                        {"action": "type_text", "text": text}
                    ]
                }
                
        # 6. Try basic Open pattern
        for pattern in self.open_patterns:
            match = pattern.match(user_input)
            if match:
                app = match.group(1)
                return {
                    "goal": f"Open {app.strip()}",
                    "steps": [
                        {"action": "open_app", "app": app.strip()}
                    ]
                }
                
        # Not a deterministically parsable intent
        return None

intent_parser = IntentParser()

