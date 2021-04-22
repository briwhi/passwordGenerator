import string

class PasswordGenerator:
    LOWERCASE = string.ascii_lowercase
    UPPERCASE = string.ascii_uppercase
    NUMBERS = "".join([str(i) for i in range(0,10)])


    def __init__(self):
        self.pw = "password"
        self.length = 10
        self.characters = [self.LOWERCASE, self.UPPERCASE, self.NUMBERS]

    def generate_password(self):
        pass

    def get_password(self):
        return self.pw

    def set_password_length(self, length):
        self.length = length

    def add_characters(self, character_type):
        self.characters.append(character_type)

    def get_source_string(self):
        source_string = ""
        for s in self.characters:
            source_string.join(s)
        return source_string