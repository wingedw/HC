
def count_digit(num, digit):
    '''Count the number of occurrances of a specified digit in a number'''
    global count

    if num > 0:
        if num % 10 == digit:
            count += 1
        count_digit(num//10,digit)
    return count

count = 0
num = 1717777777777
digit = 7
print (count_digit(num,digit))