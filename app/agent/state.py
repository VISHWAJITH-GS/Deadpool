from enum import Enum

class AgentState(Enum):
    IDLE = "IDLE"
    UNDERSTANDING = "UNDERSTANDING"
    OBSERVING = "OBSERVING"
    PLANNING = "PLANNING"
    WAITING_PERMISSION = "WAITING_PERMISSION"
    EXECUTING = "EXECUTING"
    VERIFYING = "VERIFYING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

class StateMachine:
    def __init__(self):
        self.state = AgentState.IDLE
        
    def transition(self, new_state: AgentState):
        """Transitions to a new state and logs it."""
        print(f"[STATE] Transitioning from {self.state.name} -> {new_state.name}")
        self.state = new_state
        
    def get_state(self) -> AgentState:
        return self.state
