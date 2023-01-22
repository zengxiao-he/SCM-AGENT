"""
Base AI Agent for SCM-AGENT system
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List
import logging
from datetime import datetime

class BaseAgent(ABC):
    """Abstract base class for all SCM agents"""
    
    def __init__(self, name: str, version: str = "1.0.0"):
        self.name = name
        self.version = version
        self.created_at = datetime.now()
        self.logger = logging.getLogger(f"Agent.{name}")
        self.state = "initialized"
    
    @abstractmethod
    def analyze(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze input data and return insights"""
        pass
    
    @abstractmethod
    def recommend(self, analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate recommendations based on analysis"""
        pass
    
    def get_status(self) -> Dict[str, Any]:
        """Get agent status information"""
        return {
            "name": self.name,
            "version": self.version,
            "state": self.state,
            "created_at": self.created_at.isoformat(),
            "uptime": (datetime.now() - self.created_at).total_seconds()
        }
    
    def log_activity(self, activity: str, details: Dict[str, Any] = None):
        """Log agent activities"""
        log_data = {"activity": activity, "agent": self.name}
        if details:
            log_data.update(details)
        self.logger.info(log_data)
    
    def set_state(self, new_state: str):
        """Update agent state"""
        old_state = self.state
        self.state = new_state
        self.log_activity("state_change", {"from": old_state, "to": new_state})
