'''
Created on 31-Jan-2020

@author: SUBHASHIS
'''
from builtins import object
from pip._internal.utils.outdated import SELFCHECK_DATE_FMT

class Fibonacci(object):

         def  __init__(self) :
          pass

n=int(input("please anter a number to get fibonacci: "))

def fib(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                return fib(n-1) + fib(n-2)
    
def fibi(n):
    old, new = 0, 1
    if n == 0:
        return 0
    for i in range(n-1):
        old, new = new, old + new
    return new

print(fib(n))
print(fibi(n))


    
    