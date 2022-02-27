#
import repetition

#print(repetition.sum_odd_numbers(9))
#print(repetition.get_factorial(4))


#/////// ~f
def dblChk(run,message):
    while run == True:
        #print('run = ',run,"\n")
        display = input(message)
        #validate
        if display == 'y' or display == 'Y' or display == 'n' or display == 'N':
            if display == 'N' or display == 'n':
                menu_call(True)
                run = False
            else:
                run = False
                break
        else:
            print('Please enter either Y or N. ')
            run = True

#Define Menu
def menu_call(menu_run):
    #print('Menu_run = ',menu_run,"\n")
    while menu_run == True:
        menu = input("Homework 3 Menu \n 1-Factorial \n 2-Sum odd numbers \n 3-Exit \n")
        #validate input
        # !is Number -> Error message --> Call Menu
        if menu.isnumeric():    
            #is Number
            #convert Number to int
            menu_choice = int(menu)
           
            if menu_choice >=1 and menu_choice <= 3:#is between 1 & 3 -> NEXT
                menu_run = False 
                #print('Menu_run = ',menu_run,"\n")     
            else:#!is between 1-3 -> error message -->Call Menu
                print('Please Select a Number between 1 and 3.\n')
                menu_run = True
        else:
            print('Please Select a Number.\n')
            menu_run = True
    #print('menu_choice = ',menu_choice," \n")
    #if Selector
    selector_filter(menu_choice)


def selector_filter(menu_choice):
    # is 3
        #db chk - input('are you sure you wouldlike to exit? ')
    if menu_choice == 1 or menu_choice == 2:#is 1 or 2 - > Prompt for number to use in ~f
        num = input('Enter a number to process.\n')
        #vaidate Response
        if num.isnumeric():#is Number  
            num_choice = int(num)#convert Number to int
            #print(num_choice)
            #if choice is 1
            if menu_choice == 1:
                #is between 0 & 10 -> NEXT
                if num_choice >= 0 and num_choice <= 10:
                    print(repetition.get_factorial(num_choice))#call ~f get_factorial
                    dblChk(True, 'Do you want to exit? ')
                    #!is between 0 & 10 -> error message -->Call Menu
                elif num_choice > 10:
                    print('Please select a Number between 0 and 10.\n')
                    menu_call(True)

            #if choice is 2
            elif menu_choice == 2:
                #is between 0 & 100 -> NEXT
                if num_choice >= 0 and num_choice <= 100:
                    print(repetition.sum_odd_numbers(num_choice))#call ~f Sum_odd_numbers
                    dblChk(True, 'Do you want to exit? ')
                    #!is between 0 & 100 -> error message -->Call Menu
                elif num_choice > 100:
                    print('Please select a Number between 0 and 100.\n')
                    menu_call(True)

        # !is Number -> Error message --> Call Menu
        else:
            print('Please Select a Number.\n')
            menu_call(True)
    if menu_choice == 3:
        dblChk(True,'Are you sure you want to exit? ')
    # else:
    #     print('idk how this happened.')

        
        
        


#/////// main prog
#Call menu
menu_call(True)

   

   


