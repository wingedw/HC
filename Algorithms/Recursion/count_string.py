def strcount(str, sub):
    '''Count the number of occurances of substring in string using recursion'''
    '''when str.count is too easy'''
    global count
    right = len(sub)
    if sub in str:
        left = str.find(sub)
        count += 1
        str = str[left+right:]
        strcount(str, sub)
    
    return count


count = 0
str = 'cowcatcowcat'
sub = 'cat'
print(strcount(str,sub))