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

def ear_count_inductive(n):
		if n == 0: return 0
		if n % 2 == 0:   # even
				return ear_count_inductive(n - 1) + 3
		else:	# odd
				return ear_count_inductive(n - 1) + 2

import time
ears = 0
n = 800

t2a = time.time()
print(ear_count_inductive(n))
t2b = time.time()
print(t2b-t2a)

t1a = time.time()
print(ear_count(n))
t1b = time.time()
print(t1b-t1a)


