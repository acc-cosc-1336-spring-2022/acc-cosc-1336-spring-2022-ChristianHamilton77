#
import unittest
from src.homework.i_dictionaries_sets.dictionary import get_p_distance
from src.homework.i_dictionaries_sets.dictionary import get_p_distance_matrix

class Test_Config(unittest.TestCase):
    # After the line that begins with class write a test case function test_p_distance
    # Test that get_p_distance with parameter values ['T','T','T','C','C','A','T','T','T','A'] and ['G','A','T','T','C','A','T','T','T','C'] that returns .4 .
    
    def test_p_distance(self):
        list1 = ['T','T','T','C','C','A','T','T','T','A']
        list2 = ['G','A','T','T','C','A','T','T','T','C']
        self.assertEqual(get_p_distance(list1,list2),4)

    def test_get_p_distance_matrix(self):
        dataSet = [['T','T','T','C','C','A','T','T','T','A'],['G','A','T','T','C','A','T','T','T','C'],['T','T','T','C','C','A','T','T','T','T'],['G','T','T','C','C','A','T','T','T','A']]
        result = [[0.0, 0.4, 0.1, 0.1],[0.4, 0.0, 0.4, 0.3],[0.1, 0.4, 0.0, 0.2],[0.1, 0.3, 0.2, 0.0]]
        self.assertEqual(get_p_distance_matrix(dataSet),result)