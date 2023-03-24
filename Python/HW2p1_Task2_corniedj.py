# Homework 2.1: Python Lists
# File: HW2p1_Task2_corniedj.py 
# Date:    1 19 2023
# By:      Derek Corniello
# Section: 003
# Team:    XXX
# 
# ELECTRONIC SIGNATURE
# DC
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# Purpose: Create a list of temperatures in range using
# Antoine's Equation

gasChoice = str(input("Which gas would you like to test? ")) #Get input of all gasses

while gasChoice != "Methanol" and gasChoice != "Butane" and gasChoice != "Octane":
    #ensure input is valid
    gasChoice = str(input("Please enter in 'Methanol', 'Butane', or 'Octane'. "))
    #reprompt input

#3 cases with 3 different equations will be defined
#based on inputs in the if statements here

if gasChoice == "Methanol": 
    A = 8.0724
    B = 1574.99
    C = 238.87
    Tmin = -16
    Tmax = 91
    deltaT = (Tmax - Tmin)/19
                    
elif gasChoice == "Butane":
    A = 6.80896
    B = 935.86
    C = 238.73
    Tmin = -78
    Tmax = 19
    deltaT = (Tmax - Tmin)/19

else:
    A = 6.9094
    B = 1349.82
    C = 209.385
    Tmin = 19
    Tmax = 152
    deltaT = (Tmax - Tmin)/19

#declare empty lists

tempList = []
pressureList = []

#start previous temp with minimum temp as a start

prevTemp = Tmin

for i in range(0, 20): #create temp ranges with loop
    tempList.append(prevTemp)
    prevTemp += deltaT

for j in tempList: #calculate pressure for each temp with loop
    pressureList.append(10**(A-(B/(C+j))))

for k in range(len(tempList)): #print out temps and corresponding pressure
    print("Temperature = {0:.3f}(C); Pressure = {1:.3f}(mmHg).\n".format(tempList[k], pressureList[k]))
    

