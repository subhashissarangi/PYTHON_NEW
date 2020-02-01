'''
Created on 31-Jan-2020

@author: SUBHASHIS
'''


def fib_intervall(x):
    """ returns the largest fibonacci
    number smaller than x and the lowest
    fibonacci number higher than x"""
    if x < 0:
        return -1
    (old, new, lub) = (0, 1, 0)
    while True:
        if new < x:
            lub = new 
            (old, new) = (new, old + new)
        else:
            return (lub, new)

            
while False:
    x = int(input("Your number: "))
    if x <= 0:
        break
    (lub, sup) = fib_intervall(x)
    print("Largest Fibonacci Number smaller than x: " + str(lub))
    print("Smallest Fibonacci Number larger than x: " + str(sup))
    

def f():
    global s
    print(s)
    s = "dog"
    print(s) 


s = "cat" 
f()
print(s)


def arithmetic_mean(first, *values):
    """ This function calculates the arithmetic mean of a non-empty
        arbitrary number of numerical values """

    return (first + sum(values)) / (1 + len(values))


print(arithmetic_mean(45, 32, 89, 78))
print(arithmetic_mean(8989.8, 78787.78, 3453, 78778.73))
print(arithmetic_mean(45, 32))
print(arithmetic_mean(45))

x = [3, 5, 9]
print(arithmetic_mean(*x))

my_list = [('a', 232),
           ('b', 343),
           ('c', 543),
           ('d', 23)]

    
print(list(zip(*my_list)))

def fun(**kwargs):
    print(kwargs)
    
fun(de="German",en="English",fr="French")

