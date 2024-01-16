#!/usr/bin/python3
"""_summary_
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorageAttrs(unittest.TestCase):
    """_summary_

    Arguments:
        unittest -- _description_
    """
    def test_private_attr_file_path(self):
        """_summary_
        """
        pass

    def test_private_attr_objects(self):
        """_summary_
        """
        pass

    def test_with_additional_attr(self):
        """_summary_
        """
        pass


class TestFileStorageAll(unittest.TestCase):
    """_summary_

    Arguments:
        unittest -- _description_
    """
    def test_objects_existance_at_objects_attr(self):
        """_summary_
        """
        pass

    def test_with_additional_attr(self):
        """_summary_
        """
        pass


class TestFileStorageNew(unittest.TestCase):
    """_summary_

    Arguments:
        unittest -- _description_
    """
    def test_new_object_in_objects_attr(self):
        """_summary_
        """
        pass

    def test_new_with_noArgs(self):
        """_summary_
        """
        pass

    def test_new_object_without_id_attr(self):
        """_summary_
        """
        pass

    def test_with_additional_attr(self):
        """_summary_
        """
        pass


class TestFileStorageSave(unittest.TestCase):
    """_summary_

    Arguments:
        unittest -- _description_
    """
    def test_with_additional_attr(self):
        """_summary_
        """
        pass

    def test_object_saved_in_file(self):
        """_summary_
        """
        pass

    def test_object_without_toDict_method(self):
        """_summary_
        """
        pass

    def test_saved_empty_objects_attr(self):
        """_summary_
        """
        pass


class TestFileStorageReload(unittest.TestCase):
    """_summary_

    Arguments:
        unittest -- _description_
    """
    def test_with_additional_attr(self):
        """_summary_
        """
        pass

    def test_file_not_exist(self):
        """_summary_
        """
        pass

    def test_loaded_objects_not_json(self):
        """_summary_
        """
        pass

    def test_specified_object_not_found_in_models_dict(self):
        """_summary_
        """
        pass

    def test_the_attr_class_not_found_in_object(self):
        """_summary_
        """
        pass

    def test_reloaded_objects_are_in_file(self):
        """_summary_
        """
        pass
