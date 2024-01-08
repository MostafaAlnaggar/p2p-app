import unittest
from pymongo import MongoClient
from unittest.mock import MagicMock
from db import DB
class UserLeaveGroupTest(unittest.TestCase):
    def setUp(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = DB()
        self.db.chat_rooms = self.client['p2p-chat']['chat_rooms']
        self.db.accounts = self.client['p2p-chat']['accounts']
    def testUserLeaveGroup(self):
        # Create MagicMock objects to mock the find_one and update_one methods
        self.db.accounts.find_one = MagicMock(return_value={"username": "test_user", "group": "test_group"})
        self.db.accounts.update_one = MagicMock()
        result = self.db.user_leave_room("test_user")
        self.db.accounts.update_one.assert_called_once_with(
            {"username": "test_user"},
            {"$set": {"group": None}}
        )
        self.assertTrue(result)
if __name__ == '__main__':
    unittest.main()
