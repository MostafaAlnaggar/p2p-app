import unittest
from db import DB
from pymongo import MongoClient

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = DB()
        self.db.online_peers = self.client['p2p-chat']['online_peers']
    def testIsOnline(self):
        try:
            username = 'test_user'
            password = 'test_password'
            ip = "127.222.77"
            port = 15900
            self.db.register(username, password)
            self.db.user_login(username, ip, port)
            is_online = self.db.is_account_online(username)
            self.assertTrue(is_online)
        except Exception as e:
            self.fail(f"Error checking the online user: {e}")
if __name__ == '__main__':
    unittest.main()
