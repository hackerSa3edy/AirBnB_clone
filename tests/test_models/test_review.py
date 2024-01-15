#!/usr/bin/python3
"""This module serves as a unittest suite for the Review class.
The tests cover a range of scenarios, including the initialization,
string representation, saving, and dictionary conversion of
Review objects.
"""
import unittest
import os
import datetime
from models.review import Review
from models.place import Place
from models.user import User
from models.base_model import BaseModel
import models
from time import sleep
import json


class TestReviewInit(unittest.TestCase):
    """Test cases for the initialization of the Review class.
    """
    def setUp(self):
        """Rename the storage file, so it doesn't get overwrited

        Returns:
            The default behavior of the parent class
        """
        try:
            os.rename('file.json', 'temp')
        except FileNotFoundError:
            pass

        return super().setUp()

    def tearDown(self):
        """Reset the storage file name to its default

        Returns:
            The default behavior of the parent class
        """
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

        try:
            os.rename('temp', 'file.json')
        except FileNotFoundError:
            pass

        return super().tearDown()

    def test_parent_class_is_BaseModel(self):
        """Test if the parent of the Review class is BaseModel
        """
        self.assertIsInstance(Review(), BaseModel)
        self.assertTrue(issubclass(Review, BaseModel))

    def test_public_attributes(self):
        """Test the types of public attributes.
        """
        obj = Review()
        self.assertEqual(str, type(obj.id))
        self.assertEqual(datetime.datetime, type(obj.created_at))
        self.assertEqual(datetime.datetime, type(obj.updated_at))
        self.assertEqual(str, type(obj.text))
        self.assertEqual(str, type(obj.place_id))
        self.assertEqual(str, type(obj.user_id))

    def test_empty_review_attributes(self):
        """Test empty review attribute values.
        """
        obj = Review()
        self.assertEqual(obj.text, "")

    def test_attributes_ids_must_exist(self):
        """Test for the place and user ids are the same as in User
        and Place objects
        """
        place = Place()
        user = User()
        obj = Review()
        obj.place_id = place.id
        obj.user_id = user.id
        self.assertIn(
            f"Place.{place.id}",
            list(models.storage.all().keys())
            )
        self.assertIn(
            f"User.{user.id}",
            list(models.storage.all().keys())
            )
        self.assertEqual(
            place.id,
            models.storage.all()[f"Review.{obj.id}"].to_dict()['place_id']
            )
        self.assertEqual(
            user.id,
            models.storage.all()[f"Review.{obj.id}"].to_dict()['user_id']
            )

    def test_uniq_id_for_multiple_objects(self):
        """Test uniqueness of IDs for multiple objects.
        """
        obj1 = Review()
        obj2 = Review()
        obj3 = Review()
        obj4 = Review()
        ids = {obj1.id, obj2.id, obj3.id, obj4.id}
        self.assertTrue(len(ids) == 4)

    def test_same_createdAt_updatedAt(self):
        """Test if created_at and updated_at are the same initially.
        """
        obj = Review()
        self.assertEqual(obj.created_at, obj.updated_at)

    def test_obj_existance_in_storage(self):
        """Test if the object exists in the storage.
        """
        obj = Review()
        self.assertIn(obj, models.storage.all().values())

    def test_instance_recreate_from_dict(self):
        """Test recreating an instance from a dictionary.
        """
        date = datetime.datetime(2024, 1, 14, 17, 7, 0, 0).isoformat()
        dict1 = {
            'id': '1809',
            'created_at': date,
            'updated_at': date,
            '__class__': 'Review',
            'text': 'Not bad!',
            'place_id': '007',
            'user_id': '4090'
            }
        obj = Review(**dict1)
        dict2 = obj.to_dict()
        self.assertDictEqual(dict1, dict2)

    def test_unused_args(self):
        """Test handling unused positional arguments.
        """
        obj = Review('1809')
        self.assertNotIn('1809', obj.__dict__.values())

    def test_unused_args_and_used_kwargs(self):
        """Test handling unused positional arguments and
        used keyword arguments.
        """
        obj = Review('1809', year='2024')
        self.assertNotIn('1809', obj.__dict__.values())
        self.assertIn('2024', obj.__dict__.values())

    def test_adding_additional_attributes(self):
        """Test adding additional attributes to the object.
        """
        obj = Review()
        obj.name = 'Abdelrahman'
        obj.code = 7
        obj.team = ['Zakaria', 'Abdelrahman']
        obj.project = {'AirBnB': 'team_project'}
        obj.rate = 99.6
        obj.available = True

        self.assertEqual(obj.name, 'Abdelrahman')
        self.assertEqual(obj.code, 7)
        self.assertEqual(obj.team, ['Zakaria', 'Abdelrahman'])
        self.assertEqual(obj.project, {'AirBnB': 'team_project'})
        self.assertEqual(obj.rate, 99.6)
        self.assertEqual(obj.available, True)

    def test_createdAt_typeError(self):
        """Test raising a ValueError if created_at has an invalid type
        """
        dict1 = {
            'id': '1809',
            'created_at': '1809',
            'updated_at': '2002',
            '__class__': 'Review',
            'text': 'Not bad!',
            'place_id': '007',
            'user_id': '4090'
            }
        with self.assertRaises(ValueError):
            Review(**dict1)

    def test_updatedAt_typeError(self):
        """Test raising a ValueError if updated_at has an invalid type.
        """
        date = datetime.datetime(2024, 1, 14, 17, 7, 0, 0)
        dict1 = {
            'id': '1809',
            'created_at': date.isoformat(),
            'updated_at': '2002',
            '__class__': 'Review',
            'text': 'Not bad!',
            'place_id': '007',
            'user_id': '4090'
            }
        with self.assertRaises(ValueError):
            Review(**dict1)

    def test_with_None_kwargs(self):
        """Test raising a TypeError if any keyword argument is None.
        """
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


