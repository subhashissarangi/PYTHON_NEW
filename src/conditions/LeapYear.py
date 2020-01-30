'''
Created on 29-Jan-2020

@author: SUBHASHIS
'''
'''
A leap year is a calendar year containing an additional day added to keep the calendar year synchronized with the 
astronomical or seasonal year. In the Gregorian calendar, each leap year has 366 days instead of 365, by extending 
February to 29 days rather than the common 28. These extra days occur in years which are multiples of four (with the
exception of centennial years not divisible by 400). Write a Python program, which asks for a year and calculates, 
if this year is a leap year or not.
'''
class MyClass(object):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
   
    year = int(input("Which year? "))
    
    def isLeapYear(self, year):
       flag = False
       if year % 4:
           # not divisible by 4
           print("no leap year")
       elif year % 100 == 0 and year % 400 != 0:
           print("no leap year")
       else:
           print("leap year")
           flag = True
       return flag

    
