'''
Created on 29-Jan-2020

@author: SUBHASHIS
'''

class LoopPractices(object):
    
    n = 100
    s = 0
    counter = 1
    def __init__(self,params,n,s,counter):
        self.n=n
        self.s=s
        self.counter=counter
        
        
def sumOfNumbers(self):
    n = 100
    s = 0
    counter = 1
    while counter <= n:
        s = s + counter
        counter += 1
    print("Sum of 1 until %d: %d" % (n,s))
    
    print(sumOfNumbers())
    