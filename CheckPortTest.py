import unittest
from db import DB
from pymongo import MongoClient
class TestCheckPortTest(unittest.TestCase):
    def setUp(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = DB()
        self.db.online_peers = self.client['p2p-chat']['online_peers']
    def testPortNumber(self):
        try:
            test_username = 'user_test'
            test_ip = '127.444.77'
            test_port = 15440
            self.db.online_peers.insert_one({"username": test_username.lower(), "ip": test_ip, "port": test_port})
            ip, port = self.db.get_peer_ip_port(test_username)
            self.assertEqual(ip, test_ip)
            self.assertEqual(port, test_port)
        except Exception as e:
            self.fail(f"Error retrieving the port Number: {e}")
if __name__ == '__main__':
    unittest.main()
