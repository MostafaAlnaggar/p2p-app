import unittest
from db import DB
from pymongo import MongoClient
from HashPassword import hash_password
class RegistrationTest(unittest.TestCase):
    def setUp(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = DB()
        self.db.accounts = self.client['p2p-chat']['accounts']
    def testRegister(self):
        username = 'test_user'
        password = 'test_password'
        password = hash_password(password)
        self.db.register(username, password)
        query = {"username": username.lower(), "password": password}
        result = self.db.accounts.find_one(query)
        self.assertIsNotNone(result)
if __name__ == '__main__':
    unittest.main()
