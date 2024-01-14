#!/usr/bin/python3
"""
This module provides a unittest suite for testing the BaseModel class.
The BaseModel class serves as a foundation for other classes and is
intended to handle common attributes and behaviors shared by various
objects in a Python application.
"""
import unittest
import os
import datetime
from models.base_model import BaseModel
import models
from time import sleep
import json


class TestBaseModelInit(unittest.TestCase):
    """Test the constructor of the BaseModel class

    Arguments:
        unittest -- Inherits unittest.TestCase's attributes and methods
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

    def test_public_attributes(self):
        """Test if the attributes are public
        """
        obj = BaseModel()
        self.assertEqual(str, type(obj.id))
        self.assertEqual(datetime.datetime, type(obj.created_at))
        self.assertEqual(datetime.datetime, type(obj.updated_at))

    def test_uniq_id_for_multiple_objects(self):
        """Test the uniqueness of objects' ids
        """
        obj1 = BaseModel()
        obj2 = BaseModel()
        obj3 = BaseModel()
        obj4 = BaseModel()
        ids = {obj1.id, obj2.id, obj3.id, obj4.id}
        self.assertTrue(len(ids) == 4)

    def test_same_createdAt_updatedAt(self):
        """Test if created_at and updated_at are the same
        """
        obj = BaseModel()
        self.assertEqual(obj.created_at, obj.updated_at)

    def test_obj_existance_in_storage(self):
        """Test if the created object exists in the storage
        """
        obj = BaseModel()
        self.assertIn(obj, models.storage.all().values())

    def test_instance_recreate_from_dict(self):
        """Test recreating an instance from a dictionary
        """
        date = datetime.datetime(2024, 1, 14, 17, 7, 0, 0).isoformat()
        dict1 = {
            'id': '1809',
            'created_at': date,
            'updated_at': date,
            '__class__': 'BaseModel'
            }
        obj = BaseModel(**dict1)
        dict2 = obj.to_dict()
        self.assertDictEqual(dict1, dict2)

    def test_unused_args(self):
        """Test creating an object with unused arguments
        """
        obj = BaseModel('1809')
        self.assertNotIn('1809', obj.__dict__.values())

    def test_unused_args_and_used_kwargs(self):
        """Tests the creation of an object with unused arguments
        and used keyword arguments.
        """
        obj = BaseModel('1809', year='2024')
        self.assertNotIn('1809', obj.__dict__.values())
        self.assertIn('2024', obj.__dict__.values())

    def test_adding_additional_attributes(self):
        """Tests adding additional attributes to the object.
        """
        obj = BaseModel()
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
        """Tests TypeError when creating an object with an incorrect
        data type for created_at.
        """
        dict1 = {
            'id': '1809',
            'created_at': '1809',
            'updated_at': '2002',
            '__class__': 'BaseModel'
            }
        with self.assertRaises(ValueError):
            BaseModel(**dict1)

    def test_updatedAt_typeError(self):
        """Tests TypeError when creating an object with an incorrect
        data type for updated_at.
        """
        date = datetime.datetime(2024, 1, 14, 17, 7, 0, 0)
        dict1 = {
            'id': '1809',
            'created_at': date.isoformat(),
            'updated_at': '2002',
            '__class__': 'BaseModel'
            }
        with self.assertRaises(ValueError):
            BaseModel(**dict1)

    def test_with_None_kwargs(self):
        """Tests TypeError when creating an object with None as arguments.
        """
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)


class TestBaseModelStr(unittest.TestCase):
    """This class contains test cases for the __str__ method of
    the BaseModel class.
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
        """Tests if the output of the __str__ method is formatted correctly.
        """
        obj = BaseModel()
        obj.id = '1809'
        obj.created_at = datetime.datetime(2024, 1, 14, 19, 45, 3, 255968)
        obj.updated_at = datetime.datetime(2024, 1, 14, 19, 45, 3, 255968)

        result = "[BaseModel] (1809) {'id': '1809', " + \
            "'created_at': datetime.datetime(2024, 1, 14," + \
            " 19, 45, 3, 255968), 'updated_at': datetime.datetime(2024," + \
            " 1, 14, 19, 45, 3, 255968)}"

        self.assertEqual(str(obj), result)


