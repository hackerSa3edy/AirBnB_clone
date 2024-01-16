#!/usr/bin/python3
"""
This testing module is designed to thoroughly test the functionalities
of the FileStorage class, which is responsible for serializing instances
to a JSON file and deserializing JSON files to instances in the context
of a simple object-relational mapping (ORM) system. The module includes
various test classes, each focusing on specific aspects of the FileStorage
class.
"""
import unittest
import datetime
import json
import os
from models.base_model import BaseModel
import models


class TestFileStorageAttrs(unittest.TestCase):
    """Testing the attributes of the FileStorage class.

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

        # Initialize new storage before each test
        models.FileStorage._FileStorage__objects = {}

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

    def test_the_private_attributes_objects_type(self):
        """Test the type of the private attribute __objects
        """
        self.assertEqual(dict, type(models.FileStorage._FileStorage__objects))


    def test_the_private_attributes_filePath_type(self):
        """Test the type of the private attribute __file_path
        """
        self.assertEqual(str, type(models.FileStorage._FileStorage__file_path))

    def test_the_default_value_for_file_path_private_attributes(self):
        """Check for the default value for the __file_path private attributes
        """
        self.assertEqual('file.json', models.FileStorage._FileStorage__file_path)

    def test_the_default_value_for_objects_private_attributes(self):
        """Check for the default value for the __objects private attributes
        """
        self.assertEqual({}, models.FileStorage._FileStorage__objects)

    def test_private_attributes(self):
        """Tests the existence and privacy of the __file_path and
        __objects attributes.
        """
        with self.assertRaises(AttributeError):
            models.storage.__file_path
            models.storage.__objects

    def test_with_additional_attr(self):
        """Test adding additional attributes
        """
        models.storage.test = True
        self.assertEqual(models.storage.test, True)


class TestFileStorageAll(unittest.TestCase):
    """Testing the all method of the FileStorage class.

    Arguments:
        unittest -- _description_Inherits unittest.TestCase's attributes
        and methods
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

        # Initialize new storage before each test
        models.FileStorage._FileStorage__objects = {}

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

    def test_objects_same_as_in_objects_attr(self):
        """Ensures that loaded objects is the same as the object.
        """
        obj = BaseModel()
        obj2 = BaseModel()
        self.assertDictEqual(
            {
                f"BaseModel.{obj.id}": obj,
                f"BaseModel.{obj2.id}": obj2
                },
            models.storage.all()
            )

    def test_with_additional_args(self):
        """Test adding additional arguments
        """
        with self.assertRaises(TypeError):
            models.storage.all('argument')


class TestFileStorageNew(unittest.TestCase):
    """Testing the new method of the FileStorage class.

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

        # Initialize new storage before each test
        models.FileStorage._FileStorage__objects = {}

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

    def test_new_object_in_objects_attr(self):
        """Verifies that a new object is correctly added to the __objects
        attribute.
        """
        obj = BaseModel()
        self.assertIn(obj, models.storage.all().values())

    def test_new_with_noArgs(self):
        """Tests the behavior of the new method when called with no
        arguments.
        """
        with self.assertRaises(TypeError):
            models.storage.new()

    def test_new_object_without_id_attr(self):
        """Tests the behavior of the new method when called with an object
        without the id attribute.
        """
        date = datetime.datetime(2024, 1, 14, 17, 7, 0, 0)
        dict1 = {
            'created_at': date.isoformat(),
            'updated_at': date.isoformat(),
            '__class__': 'BaseModel'
            }
        obj = BaseModel(**dict1)
        with self.assertRaises(AttributeError):
            models.storage.new(obj)

    def test_with_additional_args(self):
        """Test adding additional arguments
        """
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 'argument')


class TestFileStorageSave(unittest.TestCase):
    """Test the save method of the FileStorage class.

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

        # Initialize new storage before each test
        models.FileStorage._FileStorage__objects = {}

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

    def test_with_additional_args(self):
        """Test adding additional arguments
        """
        with self.assertRaises(TypeError):
            models.storage.save('argument')

    def test_object_saved_in_file(self):
        """Verifies that objects are correctly saved to the JSON file.
        """
        obj = BaseModel()
        obj.save()
        data = obj.to_dict()
        with open('file.json', 'r') as file:
            json_data = json.load(file)

        self.assertIn(data, list(json_data.values()))

    def test_object_without_toDict_method(self):
        """Ensures proper handling when attempting to save an object without
        a to_dict method.
        """
        class Test:
            id = '333'
        obj = Test()
        models.storage.new(obj)
        with self.assertRaises(AttributeError):
            models.storage.save()

    def test_saved_empty_objects_attribute(self):
        """Tests the behavior of saving when the __objects attribute is empty.
        """
        models.storage.save()
        with open('file.json', 'r') as file:
            json_data = json.load(file)
        self.assertDictEqual(json_data, models.storage.all())


class TestFileStorageReload(unittest.TestCase):
    """Testing the reload method of the FileStorage class.

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

        # Initialize new storage before each test
        models.FileStorage._FileStorage__objects = {}

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

    def test_with_additional_args(self):
        """Test adding additional arguments
        """
        with self.assertRaises(TypeError):
            models.storage.reload('argument')

    def test_file_not_exist(self):
        """Tests the behavior when attempting to reload from a non-existent
        file.
        """
        obj = BaseModel()
        prev_dict = models.storage.all()
        models.storage.reload()
        curr_dict = models.storage.all()
        self.assertDictEqual(prev_dict, curr_dict)

    def test_loaded_objects_not_json(self):
        """Ensures proper handling when the loaded data from the file is not
        in JSON format.
        """
        with open('file.json', 'w') as file:
            file.write("Well son, very proud of you.")

        with self.assertRaises(json.JSONDecodeError):
            models.storage.reload()

    def test_specified_object_not_found_in_models_dict(self):
        """Tests the case when a specified object in the loaded data is not
        found in the models_dict.
        """
        with open('file.json', 'w') as file:
            file.write('\
                       {\
                           "BaseModel.f1a83b88-534e-4cf1-841d-091f71f057af":\
                           {\
                               "id": "f1a83b88-534e-4cf1-841d-091f71f057af",\
                               "created_at": "2024-01-16T13:51:12.445588",\
                               "updated_at": "2024-01-16T13:51:16.891133",\
                               "__class__": "TestReload"\
                           }\
                       }')

        with self.assertRaises(KeyError):
            models.storage.reload()

    def test_the_attr_class_not_found_in_object(self):
        """Verifies the handling of cases where the '__class__' attribute
        is not found in the loaded object.
        """

        with open('file.json', 'w') as file:
            file.write('\
                       {\
                           "BaseModel.f1a83b88-534e-4cf1-841d-091f71f057af":\
                           {\
                               "id": "f1a83b88-534e-4cf1-841d-091f71f057af",\
                               "created_at": "2024-01-16T13:51:12.445588",\
                               "updated_at": "2024-01-16T13:51:16.891133"\
                           }\
                       }')

        with self.assertRaises(KeyError) as file:
            models.storage.reload()

    def test_empty_loaded_file(self):
        """Test the behavior when loading an empty file
        """
        models.storage.reload()
        self.assertDictEqual({}, models.storage.all())

    def test_new_object_before_saving_exists_after_reload(self):
        """Ensures that the new objects before saving them in a file
        are exist after reloading objects from a file.
        """
        obj = BaseModel()
        obj.save()
        obj2 = BaseModel()
        models.storage.reload()

        self.assertIn(obj2, list(models.storage.all().values()))


if __name__ == '__main__':
    unittest.main()
