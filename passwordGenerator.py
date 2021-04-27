import string
from random import randint

class PasswordGenerator:
    LOWERCASE = string.ascii_lowercase
    UPPERCASE = string.ascii_uppercase
    NUMBERS = "".join([str(i) for i in range(0,10)])
    SPECIAL = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"



    def __init__(self):
        self.pw = "password"
        self.characters = [self.LOWERCASE, self.UPPERCASE, self.NUMBERS]
        self.source_string = ""

    def generate_password(self, length=10):
        self.pw = ""
        for x in range(length):
            i = randint(0, len(self.characters)-1)
            char = self.get_source_string()[i]
            self.pw += char
        return self.pw

    def get_password(self):
        return self.pw

    def set_password_length(self, length):
        self.length = length

    def add_characters(self, character_type):
        self.characters.append(character_type)

    def get_source_string(self):
        self.source_string = "".join(self.characters)
        return self.source_string
        


