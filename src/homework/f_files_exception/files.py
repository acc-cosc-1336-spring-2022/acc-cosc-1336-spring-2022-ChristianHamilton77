#
import json

def writeFile(textToAdd,method):
    dataFile = open('data.txt',method) #open data File in Write or append mode Mode
    for key, value in textToAdd.items():#add the text
        dataFile.write(key + '\n')
        dataFile.write(str(value) + '\n')

    dataFile.close() #close File

def writeDataFile(textToAdd,method):# method to be "w" or "a"
    if method == "w" or method == "W":
        method == "w"
        writeFile(textToAdd,method)
    elif method == "a" or method == "A":
        method == "a"
        writeFile(textToAdd,method)
    else:
        print("method must be a w (write) or a (append)")

def readFile():
    # dataFile = open('data.txt', 'r') #open data File in read mode
    # data = dataFile.readlines() #read whole file to a string
    # dataFile.close() #close File
    # print(data)

    dataFile = open('data.txt', 'r') 
    dataFileItem = dataFile.readline()
    while dataFileItem != '': # read and display lines
        DataFileItemValue = dataFile.readline()
        dataFileItem = dataFile.readline()
        dict += "dataFileItem.rstrip('\n'):DataFileItemValue.rstrip('\n')"
    dataFile.close

# test = "newsfeed"
# writeDataFile(test,"a")
# readFile()

def add_inventory(widgets,widget_name,quantity):
    #print('')
    quantity = int(quantity)#make input an int
    
    if widget_name in widgets:
        widgets[widget_name] += quantity
    else:
        widgets[widget_name] = quantity
    writeDataFile(widgets,"w")
    return widgets
def remove_inventory_widget(widgets,widget_name):
    # print('')
    if widget_name in widgets:
        # print('Dictionary Widget found.')
        del widgets[widget_name]
    writeDataFile(widgets,"w")
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