'''
Created on 30-Jan-2020

@author: SUBHASHIS
'''

class PythogorianTheorem(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
     
    '''
     if a2+b2=c2 means if a square plus b square is equal to c square then that number is called pythogorian number
    '''   
    from math import sqrt
    n = int(input("Maximal Number? "))
    for a in range(1,n+1):
     for b in range(a,n):
        c_square = a**2 + b**2
        c = int(sqrt(c_square))
        if ((c_square - c**2) == 0):
           print(a, b, c)
           
           
           
    