class TestBaseModelSave(unittest.TestCase):
    """This class contains test cases for the save method of the
    BaseModel class.
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
        """Tests if save method raises a TypeError when called with arguments.
        """
        obj = BaseModel()
        with self.assertRaises(TypeError):
            obj.save('arg')

    def test_updatedAt_greaterThan_createdAt(self):
        """Tests if updated_at is greater than created_at after calling save.
        """
        obj = BaseModel()
        sleep(0.3)
        obj.save()
        self.assertGreater(obj.updated_at, obj.created_at)

    def test_updatedAt_greaterThan_prev_updatedAt(self):
        """Tests if updated_at is greater than the previous
        updated_at after calling save.
        """
        obj = BaseModel()
        prev_updated = obj.updated_at
        obj.save()
        self.assertGreater(obj.updated_at, prev_updated)

    def test_updatedAt_type(self):
        """Tests if updated_at retains its type after calling save.
        """
        obj = BaseModel()
        obj.updated_at = 'foo'
        obj.save()
        self.assertEqual(datetime.datetime, type(obj.updated_at))

    def test_saved_obj_in_storage(self):
        """Tests if the saved object exists in the storage file.
        """
        obj = BaseModel()
        obj.save()
        with open('file.json', 'r') as f:
            instances = json.load(f)
        self.assertIn(obj.to_dict(), list(instances.values()))


class TestBaseModelToDict(unittest.TestCase):
    """This class contains test cases for the to_dict method
    of the BaseModel class.
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
        """Tests if to_dict method raises a TypeError when called
        with arguments.
        """
        obj = BaseModel()
        with self.assertRaises(TypeError):
            obj.to_dict('arg')

    def test_create_instance_from_dict(self):
        """Tests if an object can be created from a dictionary.
        """
        obj = BaseModel()
        data = obj.to_dict()
        obj2 = BaseModel(**data)
        self.assertEqual(obj.id, obj2.id)
        self.assertEqual(obj.created_at, obj2.created_at)
        self.assertEqual(obj.updated_at, obj2.updated_at)

    def test_return_type(self):
        """Tests if the return type of to_dict is a dictionary.
        """
        obj = BaseModel()
        data = obj.to_dict()
        self.assertEqual(dict, type(data))

    def test_dict_keys_types(self):
        """Tests if all keys in the dictionary returned by to_dict
        have the correct type.
        """
        obj = BaseModel()
        data = obj.to_dict()
        for key in data.keys():
            self.assertEqual(str, type(key))

    def test_dict_keys(self):
        """Tests if the keys in the dictionary match the expected keys.
        """
        obj = BaseModel()
        data = list(obj.to_dict().keys())
        keys = ['id', 'created_at', 'updated_at', '__class__']
        keys.sort()
        data.sort()
        self.assertEqual(data, keys)

    def test_dict_values_types(self):
        """Tests if all values in the dictionary returned by
        to_dict have the correct type.
        """
        obj = BaseModel()
        data = obj.to_dict()
        for value in data.values():
            self.assertEqual(str, type(value))

    def test_dict_values(self):
        """Tests if the values in the dictionary match the expected values.
        """
        date = datetime.datetime(2024, 1, 14, 17, 7, 0, 0)
        dict1 = {
            'id': '1809',
            'created_at': date.isoformat(),
            'updated_at': date.isoformat(),
            '__class__': 'BaseModel'
            }

        obj = BaseModel(**dict1)
        for key, value in obj.to_dict().items():
            self.assertEqual(dict1[key], value)


if __name__ == '__main__':
    unittest.main()
