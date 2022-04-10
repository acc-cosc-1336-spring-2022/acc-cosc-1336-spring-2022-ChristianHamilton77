def test_config():
    return True

def local_var():
    val = 0
    return val
    
def main():
    val = 0
    local_var()

import random

def get_random(min,max):#user defined funct, using a python library function.
    return random.randint(min,max)

random.seed(10)#Sets the start point for the random generator.

def display_random(min,max,cnt):

    for i in range(cnt):
        print(random.randint(min,max))

def return_f_l_name():
    return "joe","cool"