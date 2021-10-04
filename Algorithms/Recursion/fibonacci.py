def calc_fib(n):
    print(f'Calculate the Fibonacci of {n}')
    if n < 2:
        return 1
    else: 
        return calc_fib(n-1) + calc_fib(n-2)

############################################
# f= 30 #
# 4201.822812795639  -  0.008000850677490234  =  4201.814811944962
from functools import lru_cache

@lru_cache
def calc_fib2(n):
    print(f'Calculate the Fibonacci (cache) of {n}')
    if n < 2:
        return 1
    else: 
        return calc_fib2(n-1) + calc_fib2(n-2)

import time

n = 30
t1a = time.time()
print(calc_fib(n))
t1b = time.time()
d1 = t1b - t1a

t2a = time.time()
print(calc_fib2(n))
t2b = time.time()
d2 = t2b - t2a

print (d1, ' - ', d2, ' = ', d1 - d2)
