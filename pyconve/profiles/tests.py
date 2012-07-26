from django.test import TestCase
from django.test.client import Client


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class NewProfileTest(TestCase):
    def setUp(self):
        self.client = Client()
    

    def test__new_user(self):
        pass
