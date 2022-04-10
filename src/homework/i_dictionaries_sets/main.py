#
from tkinter import Y
import dictionary
# write code to create the following menu.

# 1-Get p distance matrix
# 2-Exit

# The program runs until the user chooses option 2

# Option 1 prompt the user for a list, call the get_p_distance_matrix function and display the result.

menu = "\n 1-Get p distance matrix\n 2-Exit: \n"
option = 0
while option != 2:
    o = int(input(menu))
    option = o
    if o == 1:
        k = 'y'
        t= 0
        list1 = []
        # number of elements as input
        n = int(input("\nEnter number of elements in the lists: "))
        while k == 'y' or k == 'Y':
            l = []
            # iterating till the range
            print("\n")
            for i in range(0, n):
                ele = input('Enter the items in the list one by one: ')
                l.append(ele) # add the element

            #l = [item for item in input("Enter the list items with a space between each item: ").split()]
            print(l)
            list1.append(l)
            if t > 0:
                k = input('\nEnter another list?\n "y" for yes\n "n" for no.\n')
            t += 1
        # print(list1)
        result =  dictionary.get_p_distance_matrix(list1)
        print("P Distance Matrix is : ",result)
