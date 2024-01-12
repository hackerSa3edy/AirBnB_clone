#!/usr/bin/python3
"""User Module to create users"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class

    Arguments:
        BaseModel -- Inherts BaseModel's attributes and methods
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
