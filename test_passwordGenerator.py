import unittest
from passwordGenerator import PasswordGenerator
import string

class TestPasswordGenerator(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.pg = PasswordGenerator()
    
    def test_generate_password(self):
        self.pg.generate_password()
        length = self.pg.length
        print(self.pg.pw)
        self.assertEqual(length, len(self.pg.pw))

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
        self.pg.add_characters(self.pg.SPECIAL)
        characters = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        self.assertIn(characters, self.pg.characters)

    def test_default_source__string(self):
        source = self.pg.get_source_string()
        self.assertEqual('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', source)

    
if __name__ == '__main__':
    unittest.main()
