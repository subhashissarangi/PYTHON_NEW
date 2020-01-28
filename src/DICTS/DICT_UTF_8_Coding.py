'''
Created on 28-Jan-2020

@author: SUBHASHIS
'''

if __name__ == '__main__':
    pass

# -*- coding: utf-8 -*-

trainings = { "course1":{"title":"Python Training Course for Beginners", 
                         "location":"Frankfurt", 
                         "trainer":"Steve G. Snake"},
              "course2":{"title":"Intermediate Python Training",
                         "location":"Berlin",
                         "trainer":"Ella M. Charming"},
              "course3":{"title":"Python Text Processing Course",
                         "location":"Munchen",
                         "trainer":"Monica A. Snowdon"}
              }

trainings2 = trainings.copy()

trainings["course2"]["title"] = "Perl Training Course for Beginners"
print(trainings)
print(trainings2)


knowledge = {"Frank": {"Perl"}, "Monica":{"C","C++"}}
knowledge2 = {"Guido":{"Python"}, "Frank":{"Perl", "Python"}}
knowledge.update(knowledge2)
print(knowledge)

#Iterating over a dictionary
d = {"a":123, "b":34, "c":304, "d":99}
#No method is needed to iterate over the keys of a dictionary: 
for key in d:
    print(key)
#But it's possible to use the method keys(), but we will get the same result: 
for key in d.keys():
    print(key)
#The method values() is a convenient way for iterating directly over the values:
for value in d.values():
    print(value)
    
# The above loop is logically equivalent to the following one:the second way is less efficient
for key in d:
    print(d[key])
    
# What is timeit  in Ipython
   















