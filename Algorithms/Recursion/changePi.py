def changePI(str = "pipi", pi = "3.14", pi_c = "pi"):
    return str.replace(pi_c, pi)

def changePI_rec(str, pi_c = "pi", pi = "3.14"):
    '''Given a string, compute recursively (no loops) a new string where
    all appearances of "pi" have been replaced by "3.14".'''
    if pi_c in str:
        left = str.find(pi_c)
        str = changePI_rec(str[:left] + pi + str[left + len(pi_c):])
    return str

str= 'xpixxxpixxpipixx'
print (changePI(str))
print (changePI_rec(str))
