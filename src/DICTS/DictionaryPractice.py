'''
Created on 27-Jan-2020

@author: SUBHASHIS
'''
from DICTS.morsecode import MorseCode

if __name__ == '__main__':
    pass

city_population = {"New York City":8550405, "Los Angeles":3971883, "Toronto":2731571, "Chicago":2720546,
                     "Houston":2296224, "Montreal":1704694, "Calgary":1239220, "Vancouver":631486, "Boston":667137}

print(city_population["New York City"])
print(city_population["Toronto"])
print(city_population["Boston"])
print(city_population)
#print(city_population[0])  # we can not access a value by its index position in dictionary because it is not ordered
city_population["Halifax"] = 390096  # Adding one more element to dictionary
city = {}  # empty dictionary

food = {"ham" : "yes", "egg" : "yes", "spam" : "no" }
print(food)
food["spam"] = "yes"
print(food)

#dic = { [1,2,3]:"abc"}# only immutable data types are applicable as keys so we can not use List, Set but can use Tuple, FrozenSet ... etc
dic = { (1, 2, 3):"abc", 3.1415:"abc"}
print(dic)


)
