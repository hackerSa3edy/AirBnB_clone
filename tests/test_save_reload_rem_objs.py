#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)


print("-- Create a new State --")
my_user = State()
my_user.name = "Sohag"
my_user.save()

print("-- Create a new Review --")
my_user = Review()
my_user.text = "Test reviews"
my_user.place_id = "place_id"
my_user.user_id = "user_id"
my_user.save()
print(my_user)

print("-- Create a new Place --")
my_user = Place()
my_user.city_id = "city_id"
my_user.user_id = "user_id"
my_user.name = "name of the place"
my_user.number_rooms = 32
my_user.number_bathrooms = 88
my_user.max_guest = 33
my_user.price_by_night = 99
my_user.latitude = 33.34
my_user.longitude = 23.3
my_user.amenity_ids = ['idAmenity1', 'idAmenity2']
my_user.save()
print(my_user)

print("-- Create a new City --")
my_user = City()
my_user.name = "state_name"
my_user.state_id = "state_id"
my_user.save()
print(my_user)

print("-- Create a new Amenity --")
my_user = Amenity()
my_user.name = "Amenity"
my_user.save()
print(my_user)
