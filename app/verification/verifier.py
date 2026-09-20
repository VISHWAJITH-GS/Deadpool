from typing import Any, Dict

class Verifier:
    def verify(self, tool_name: str, args: Dict[str, Any], result: str) -> bool:
        """
        Generic verification framework for tools.
        Returns True if the action is deemed successful based on its verification strategy.
        """
        if "Error" in result:
            return False
            
        if tool_name == "launch_application":
            return "Success" in result or "Launched" in result
            
        if tool_name == "type_text":
            return "Success" in result or "Typed" in result
            
        # Default verification expects successful return text
        return True

verifier = Verifier()
