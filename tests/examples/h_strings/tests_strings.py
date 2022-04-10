import unittest

from src.examples.h_strings.strings import test_config
from src.examples.h_strings.strings import concat_strings

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_concat(self):
        self.assertEqual(concat_strings("Hello ","World"),"Hello World")

    def test_str_rep(self):
        str = "w" * 5
        self.assertEqual(str,"wwwww")