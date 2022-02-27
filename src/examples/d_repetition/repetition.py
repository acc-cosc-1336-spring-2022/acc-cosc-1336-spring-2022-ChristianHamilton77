def test_config():
    return True

def display_number(num):
    cnt=0
    while cnt < num:
        print(cnt + 1)
        cnt = cnt + 1

#display_number(100)

def sum_of_squares(num): #1*1 + 2*2 + 3*3 = 14
    cnt = 0
    sum = 0
    while cnt <= num:
        sum = sum + cnt ** 2
        cnt += 1
        print(sum)

def promt_user():
    keep_going = 'Y'
    keep_going = input('Do you want to Loop again?')

def for_intro_loop():
    for num in [1,2,3,4,5]:
        print(num)

def for_intro_loop_str():
    for name in ['winken', 'linkin', 'nod']:
        print(name)

def for_num_range(val):
    for num in range(val):
        print(num)

def for_num_range_start_value(num, num1):
    for val in range(num, num1):
        print(val)

def for_num_range_with_step(num,num1,num2):
    for val in range(num,num1,num2):
        print(val)

def for_display_sum_of_squares(num,num1):
    for val in range(num, num1):
        square = val**2
        print(val, '\t', square)