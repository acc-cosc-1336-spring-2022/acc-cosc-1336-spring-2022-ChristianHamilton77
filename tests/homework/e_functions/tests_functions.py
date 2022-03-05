#
import unittest
from src.homework.e_functions.value_return import get_hour
from src.homework.e_functions.value_return import get_minutes
from src.homework.e_functions.value_return import get_seconds
from src.homework.e_functions.value_return import time_from_utc

class Test_Config(unittest.TestCase):

# After the line that begins with class write a test case function test_get_hour
    def test_get_hour(self):# Test that get_hour with parameter value 3800 returns the value 1.
        self.assertEqual(get_hour(3800),1)

    def test_get_hour_2(self):# Test that get_hour with parameter value 3600 returns the value 1.
        self.assertEqual(get_hour(3600),1)

# Test case function test_get_minutes
    def test_get_minutes(self):# Test that get_minutes with parameter value 3800 returns the value 3.
        self.assertEqual(get_minutes(3800), 3)
    
    def test_get_minutes_2(self):# Test that get_minutes with parameter value 3600 returns the value 0.
        self.assertEqual(get_minutes(3600), 0)

# Test case function test_get_seconds
    def test_get_seconds(self):# Test that get_seconds with parameter value 3800 returns the value 20.
        self.assertEqual(get_seconds(3800),20)
        
    def test_get_seconds_2(self):# Test that get_seconds with parameter value 3600 returns the value 0.
        self.assertEqual(get_seconds(3600),0)

# Test case function test_utc_time_to_eastern_standard_time
    def test_utc_time_to_eastern_standard_time(self):# Test that time_from_utc with parameters -5 and 20 returns 15
        self.assertEqual(time_from_utc(-5,20),15)

# Test case function test_utc_time_to_central_standard_time
    def test_utc_time_to_central_standard_time(self):
        self.assertEqual(time_from_utc(-6,20),14)# Test that time_from_utc with parameters -6 and 20 returns 14

# Test case function test_utc_time_to_mountain_standard_time
    def test_utc_time_to_mountain_standard_time(self):
        self.assertEqual(time_from_utc(-7,20),13)# Test that time_from_utc with parameters -7 and 20 returns 13

# Test case function test_utc_time_to_pacific_standard_time
    def test_utc_time_to_pacific_standard_time(self):
        self.assertEqual(time_from_utc(-8,20),12)# Test that time_from_utc with parameters -8 and 20 returns 12