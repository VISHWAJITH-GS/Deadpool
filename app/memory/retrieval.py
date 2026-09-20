from typing import List
from app.memory.store import memory_store

class MemoryRetriever:
    @staticmethod
    def get_context_string() -> str:
        """Returns all long-term explicit memories formatted as a context string."""
        memories = memory_store.get_all_memories()
        if not memories:
            return "No explicit memories recorded."
        
        lines = ["Explicit Memories:"]
        for m in memories:
            lines.append(f"- [{m['id']}] {m['content']}")
        return "\n".join(lines)