class TestReviewStr(unittest.TestCase):
    """Test cases for the __str__ method of the Review class.
    """
    def setUp(self):
        """Rename the storage file, so it doesn't get overwrited

        Returns:
            The default behavior of the parent class
        """
        try:
            os.rename('file.json', 'temp')
        except FileNotFoundError:
            pass

        return super().setUp()

    def tearDown(self):
        """Reset the storage file name to its default

        Returns:
            The default behavior of the parent class
        """
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

        try:
            os.rename('temp', 'file.json')
        except FileNotFoundError:
            pass

        return super().tearDown()

    def test_formated_output(self):
        """ Test the formatted string output of the Review object.
        """
        obj = Review()
        obj.id = '1809'
        obj.created_at = datetime.datetime(2024, 1, 14, 19, 45, 3, 255968)
        obj.updated_at = obj.created_at
        obj.place_id = '007'
        obj.user_id = '4090'
        obj.text = "Not bad!"

        result = "[Review] (1809) {'id': '1809', 'created_at':" + \
            " datetime.datetime(2024, 1, 14, 19, 45, 3, 255968), " + \
            "'updated_at': datetime.datetime(2024, 1, 14, 19, 45," + \
            " 3, 255968), 'place_id': '007', 'user_id': '4090'" + \
            ", 'text': 'Not bad!'}"

        self.assertEqual(str(obj), result)


class TestReviewSave(unittest.TestCase):
    """Test cases for the save method of the Review class.
    """
    def setUp(self):
        """Rename the storage file, so it doesn't get overwrited

        Returns:
            The default behavior of the parent class
        """
        try:
            os.rename('file.json', 'temp')
        except FileNotFoundError:
            pass

        return super().setUp()

    def tearDown(self):
        """Reset the storage file name to its default

        Returns:
            The default behavior of the parent class
        """
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

        try:
            os.rename('temp', 'file.json')
        except FileNotFoundError:
            pass

        return super().tearDown()

    def test_save_with_args(self):
        """Test raising a TypeError when save method is called
        with arguments.
        """
        obj = Review()
        obj.place_id = '007'
        obj.user_id = '4090'
        obj.text = "Not bad!"
        with self.assertRaises(TypeError):
            obj.save('arg')

    def test_updatedAt_greaterThan_createdAt(self):
        """Test if updated_at is greater than created_at after saving.
        """
        obj = Review()
        obj.place_id = '007'
        obj.user_id = '4090'
        obj.text = "Not bad!"
        sleep(0.3)
        obj.save()
        self.assertGreater(obj.updated_at, obj.created_at)

    def test_updatedAt_greaterThan_prev_updatedAt(self):
        """Test if updated_at is greater than the previous
        updated_at after saving.
        """
        obj = Review()
        obj.place_id = '007'
        obj.user_id = '4090'
        obj.text = "Not bad!"
        prev_updated = obj.updated_at
        obj.save()
        self.assertGreater(obj.updated_at, prev_updated)

    def test_updatedAt_type(self):
        """Test if updated_at is a datetime object after saving.
        """
        obj = Review()
        obj.place_id = '007'
        obj.user_id = '4090'
        obj.text = "Not bad!"
        obj.updated_at = 'foo'
        obj.save()
        self.assertEqual(datetime.datetime, type(obj.updated_at))

    def test_saved_obj_in_storage(self):
        """Test if the saved object is present in the storage.
        """
        obj = Review()
        obj.place_id = '007'
        obj.user_id = '4090'
        obj.text = "Not bad!"
        obj.save()
        with open('file.json', 'r') as f:
            instances = json.load(f)
        self.assertIn(obj.to_dict(), list(instances.values()))


