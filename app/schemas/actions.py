from typing import Any, Dict, List
from dataclasses import dataclass, field

@dataclass
class ToolCall:
    name: str
    arguments: Dict[str, Any] = field(default_factory=dict)

@dataclass
class AgentResponse:
    text: str
    tool_calls: List[ToolCall] = field(default_factory=list)
