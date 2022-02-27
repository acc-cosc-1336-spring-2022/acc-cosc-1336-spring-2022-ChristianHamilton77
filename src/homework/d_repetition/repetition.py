#

def get_factorial(num):
    fact = 0
    for n in range(num,1,-1):##make neg step here
        #print(n)
        if fact == 0:
            fact = n
            #print(fact)
        else:
            fact = fact * n
            #print(fact)
    
    #print('--',fact)
    return fact


def sum_odd_numbers(num):
    count = 0
    sum_odd = 0
    while count <= num:
        testNum =  count % 2
        if testNum != 0:
            sum_odd += count
        count += 1

    return sum_odd

#print('Sum odd : ',sum_odd_numbers(7))
