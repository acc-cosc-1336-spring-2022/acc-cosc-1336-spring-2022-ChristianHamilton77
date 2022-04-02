# 1-Hamming Distance
# 2-Dna Complement
# 3-Exit
import strings
menu = '\n\n Choose a number to select a menu item: \n 1-Hamming Distance\n 2-Dna Complement\n 3-Exit\n'
#print(menu)
choice = 0
while choice != 3:
    choice = input(menu)
    choice = int(choice)
    #print(choice)
    if choice == 1:
        dna1 = input('Input the first string of DNA to check the Hamming Distance:')
        dna2 =   input('Input the second string of DNA to check the Hamming Distance:')
        print('The Hamming Distance is', strings.get_hamming_distance(dna1,dna2))
    elif choice == 2:
        dna = input('Input the DNA sequence to check for the complement pair:')
        print('The DNA sequence pair for', dna, 'is', strings.get_dna_complement(dna))
