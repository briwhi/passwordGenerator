import unittest
from passwordGenerator import PasswordGenerator

class TestPasswordGenerator(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.pg = PasswordGenerator()
    
    def test_addPassword(self):
        self.pg.add_password("newPassword")


if __name__ == '__main__':
    unittest.main()
