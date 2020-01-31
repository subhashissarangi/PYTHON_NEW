'''
Created on 30-Jan-2020

@author: SUBHASHIS
'''

def fahrenheit(T_in_celsius):
    """ returns the temperature in degrees Fahrenheit"""
    return (T_in_celsius * 9 / 5) + 32

for t in (22.6, 25.8, 27.3, 29.8):
    print(t,":",fahrenheit(t))  
    
def Hello(name="everybody"):
    """ Greets a person """
    print("Hello " + name + "!")
    
Hello("subhashis")
Hello()

def Hello1(name="everybody"):
    """ Greets a me """
    print("Hello " + name + "!")

print("The docstring of the function Hello: " + Hello1.__doc__)
print()
def sumsub(a, b, c=1, d=0):
    return a - b + c - d

print(sumsub(12,4))
print(sumsub(42,15,d=10))