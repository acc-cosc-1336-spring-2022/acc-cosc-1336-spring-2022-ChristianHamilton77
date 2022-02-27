import unittest

from src.examples.d_repetition.repetition import test_config
from src.examples.d_repetition.repetition import display_number
from src.examples.d_repetition.repetition import sum_of_squares

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    #def test_display_number(self):
     #   self.assertTrue()

    def test_sum_of_squares(self):
        self.assertEqual(14, sum_of_squares(3))