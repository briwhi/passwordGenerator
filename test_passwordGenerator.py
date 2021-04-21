import unittest
from passwordGenerator import PasswordGenerator
import string

class TestPasswordGenerator(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.pg = PasswordGenerator()
    
    def test_generate_password(self):
        self.pg.generate_password()

    def test_get_password(self):
        pw = self.pg.get_password()
        self.assertEqual("password", pw)

    def test_set_password_length(self):
        self.pg.set_password_length(12)
        length = self.pg.length
        self.assertEqual(12, length)

    def test_default_password_length(self):
        length = self.pg.length
        self.assertEqual(10, length)

    def test_add_characters(self):
        self.pg.add_characters(self.pg.LOWERCASE)
        characters = string.ascii_lowercase
        self.assertIn(characters, self.pg.characters)
        

if __name__ == '__main__':
    unittest.main()
