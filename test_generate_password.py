import unittest
import string
from generate_password import generate_password

class TestPasswordGenerator(unittest.TestCase):
    
    def test_password_length(self):
        length = 12
        special_chars_count = 3
        password = generate_password(length, special_chars_count)
        self.assertEqual(len(password), length)
        
    def test_special_characters_count(self):
        length = 12
        special_chars_count = 3
        password = generate_password(length, special_chars_count)
        special_chars = [char for char in password if char in string.punctuation]
        self.assertEqual(len(special_chars), special_chars_count)
        
    def test_randomness(self):
        length = 12
        special_chars_count = 3
        passwords = set(generate_password(length, special_chars_count) for _ in range(1000))
        self.assertGreater(len(passwords), 900)

if __name__ == '__main__':
    unittest.main()
