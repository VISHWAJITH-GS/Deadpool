from typing import List, Dict, Any, Optional

class TaskState:
    def __init__(self, original_goal: str):
        self.original_goal = original_goal
        self.current_goal: str = original_goal
        self.current_step: Optional[str] = None
        self.completed_steps: List[str] = []
        self.remaining_steps: List[str] = []
        self.active_application: Optional[str] = None
        self.active_window: Optional[str] = None
        self.latest_observation: Optional[str] = None
        self.available_ui_elements: List[Dict[str, Any]] = []
        self.planned_action: Optional[Dict[str, Any]] = None
        self.action_history: List[Dict[str, Any]] = []
        self.verification_result: Optional[str] = None
        self.error_history: List[Dict[str, Any]] = []
        self.retry_count: int = 0
        self.safety_status: str = "UNKNOWN"
        self.task_status: str = "INITIALIZED"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "original_goal": self.original_goal,
            "current_goal": self.current_goal,
            "current_step": self.current_step,
            "completed_steps": self.completed_steps,
            "remaining_steps": self.remaining_steps,
            "active_application": self.active_application,
            "task_status": self.task_status
        }
