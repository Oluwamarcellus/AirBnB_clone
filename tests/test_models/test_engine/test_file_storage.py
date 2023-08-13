#!/usr/bin/env python3
"""
Test for FileStorage module
"""


import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
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
        city = City()
        state = State()
        amenity = Amenity()
        user = User()
        review = Review()
        place = Place()
        base = BaseModel()
        self.assertIn("City." + city.id, models.storage.all().keys())
        self.assertIn("State." + state.id, models.storage.all().keys())
        self.assertIn("Amenity." + amenity.id, models.storage.all().keys())
        self.assertIn("User." + user.id, models.storage.all().keys())
        self.assertIn("Review." + review.id, models.storage.all().keys())
        self.assertIn("Place." + place.id, models.storage.all().keys())
        self.assertIn("BaseModel." + base.id, models.storage.all().keys())
        self.assertIn(city, models.storage.all().values())
        self.assertIn(state, models.storage.all().values())
        self.assertIn(amenity, models.storage.all().values())
        self.assertIn(user, models.storage.all().values())
        self.assertIn(review, models.storage.all().values())
        self.assertIn(place, models.storage.all().values())
        self.assertIn(base, models.storage.all().values())

    def test_save(self):
        """
        Testing the save() method
        """
        city = City()
        state = State()
        amenity = Amenity()
        user = User()
        review = Review()
        place = Place()
        base = BaseModel()
        models.storage.save()
        with open("file.json", "r") as file:
            f_contents = file.read()
            self.assertIn("City." + city.id, f_contents)
            self.assertIn("State." + state.id, f_contents)
            self.assertIn("Amenity." + amenity.id, f_contents)
            self.assertIn("User." + user.id, f_contents)
            self.assertIn("Review." + review.id, f_contents)
            self.assertIn("Place." + place.id, f_contents)
            self.assertIn("BaseModel." + base.id, f_contents)


class TestTypes(unittest.TestCase):
    """
    Test fot instances types
    """

    def test_file_storage_inst(self):
        """
        Testing FS inst type
        """
        fs = FileStorage()
        self.assertEqual(type(fs), FileStorage)

    def test_storage(self):
        """
        Testing storage inst
        """
        self.assertEqual(type(models.storage), FileStorage)


if __name__ == "__main__":
    unittest.main()
