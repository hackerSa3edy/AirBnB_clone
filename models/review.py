#!/usr/bin/env python
"""Review class for reviews instances creation"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Initialize Review class"""

    place_id = ''
    user_id = ''
    text = ''
