import unittest

from src.examples.g_lists_and_tuples.lists import test_config
from src.examples.g_lists_and_tuples.lists import find_item_in_list
class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_find_item(self):
        list1 = ["c++","Python","PHP"]
        self.assertEqual(True,find_item_in_list("PHP",list1))
