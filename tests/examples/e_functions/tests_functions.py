import unittest

from src.examples.e_functions.value_return_functions import test_config
from src.examples.e_functions.value_return_functions import get_random
class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_get_random_num(self):
        rand = get_random(1,100)
        flag = rand >= 1 and rand <= 100
        self.assertEqual(flag, True)
        # self.assertGreaterEqual(rand,1)
        # self.assertLessEqual(rand,100)    