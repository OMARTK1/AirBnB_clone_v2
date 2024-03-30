#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel


class Place(BaseModel):
    """ A place to stay """
    number_bathrooms = 0
    longitude = 0.0
    city_id = ""
    user_id = ""
    name = ""
    latitude = 0.0
    price_by_night = 0
    description = ""
    number_rooms = 0
    max_guest = 0
    amenity_ids = []

    def __str__(self):
        """ Return string representation of Place object """
        attributes = {
            'number_bathrooms': self.number_bathrooms,
            'city_id': self.city_id,
            'user_id': self.user_id,
            'latitude': self.latitude,
            'price_by_night': self.price_by_night,
            'name': self.name,
            'id': self.id,
            'max_guest': self.max_guest,
            'updated_at': repr(self.updated_at),
            'created_at': repr(self.created_at),
            #'number_rooms': self.number_rooms,
            #'longitude': self.longitude,
        }
        return "[Place] ({}) {}".format(self.id, attributes)
