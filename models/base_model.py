#!/usr/bin/env python
"""Base class for all models"""
import uuid
import datetime

class BaseModel():
    def __init__(self):
        """Set shared models attributes."""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Convert the instance to string.

        Returns:
            Human readable representation of the class.
        """

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the updated_at instance attribute."""

        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Convert the instance to a dict"""

        instance_to_dict = self.__dict__.copy()
        instance_to_dict.update({'__class__': self.__class__.__name__, 'created_at': self.created_at.isoformat(), 'updated_at': self.updated_at.isoformat()})
        return instance_to_dict
