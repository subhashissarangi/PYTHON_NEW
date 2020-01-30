'''
Created on 30-Jan-2020

@author: SUBHASHIS
'''
from iterators.Reverse import Reverse
if __name__ == '__main__':
    pass

    lst = [34, 978, 42]
    lst_backwards = Reverse(lst)
    for el in lst_backwards:
        print(el)