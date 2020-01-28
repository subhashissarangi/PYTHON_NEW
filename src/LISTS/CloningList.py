'''
Created on 26-Jan-2020

@author: SUBHASHIS
'''

if __name__ == '__main__':
    pass

x = 3
y = x
print(id(x), id(y))


y = 4
print(id(x), id(y))
colours1 = ["red", "blue"]
colours2 = colours1
print(id(colours1),id(colours2))

colours2[1] = "green"
print(id(colours1),id(colours2))
print(colours1)
print(colours2)

list1 = ['a','b','c','d']
list2 = list1[:]
list2[1] = 'x'
print(list2)
print(list1)


lst1 = ['a','b',['ab','ba']]
lst2 = lst1[:]
lst2[0] = 'c'
print(lst1)
print(lst2)


lst2[2][1] = 'd'
print(lst1)
print(lst2)

from copy import deepcopy

lst1 = ['a','b',['ab','ba']]
lst2 = deepcopy(lst1)
lst1
lst2
id(lst1)
id(lst2)

lst2[2][1] = "d"
lst2[0] = "c"
print(lst1)
print(lst2)





















