'''
Created on 26-Jan-2020

@author: SUBHASHIS
'''

if __name__ == '__main__':
    pass

# List created
countries = ["Germany","Switzerland","Austria","France","Belgium", "Netherlands", "England"]
print(len(countries))

languages = ["Python", "C", "C++", "Java", "Perl"]
print(languages[0] + " and " + languages[1] + " are quite different!") 
print("Accessing the last element of the list: " + languages[-1])

person = [["Marc","Mayer"],["17, Oxford Str", "12345","London"],"07876-7876"]
name = person[0]
print(name)

first_name = person[0][0]
print(first_name)


complex_list1 = [["a",["b",["c","x"]]]]
complex_list = [["a",["b",["c","x"]]],42]

print(complex_list[0][1])

t = ("tuples", "are", "immutable")
t[0]="assignments to elements are not possible"

str1 = "Python is great"
first_six = str1[0:6]
print(first_six)

starting_at_five = str1[5:]
print(starting_at_five)

a_copy = str1[:]
print(a_copy)


without_last_five = str1[0:-5]
print(without_last_five)

cities = ["Vienna", "London", "Paris", "Berlin", "Zurich", "Hamburg"]
first_three = cities[0:3]
#or we can do like this
first_three = cities[:3]


























