import unittest
from passwordlock import User


class TestClass(unittest.TestCase):
    """
        A Test class that defines test cases for the User class.
    """

    def setUp(self):
        """
        Method that runs before each individual test methods run.
        """
        self.new_user = User('IanSang', 'Is24446666668888888')
