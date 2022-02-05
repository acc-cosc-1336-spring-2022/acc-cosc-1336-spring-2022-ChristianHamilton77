import unittest

from src.examples.b_input_proc_output.input_process_output import test_config
from src.examples.b_input_proc_output.input_process_output import multiply_numbers

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_multiply_numbers(self):
        self.assertEqual(25, multiply_numbers(5,5))