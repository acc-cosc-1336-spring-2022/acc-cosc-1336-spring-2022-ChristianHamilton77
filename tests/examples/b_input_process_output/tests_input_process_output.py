import unittest

from src.examples.b_input_proc_output.input_process_output import test_config
from src.examples.b_input_proc_output.input_process_output import multiply_numbers
from src.examples.b_input_proc_output.input_process_output import integer_division
from src.examples.b_input_proc_output.input_process_output import float_division
from src.examples.b_input_proc_output.input_process_output import operator_procedure
from src.examples.b_input_proc_output.input_process_output import expo_me
from src.examples.b_input_proc_output.input_process_output import get_remain

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_multiply_numbers(self):
        self.assertEqual(25, multiply_numbers(5,5))

    def test_integer_division_1(self):
        self.assertEqual(1,integer_division(5,5))
        #self.assertEqual(2,integer_division(6,2))

    def test_float_division(self):
        self.assertEqual(2.5,float_division(5,2))

    def test_operator_procedure(self):
        self.assertEqual(1,operator_procedure(2,3,5))

    def test_expo_me(self):
        self.assertEqual(3136,expo_me(56,2))

    def test_get_remain(self):
        self.assertEqual(1,get_remain(5,2))