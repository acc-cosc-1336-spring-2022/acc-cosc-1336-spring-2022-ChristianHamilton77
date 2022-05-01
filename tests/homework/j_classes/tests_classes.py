import unittest
from src.homework.j_classes.class_b import die

class Test_Config(unittest.TestCase):

    def testRollDie_1(self):
        c = die()
        self.assertGreater(c.get_rolled_value(),0)
        self.assertLess(c.get_rolled_value(),7)

    def testRollDie_2(self):
        c = die()
        self.assertGreater(c.get_rolled_value(),0)
        self.assertLess(c.get_rolled_value(),7)\

    def testRollDie_3(self):
        c = die()
        self.assertGreater(c.get_rolled_value(),0)
        self.assertLess(c.get_rolled_value(),7)