import unittest
import passwordvalidator

class TestPasswordValidator(unittest.TestCase):

    def test_that_password_validator_function_exists(self):
        passwordvalidator.strong_password("strong")

    def test_strong_password(self):
        self.assertTrue(passwordvalidator.strong_password("password1234"))


    def test_short_password_are_invalid(self):
        self.assertFalse(passwordvalidator.strong_password("pass"))
