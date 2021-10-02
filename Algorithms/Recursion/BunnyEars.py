def ear_count(n):
    '''We have bunnies standing in a line, numbered 1, 2, ... 
    The odd bunnies (1, 3, ..) have the normal 2 ears. The 
    even bunnies (2, 4, ..) we'll say have 3 ears, because 
    they each have a raised foot. Recursively return the 
    number of "ears" in the bunny line 1, 2, ... n (without 
    loops or multiplication).'''

    global ears

    if n >= 1:
        if n % 2 == 0:
            ears += 3
        else:
            ears += 2
        n -= 1
        ear_count(n)
    
    return ears

ears = 0
n = 10
print(ear_count(n))
