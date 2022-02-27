import decisions
#num = int(input('Enter a number:'))
#if(decisions.is_even(num)):
#    print(num, 'is Even.')
#else:
 #   print(num, 'is odd.')

grade = input("What was your score?")
grade = int(grade)
print(decisions.get_letter_grade(grade))