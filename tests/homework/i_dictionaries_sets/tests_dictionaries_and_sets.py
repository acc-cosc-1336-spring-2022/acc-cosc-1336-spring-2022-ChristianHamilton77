#
import unittest
from src.homework.i_dictionaries_sets.dictionary import remove_inventory_widget
from src.homework.i_dictionaries_sets.dictionary import add_inventory

class Test_Config(unittest.TestCase):
    def test_add_inventory(self):
        inventory_dictionary = {}
        widget = "widget1"
        self.assertEqual({"widget1":10},add_inventory(inventory_dictionary,widget,10))
        self.assertEqual({"widget1":35},add_inventory(inventory_dictionary,widget,25))
        self.assertEqual({"widget1":25},add_inventory(inventory_dictionary,widget,-10))

    def test_remove_inventory_widget(self):
        dict = {}
        w1 = "widget1"
        w2 = "widget2"
        add_inventory(dict,w1,5)
        self.assertEqual(5,dict["widget1"])
        add_inventory(dict,w2,15)
        self.assertEqual(15,dict["widget2"])
        
        remove_inventory_widget(dict,w1)
        self.assertEqual(len(dict),1)
        self.assertEqual(dict["widget2"],15)