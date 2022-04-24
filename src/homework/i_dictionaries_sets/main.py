import dictionary

menu = "\nPlease make a selection:\n1-Add or Update Item\n2-Delete Item\n3-Exit\n"
# print(menu)
dict = {}
choice = 0
while choice != 3:
    try:
        choice = int(input(menu))
    except ValueError:
        choice = 0

    if choice == 1:
        dataName = input('Enter an item name to add or edit.\n')
        value = dict.get(dataName)
        if value:
            dataValue = input(dataName + ' is in the dictionary, enter the number value to add to ' + dataName + '.\n')
            dictionary.add_inventory(dict,dataName,dataValue)
            print('\n' + dataName + ':' + dataValue + ' has been added to the dictionary.\n')
            #print(dict)
        else:
            dataValue = input(dataName + ' was not found in the dictionary, enter the number value to add to ' + dataName + '.\n')
            dictionary.add_inventory(dict,dataName,dataValue)
            print('\n' + dataName + ':' + dataValue + ' has been added to the dictionary.\n')
           # print(dict)
    if choice == 2:
        dataName = input('Enter an item name to delete.\n')
        value = dict.get(dataName)
        if value:
            dictionary.remove_inventory_widget(dict,dataName)
            print('\n' + dataName + ' has been removed from the dictionary.\n')
        else:
            print(dataName + ' was not found in the dictionary.\n')