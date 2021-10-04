def changePI(str, pi = "3.14", pi_c = "pi"):
    if pi_c in str:
        str = str.replace(pi_c, pi)
    return str

def changePI_rec(str, pi = "3.14", pi_c = "pi"):
    '''Given a string, compute recursively (no loops) a new string where
    all appearances of "pi" have been replaced by "3.14".'''
    if pi_c in str:
        left = str.find(pi_c)
        str = changePI_rec(str[:left] + pi + str[left + len(pi_c):])
    return str

str= 'xpixxxpixxpipixx'
print (changePI_rec(str))
