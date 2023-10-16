#!/usr/bin/python3
""" Tests for class fileStorage """
import unittest
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """ Sets up the class test """
        self.base = BaseModel()
        self.amen = Amenity()
        self.cit = City()
        self.pla = Place()
        self.rev = Review()
        self.sta = State()
        self.use = User()
        self.storage = FileStorage()
        self.storage.save()
        if os.path.exists("file.json"):
            pass
        else:
            os.mknod("file.json")

    def tearDown(self):
        """ Tears down the testing environment """
        del self.base
        del self.amen
        del self.cit
        del self.pla
        del self.rev
        del self.sta
        del self.use
        del self.storage
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """ test all method """
        obj = self.storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, self.storage._FileStorage__objects)

    def test_storage_empty(self):
        """ Test storage not empty """
        self.assertIsNotNone(self.storage.all())

    def test_storage_all_type(self):
        """ Test type storage """
        self.assertEqual(dict, type(self.storage.all()))

    def test_new(self):
        """ Test new User """
        obj = self.storage.all()
        self.use.id = 1234
        self.use.name = "Julien"
        self.storage.new(self.use)
        key = "{}.{}".format(self.use.__class__.__name__, self.use.id)
        self.assertIsNotNone(obj[key])

    def test_check_json_loading(self):
        """ Test load of json file """

        with open("file.json") as my_file:
            dic = json.load(my_file)
            self.assertEqual(isinstance(dic, dict), True)

    def test_file_existence(self):
        """
            Test working of Storage Engine's methods
        """
        with open("file.json") as my_file:
            self.assertTrue(len(my_file.read()) > 0)


if __name__ == '__main__':
    unittest.main()
