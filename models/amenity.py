#!/usr/bin/python3
"""Amenity Module to create Amenities"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class

    Arguments:
        BaseModel -- Inherts BaseModel's attributes and methods
    """

    name = ''
