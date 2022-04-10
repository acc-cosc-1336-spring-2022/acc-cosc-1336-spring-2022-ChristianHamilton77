#main program
import lists
list1 = ["c++","Python","PHP"]
item1 = "PHP"
result = lists.find_item_in_list(item1,list1)

if result:
    print("it's in the list.")
else:
    print("it's not in the list")