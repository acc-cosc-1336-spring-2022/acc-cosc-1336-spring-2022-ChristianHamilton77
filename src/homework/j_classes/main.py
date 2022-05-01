#
import class_b
c = class_b.die()
#print(c.get_rolled_value())
menu = "\nPlease make a selection:\n1-Roll The die\n2-Exit\n"
# print(menu)
choice = 0

while choice != 2:
    choice = int(input(menu))
    if choice == 1:
        print("\n")
        print(c._str_)
        print(c.get_rolled_value())