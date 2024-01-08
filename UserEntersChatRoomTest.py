import unittest
from db import DB
from pymongo import MongoClient
class UserEnterChatRoomTest(unittest.TestCase):
    def setUp(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = DB()
        self.db.chat_rooms = self.client['p2p-chat']['chat_rooms']
        self.db.accounts = self.client['p2p-chat']['accounts']
    def testUserJoinChatRoom(self):
        test_username = 'test_user'
        test_group = 'test_group'
        self.db.chat_rooms.insert_one({"name": test_group.lower()})
        user_exists = self.db.accounts.find_one({"username": test_username.lower()})
        group_exists = self.db.chat_rooms.find_one({"name": test_group.lower()})

        # If both user and group exist, attempt to join the user to the group
        if user_exists and group_exists:
            result = self.db.user_join_room(test_username, test_group)
            self.assertIsNotNone(result)  # Check if the update operation was successful
        else:
            self.fail(f"Either user '{test_username}' or group '{test_group}' does not exist")
if __name__ == '__main__':
    unittest.main()
