from operator import truediv
import unittest

from src.examples.c_decisions.decisions import test_config
from src.examples.c_decisions.decisions import is_even
from src.examples.c_decisions.decisions import get_letter_grade

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_and_truth_table(self):
        self.assertEqual(True and True, True)
        self.assertEqual(True and False, False)
        self.assertEqual(False and True, False)
        self.assertEqual(False and False, False)

    def test_or_truth_table(self):
        self.assertEqual(True or True, True)
        self.assertEqual(True or False, True)
        self.assertEqual(False or True, True)
        self.assertEqual(False or False, False)

    def test_is_even(self):
        #self.assertEqual(True, iS_even(5))
        self.assertEqual(True, is_even(4))

    def test_get_letter_grade(self):
        self.assertEqual('A',get_letter_grade(95))