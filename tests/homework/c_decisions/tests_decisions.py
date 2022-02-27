import unittest

from src.homework.c_decisions.decisions import get_options_ratio
from src.homework.c_decisions.decisions import get_faculty_rating

class Test_Config(unittest.TestCase):
    # After the line that begins with class write a test case function for the get_options_ratio function (Use the homework 1 as a guide to write the test case).
    # Test that get_options_ration with values 5 and 20 returns the value .25.
    def test_get_options_ratio(self):
        self.assertEqual(0.25, get_options_ratio(5,20))
    # Test that get_options_ration with values 10 and 20 returns the value .5.
    def test_get_options_ratio(self):
        self.assertEqual(0.5, get_options_ratio(10,20))

    # Write a test case for the get_faculty_rating.
    # Test that the function returns ‘Excellent’ when the rating is .91.
    def test_get_faculty_rating(self):
        self.assertEqual('Excellent', get_faculty_rating(4.55,5))
    # Test that the function returns ‘Very Good’ when the rating is .85.
    def test_get_faculty_rating(self):
        self.assertEqual('Very Good', get_faculty_rating(4.25,5))
    # Test that the function returns ‘Good’ when the rating is .71.
    def test_get_faculty_rating(self):
        self.assertEqual('Good', get_faculty_rating(3.55,5))
    # Test that the function returns ‘Needs Improvement’ when the rating is .66.
    def test_get_faculty_rating(self):
        self.assertEqual('Needs Improvement', get_faculty_rating(3.3,5))
    # Test that the function returns ‘Unacceptable’ when the rating is .45.
    def test_get_faculty_rating(self):
        self.assertEqual('Unacceptable', get_faculty_rating(2.25,5))
