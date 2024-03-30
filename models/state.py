#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from datetime import datetime


class State(BaseModel):
    """ State class """
    name = ""

    def __str__(self):
        """String representation of State instance"""
        attributes = {
            'name': self.name,
            'created_at': repr(self.created_at),
            'id': self.id,
        }
        return "[State] ({}) {}".format(self.id, attributes)