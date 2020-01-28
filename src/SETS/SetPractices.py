'''
Created on 26-Jan-2020

@author: SUBHASHIS
'''

if __name__ == '__main__':
    pass

x = set("A Python Tutorial")
print(x)
x = set(["Perl", "Python", "Java"])
print(x)
cities = set((("Python","Perl"), ("Paris", "Berlin", "London")))
#cities = set((["Python","Perl"], ["Paris", "Berlin", "London"]))
print(cities)

#FrozenSet
cities = frozenset(["Frankfurt", "Basel","Freiburg"])
#cities.add("Strasbourg")
#After python 2.6 we can create set as
adjectives = {"cheap","expensive","inexpensive","economical"}

#add()
colours = {"red","green"}
colours.add("yellow")
print(colours)

#colours.add(["black","white"])
#clear()
cities = {"Stuttgart", "Konstanz", "Freiburg"}
cities.clear()
print(cities)

#copy()
more_cities = {"Winterthur","Schaffhausen","St. Gallen"}
cities_backup = more_cities.copy()
more_cities.clear()
print(cities_backup)

#In this case it will give an emptySet
more_cities = {"Winterthur","Schaffhausen","St. Gallen"}
cities_backup = more_cities
more_cities.clear()
print(cities_backup)


#difference()
x = {"a","b","c","d","e"}
y = {"b","c"}
z = {"c","d"}
print(x.difference(y))
{'a', 'e', 'd'}
print(x.difference(y).difference(z))
#or we can do like
print(x-y)
print(y-z)
print(x-y-z)


#difference_update() will remove all duplicate from set
x = {"a","b","c","d","e"}
y = {"b","c"}
x.difference_update(y)

#same as
x=x-y

#discard() will remove the declared element in the argument list 
#If element is not a member of the set, nothing will be done. 
x = {"a","b","c","d","e"}
x.discard("a")
print(x)

#remove() but it will throw KeyError if element not found in the set
x = {"a","b","c","d","e"}
x.remove("a")
#x.remove("z")#Throws KeyError as z is not in set

if y in x:
    x.remove(y)
else:
    print("No cities found")
#union()       
x = {"a","b","c","d","e"}
y = {"c","d","e","f","g"}
print(x.union(y))
print(x | y) #The above both statements performs the same task
#intersection
print(x.intersection(y))
print(x & y) #The above both statements performs the same task

# isdisjoint() This method returns True if two sets have a null intersection. 
x = {"a","b","c"}
y = {"c","d","e"}
x.isdisjoint(y)

x = {"a","b","c"}
y = {"d","e","f"}
x.isdisjoint(y)

# issubset() 
# x.issubset(y) returns True, if x is a subset of y. "<=" is an abbreviation for "Subset of" and ">=" for "superset of"
# "<" is used to check if a set is a proper subset of a set. 

x = {"a","b","c","d","e"}
y = {"c","d"}
print(x.issubset(y))
print(y.issubset(x))

print(x < y)
print(y < x)# y is a proper subset of x
print(x <= x )

# issuperset()
# x.issuperset(y) returns True, if x is a superset of y. ">=" is an abbreviation for "issuperset of"
# ">" is used to check if a set is a proper superset of a set. 

x = {"a","b","c","d","e"}
y = {"c","d"}
x.issuperset(y)
print(x > y)
print( x >= y)
print( x <= y)
print(x.issuperset(x))

# pop()
# pop() removes and returns an arbitrary set element. The method raises a KeyError if the set is empty
x.pop()
x.pop()












