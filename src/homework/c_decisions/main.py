import decisions

option = float(input('Enter Faculty Rating: '))
totalStmt = 'You entered '+ str(option) + '; Out of how many ? '
total = float(input(totalStmt))
#print(option,total)

decisions.get_options_ratio(option,total)
# print(decisions.get_options_ratio(option,total))
res = decisions.get_options_ratio(option,total)
#print(res)

print('The Faculty Rating is',decisions.get_faculty_rating(res))
