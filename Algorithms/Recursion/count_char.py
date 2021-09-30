def count_c(str, letter):
    """Count the number of specified letters in a string"""
    global count
    if len(str) > 0:
        if str[-1:] == letter:
            count += 1
        str =str[:-1]
        count_c (str,letter)
    
    return count

count = 0
str = 'adbcddd'
letter = 'd'
print(count_c(str, letter))