class TestReviewToDict(unittest.TestCase):
    """Test cases for the to_dict method of the Review class.
    """
    def setUp(self):
        """Rename the storage file, so it doesn't get overwrited

        Returns:
            The default behavior of the parent class
        """
        try:
            os.rename('file.json', 'temp')
        except FileNotFoundError:
            pass

        return super().setUp()

    def tearDown(self):
        """Reset the storage file name to its default

        Returns:
            The default behavior of the parent class
        """
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

        try:
            os.rename('temp', 'file.json')
        except FileNotFoundError:
            pass

        return super().tearDown()

    def test_to_dict_with_args(self):
        """Test raising a TypeError when to_dict method is
        called with arguments.
        """
        obj = Review()
        with self.assertRaises(TypeError):
            obj.to_dict('arg')

    def test_create_instance_from_dict(self):
        """Test creating an instance from a dictionary.
        """
        obj = Review()
        obj.place_id = '007'
        obj.user_id = '4090'
        obj.text = "Not bad!"
        data = obj.to_dict()
        obj2 = Review(**data)
        self.assertEqual(obj.id, obj2.id)
        self.assertEqual(obj.created_at, obj2.created_at)
        self.assertEqual(obj.updated_at, obj2.updated_at)

    def test_return_type(self):
        """Test if the return type of to_dict is a dictionary.
        """
        obj = Review()
        obj.place_id = '007'
        obj.user_id = '4090'
        obj.text = "Not bad!"
        data = obj.to_dict()
        self.assertEqual(dict, type(data))

    def test_dict_keys_types(self):
        """Test if the keys in the dictionary are of type string.
        """
        obj = Review()
        obj.place_id = '007'
        obj.user_id = '4090'
        obj.text = "Not bad!"
        data = obj.to_dict()
        for key in data.keys():
            self.assertEqual(str, type(key))

    def test_dict_keys(self):
        """Test if the keys in the dictionary match the expected keys.
        """
        obj = Review()
        obj.place_id = '007'
        obj.user_id = '4090'
        obj.text = "Not bad!"

        data = list(obj.to_dict().keys())
        keys = [
            'id', 'created_at', 'updated_at',
            '__class__', 'place_id', 'user_id', 'text'
            ]
        keys.sort()
        data.sort()
        self.assertEqual(data, keys)

    def test_dict_values_types(self):
        """Test if the values in the dictionary are of type string.
        """
        obj = Review()
        obj.place_id = '007'
        obj.user_id = '4090'
        obj.text = "Not bad!"

        data = obj.to_dict()
        for value in data.values():
            self.assertEqual(str, type(value))

    def test_dict_values(self):
        """Test if the values in the dictionary match the
        expected values.
        """
        date = datetime.datetime(2024, 1, 14, 17, 7, 0, 0)
        dict1 = {
            'id': '1809',
            'created_at': date.isoformat(),
            'updated_at': date.isoformat(),
            '__class__': 'Review',
            'place_id': '007',
            'user_id': '4090',
            'text': 'Not bad!'
            }

        obj = Review(**dict1)
        for key, value in obj.to_dict().items():
            self.assertEqual(dict1[key], value)


if __name__ == '__main__':
    unittest.main()
