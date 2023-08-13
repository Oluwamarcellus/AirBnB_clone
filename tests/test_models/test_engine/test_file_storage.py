#!/usr/bin/env python3
"""
Test for FileStorage module
"""


import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import datetime
import unittest
import models
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestStorage(unittest.TestCase):
    """
    Testing FileStorage class
    """

    @classmethod
    def setup(cls):
        """
        Preps for testing
        """
        try:
            os.rename("file.json", "tmp")
        except Exception:
            pass

    @classmethod
    def tearDownClass(cls):
        """
        Restoring file
        """
        try:
            os.remove("file.json")
        except Exception:
            pass
        try:
            os.rename("tmp", "file.json")
        except Exception:
            pass

    def test_inst(self):
        """
        Testing instance type
        """
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)

    def test_storage_all(self):
        """
        Testing the all() method
        """
        storage = FileStorage()
        dic = storage.all()
        self.assertIsInstance(dic, dict)

    def test_new(self):
        """
        Testing the new() method
        """
        sample = City()
        models.storage.new(sample)
        self.assertIn("City." + sample.id, models.storage.all().keys())
        self.assertIn(sample, models.storage.all().values())

    def test_save(self):
        """
        Testing the save() method
        """
        sample = City()
        models.storage.new(sample)
        models.storage.save()
        with open("file.json", "r") as file:
            f_contents = file.read()
            self.assertIn("City." + sample.id, f_contents)


if __name__ == "__main__":
    unittest.main()
