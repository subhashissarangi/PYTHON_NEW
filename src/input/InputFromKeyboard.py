'''
Created on 29-Jan-2020

@author: SUBHASHIS
'''

if __name__ == '__main__':
    pass

#-------------------------------------------- name = input("What's your name? ")
#--------------------------------------- print("Nice to meet you " + name + "!")
#----------------------------------------------------- age = input("Your age? ")
#------------- print("So, you are already " + age + " years old, " + name + "!")

cities_canada = input("Largest cities in Canada: ")
print(cities_canada, type(cities_canada))

cities_canada = eval(input("Largest cities in Canada: "))
print(cities_canada, type(cities_canada))

population = input("Population of Toronto? ")
print(population, type(population))

population = int(input("Population of Toronto? "))
print(population, type(population))