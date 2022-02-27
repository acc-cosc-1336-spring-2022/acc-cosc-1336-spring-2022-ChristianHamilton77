def test_config():
    return True

def is_even(num):
    return num % 2 == 0 # boolean expression, why? it returns true or false

def get_letter_grade(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 85:
        return 'B'
    elif grade >= 80:
        return 'C'
    elif grade >= 70:
        return 'D'
    elif grade <= 69:
        return 'F'
