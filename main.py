import secrets
import string

class PasswordGenerator:
    def __init__(self, pw_length=12, min_digits=2, min_special_chars=1): # Adjust the values to your liking
        self.pw_length = pw_length
        self.min_digits = min_digits
        self.min_special_chars = min_special_chars

        self.letters = string.ascii_letters
        self.digits = string.digits
        self.special_chars = string.punctuation
        self.alphabet = self.letters + self.digits + self.special_chars

    def generate(self):
        password = ''
        while not self.is_strong(password):
            password = ''.join(secrets.choice(self.alphabet) for _ in range(self.pw_length))
        return password

    def is_strong(self, password):
        if (sum(char in self.special_chars for char in password) >= self.min_special_chars and
                sum(char in self.digits for char in password) >= self.min_digits):
            return True
        return False

if __name__ == '__main__':
    generator = PasswordGenerator()
    print(generator.generate())