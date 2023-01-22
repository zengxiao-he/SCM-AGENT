"""
Base service class for SCM-AGENT
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
import logging

class BaseService(ABC):
    """Abstract base service class"""
    
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
    
    @abstractmethod
    def validate_input(self, data: Dict[str, Any]) -> bool:
        """Validate input data"""
        pass
    
    @abstractmethod
    def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Process the data"""
        pass
    
    def log_operation(self, operation: str, data: Dict[str, Any]):
        """Log service operations"""
        self.logger.info(f"Operation: {operation}, Data: {data}")
    
    def handle_error(self, error: Exception) -> Dict[str, Any]:
        """Handle service errors"""
        self.logger.error(f"Service error: {str(error)}")
        return {
            "error": True,
            "message": str(error),
            "type": error.__class__.__name__
        }
