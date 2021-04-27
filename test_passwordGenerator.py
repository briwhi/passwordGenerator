import unittest
from passwordGenerator import PasswordGenerator
import string

class TestPasswordGenerator(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.pg = PasswordGenerator()

    def test_default_password_length(self):
        pw = self.pg.generate_password()
        length = len(pw)
        self.assertEqual(10, length)

    def test_get_password_length_15(self):
        pw = self.pg.generate_password(15)
        length = len(pw)
        self.assertEqual(15, length)





    """


    

    def test_add_characters(self):
        self.pg.add_characters(self.pg.SPECIAL)
        characters = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        self.assertIn(characters, self.pg.characters)

    def test_default_source__string(self):
        source = self.pg.get_source_string()
        self.assertEqual('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', source)

    """

if __name__ == '__main__':
    unittest.main()
