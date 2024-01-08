import unittest
from db import DB
from pymongo import MongoClient


class CheckRoomExistTest(unittest.TestCase):
    def setUp(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = DB()
        self.db.chat_room = self.client['p2p-chat']['chat_rooms']
    def testRoomCheck(self):
        try:
            test_room_name = 'test_room'
            self.db.chat_rooms.insert_one({"name": test_room_name.lower()})
            room_exists = self.db.chat_room_exists(test_room_name)
            self.assertTrue(room_exists)
        except Exception as e:
            self.fail(f"Room not saved in DB: {e}")
if __name__ == '__main__':
    unittest.main()
