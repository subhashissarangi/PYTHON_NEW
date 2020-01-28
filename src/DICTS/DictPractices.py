'''
Created on 26-Jan-2020

@author: SUBHASHIS
'''

city_population = {"New York City":8550405, "Los Angeles":3971883, "Toronto":2731571, "Chicago":2720546,
                     "Houston":2296224, "Montreal":1704694, "Calgary":1239220, "Vancouver":631486, "Boston":667137}

print(city_population["New York City"])
print(city_population["Toronto"])
print(city_population["Boston"])
print(city_population)
#print(city_population[0])  # we can not access a value by its index position in dictionary because it is not ordered
city_population["Halifax"] = 390096  # Adding one more element to dictionary
city = {}  # empty dictionary

food = {"ham":"yes","egg":"yes","spam":"no" }
print(food)
food["spam"] = "yes"
print(food)

#Example English German dictionary
en_de= {"red":"rot","green":"grun","blue":"balu","yellow":"gleb"}
print(en_de)
print(en_de["red"])

en_de = {"red":"rot","green":"grun","blue":"blau","yellow":"gelb"}
print(en_de)
print(en_de["red"])
de_fr = {"rot":"rouge","grun":"vert","blau":"bleu","gelb":"jaune"}
print("The French word for red is: " + de_fr[en_de["red"]])

#dic = { [1,2,3]:"abc"}# only immutable data types are applicable as keys so we can not use List, Set but can use Tuple, FrozenSet ... etc
dic = { (1, 2, 3):"abc", 3.1415:"abc"}
print(dic)
en_de = {"red":"rot","green":"grun","blue":"blau","yellow":"gelb"}
de_fr = {"rot":"rouge","grun":"vert","blau":"bleu","gelb":"jaune"}
dictionaries = {"en_de" : en_de, "de_fr" : de_fr }
print(dictionaries["de_fr"]["blau"])


en_de = {"Austria":"Vienna", "Switzerland":"Bern", "Germany":"Berlin", "Netherlands":"Amsterdam"}
capitals = {"Austria":"Vienna", "Germany":"Berlin", "Netherlands":"Amsterdam"}
capital = capitals.pop("Austria")
capital = capitals.pop("Switzerland", "Bern")# To avoid KeyError if key is not found(Switzerland) then it will return Bern
capitals = {"Springfield":"Illinois", "Augusta":"Maine", "Boston": "Massachusetts", 
            "Lansing":"Michigan", "Albany":"New York", "Olympia":"Washington", "Toronto":"Ontario"}
(city, state) = capitals.popitem()
print(capitals.popitem())

locations = {"Toronto" : "Ontario", "Vancouver":"British Columbia"}
#locations["Ottawa"]# throws KeyError
#To prevent KeyError

if "Ottawa" in locations: print(locations["Ottawa"])
if "Toronto" in locations: print(locations["Toronto"])

#get() is not raising an error, if an index doesn't exist. In this case it will
# return None. It's also possible to set a default value, which will be returned, if an index doesn't exit: 

proj_language = {"proj1":"Python", "proj2":"Perl", "proj3":"Java"}
proj_language.get("proj2")
print(proj_language.get("proj4"))

# setting a default value:
proj_language.get("proj4", "Python")

words={'house': 'Haus', 'cat': 'Katze'}
w = words.copy()
words["cat"]="chat"
print(w)
print(words)

w.clear()#The content of a dictionary can be cleared with the method clear(). 
         #The dictionary is not deleted, but set to an empty dictionary: 























