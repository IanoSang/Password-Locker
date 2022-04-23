import unittest
from passwordlock import User
from passwordlock import Credentials


class TestClass(unittest.TestCase):
    """
        A Test class that defines test cases for the User class.
    """

    def setUp(self):
        """
        Method that runs before each individual test methods run.
        """
        self.new_user = User('IanSang', 'Is24446666668888888')

    def test_init(self):
        """
        test case to check if the object has been initialized correctly
        """
        self.assertEqual(self.new_user.username, 'IanSang')
        self.assertEqual(self.new_user.password, 'Is24446666668888888')

    def test_save_user(self):
        """
        test case to test if a new user instance has been saved into the User list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)


class TestCredentials(unittest.TestCase):
    """
    A test class that defines test cases for credentials class
    """


if __name__ == "__main__":
    unittest.main()
