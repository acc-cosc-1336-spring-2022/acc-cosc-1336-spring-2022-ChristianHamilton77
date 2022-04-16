def add_inventory(widgets,widget_name,quantity):
    #print('')
    quantity = int(quantity)
    
    if widget_name in widgets:
        widgets[widget_name] += quantity
    else:
        widgets[widget_name] = quantity
    return widgets
def remove_inventory_widget(widgets,widget_name):
    # print('')
    if widget_name in widgets:
        # print('Dictionary Widget found.')
        del widgets[widget_name]
    # else:
    #     print('Sorry the Widget Name was not found in the Dictionary.')

# dict = {"newsfeed":1,"recentOrder":4}
# print(dict,"/n")

# add_inventory(dict,"newProduct",3)
# print(dict,"/n")

# remove_inventory_widget(dict,"newProduct")
# print(dict,"/n")

# remove_inventory_widget(dict,"newProduct")
# print(dict,"/n")