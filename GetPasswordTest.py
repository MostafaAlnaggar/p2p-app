import unittest
from db import DB
from pymongo import MongoClient
from HashPassword import hash_password
class GetPassswordTest(unittest.TestCase):
    def setUp(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = DB()
        self.db.accounts = self.client['p2p-chat']['accounts']
    def testGetPassword(self):
        username = 'test_user'
        password = 'test_password'
        hashed_password = hash_password(password)
        self.db.accounts.insert_one({
            "username": username,
            "password": hashed_password,  # Save the hashed password
            "group": None
        })
        retrieved_password = self.db.get_password(username)

        self.assertEqual(retrieved_password, hashed_password)  # add assertion her
if __name__ == '__main__':
    unittest.main()
