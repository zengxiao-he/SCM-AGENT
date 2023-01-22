"""
Base model class for SCM-AGENT
"""

from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional
import uuid

@dataclass
class BaseModel:
    """Base model with common fields"""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    
    def update_timestamp(self):
        """Update the updated_at timestamp"""
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """Convert model to dictionary"""
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
