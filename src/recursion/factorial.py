'''
Created on 31-Jan-2020

@author: SUBHASHIS
'''

if __name__ == '__main__':
    pass

n=int(input("please enter a number: "))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
def iterative_factorial(n):
    result = 1
    for i in range(2,n+1):
        result *= i
    return result

print(factorial(n))
print(iterative_factorial(n))