'''
Created on 29-Jan-2020

@author: SUBHASHIS
'''

if __name__ == '__main__':
    pass


#Example of elif
person = input("Nationality? ")
if person == "french" or person == "French":
    print("You are ?" +person+" person")
elif person == "italian" or person == "Italian":
    print("Preferisci parlare italiano?")
else:
    print("You are neither French nor Italian.")
    print("So, let us speak English!")


# Another example of elif    
age = int(input("Age of the dog: "))
print()
if age < 0:
    print("This cannot be true!")
elif age == 0:
    print("This corresponds to 0 human years!")
elif age == 1:
    print("Roughly 14 years!")
elif age == 2:
    print("Approximately 22 years!")
else:
    human = 22 + (age -2) * 5
    print("Corresponds to  " + str(human) + " human years!")
    
    
# Another example of elif to find the greatest between three numbers

x = float(input("1st Number: "))
y = float(input("2nd Number: "))
z = float(input("3rd Number: "))

if x > y and x > z:
    maximum = x
elif y > x and y > z:
    maximum = y
else:
    maximum = z

print("The maximal value is: " + str(maximum))

# Easy way to find the maximum between three numbers
x = float(input("1st Number: "))
y = float(input("2nd Number: "))
z = float(input("3rd Number: "))

maximum = max((x,y,z))
print("The maximal value is: " + str(maximum))

