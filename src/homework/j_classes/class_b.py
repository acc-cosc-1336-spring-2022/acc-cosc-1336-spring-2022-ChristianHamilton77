# rite a class named die, with no constructor.
# public functions:
# roll()—use random to generate a value from 1 to 6, save value to roll_value
# get_rolled_value()—return the roll_value
# __str__ --write code to output: “The rolled value is “ whatever roll_value is
# private data:
# roll_value

import random


class die:
    #Privy
    def  __roll_value(self):
        return die.roll(self)
        
    # Public
    def roll(self):
        x = random.randint(1,6)
        return x

    def get_rolled_value(self):
        return die.__roll_value(self)

    _str_ = "The rolled value is: " 

