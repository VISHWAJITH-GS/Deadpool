class Persona:
    @staticmethod
    def format_response(text: str) -> str:
        """Applies final persona formatting if needed."""
        # For MVP, we mostly rely on the system prompt for persona,
        # but we can inject signature phrases or modify text here.
        if not text.strip():
            return "*stares in silence*"
        return text
