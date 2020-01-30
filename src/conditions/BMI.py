'''
Created on 29-Jan-2020

@author: SUBHASHIS
'''

'''
Body mass index (BMI) is a value derived from the mass (weight) and height of a person. The BMI is defined as the 
body mass divided by the square of the body height, and is universally expressed in units of kg/m2, resulting from 
mass in kilograms and height in metres. BMI=ml2 Write a program, which asks for the length and the weight of a person 
and returns an evaluation string according to the following table:
'''


class BMI(object):
    
    def __init(self,params):
        
    
    

     height = float(input("What is your height? "))
     weight = float(input("What is your weight? "))
     def getBMI(self):
            bmi = weight / height ** 2
            print(bmi)
            if bmi < 15:
                print("Very severely underweight")
                return bmi
            elif bmi < 16:
                print("Severely underweight")
                return bmi
            elif bmi < 18.5:
                print("Underweight")
                return bmi
            elif bmi < 25:
                print("Normal (healthy weight)")
                return bmi
            elif bmi < 30:
                print("Overweight")
                return bmi
            elif bmi < 35:
                print("Obese Class I (Moderately obese)")
                return bmi
            elif bmi < 40:
                print("Obese Class II (Severely obese)")
                return bmi
            else:
                print("Obese Class III (Very severely obese)")
                return bmi
        
        