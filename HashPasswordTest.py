import unittest
import hashlib
from HashPassword import hash_password
class MyTestHashPassword(unittest.TestCase):
    def test_hash_password_correctness(self):
        password = "123"
        expected_hash = hashlib.sha256(password.encode()).hexdigest()
        hashed_password = hash_password(password)
        self.assertEqual(hashed_password, expected_hash)
    def test_hash_password_different_lengths(self):
        # Test with different input lengths
        passwords = [
            "short",
            "a" * 100,  # A very long password
            "password_with_special_characters_!@#$%^&*()"
        ]
        for password in passwords:
            hashed_password = hash_password(password)
            self.assertIsNotNone(hashed_password)
if __name__ == '__main__':
    unittest.main()
