'''
Created on 30-Jan-2020

@author: SUBHASHIS
'''
'''
In one perspective they are the same: You can iterate with a for loop over iterators and iterables. Every iterator is also an
iterable, but not every iterable is an iterator. E.g. a list is iterable but a list is not an iterator! An iterator can be created
from an iterable by using the function 'iter'. To make this possible the class of an object needs either a method '__iter__',
which returns an iterator, or a '__getitem__' method with sequential indexes starting with 0.
'''


if __name__ == '__main__':
    pass



for city in ["Berlin", "Vienna", "Zurich"]: # list
    print(city)
for city in ("Python", "Perl", "Ruby"): # tuple
    print(city)
for char in "Iteration is easy":   #String
    print(char)



cities = ["Berlin", "Vienna", "Zurich"]
iterator_obj = iter(cities)
print(iterator_obj)

print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))

def iterable(obj):
     try:
         iter(obj)
         return True
     except TypeError:
         return False 
        
for element in [34, [4, 5], (4, 5), {"a":4}, "dfsdf", 4.5]:
    print(element, "iterable: ", iterable(element))
    
    

