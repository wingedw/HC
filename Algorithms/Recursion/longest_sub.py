def longest_sub(str, sub):
    '''Given a string and a non-empty substring sub, compute recursively the 
    largest substring which starts and ends with sub and return its length.'''
    global first
    global last
    global count
    length = len(sub)

    if sub in str[first + last:]:
        if count == 0:
            first =  str.find(sub)
            last = first
            count += 1
        else:
            last = last+length + str[last+length:].find(sub)
        longest_sub(str,sub)
        if count == 0:
            return 0
        else:
            return last - first + length



first, last, count = 0, 0, 0
str = 'xxcatcatdogcatcowcatdog'
sub = 'cat'

print(longest_sub(str, sub))
