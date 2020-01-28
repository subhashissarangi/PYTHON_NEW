'''
Created on 28-Jan-2020

@author: SUBHASHIS
'''

if __name__ == '__main__':
    pass

w = {"house":"Haus", "cat":"", "red":"rot"}
items_view = w.items()
items = list(items_view)
print(items)

keys_view = w.keys()
keys = list(keys_view)
print(keys)

values_view = w.values()
values=list(values_view)
print(values)

#Converting lists to dictionaries
dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"]

country_specialities_iterator = zip(countries, dishes)
print(country_specialities_iterator)
country_specialities = list(country_specialities_iterator)
print(country_specialities)
#converting to dictionary
country_specialities_dict = dict(country_specialities)
print(country_specialities_dict)

#Making it shorter
dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"]
dict(zip(countries, dishes))
#There is still one question concerning the function zip(). 
#What happens, if one of the two argument lists contains more elements than the other one?
dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"," Switzerland"]
country_specialities = list(zip(countries, dishes))
country_specialities_dict = dict(country_specialities)
print(country_specialities_dict)

#Making it more shorter
country_specialities_dict = dict(list(zip(["pizza", "sauerkraut", "paella", "hamburger"],
                                          ["Italy", "Germany", "Spain", "USA"," Switzerland"])))
print(country_specialities_dict)

l1 = ["a","b","c"]
l2 = [1,2,3]
c = zip(l1, l2)
for i in c:
    print(i)
#iterators exhaust themselves so in this time it wont print anything
for i in c:
    print(i)
    
    
l1 = ["a","b","c"]
l2 = [1,2,3]
c = zip(l1,l2)
z1 = list(c)
z2 = list(c)
print(z1)
[('a', 1), ('b', 2), ('c', 3)]
print(z2)
[]

dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"]
country_specialities_zip = zip(dishes,countries)
print(list(country_specialities_zip))
country_specialities_list = list(country_specialities_zip)
country_specialities_dict = dict(country_specialities_list)
print(country_specialities_dict)
print(country_specialities_dict)
print(country_specialities_dict)
print(country_specialities_dict)
















