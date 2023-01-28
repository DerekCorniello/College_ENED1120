# Homework 1.2: Python Functions
# File:     HW1p2_Task3_corniedj.py 
# Date:    1 12 2023
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
# Purpose: Use the alloy function to return a cost value


import Alloys #import other script with functon

#take inputs
num = str(input("Input your alloy number (2024, 7075, or 356). "))
#Check Inputs
while (num != "2024" and num != "7075" and num != "356"):
    num = input("Please input the correct alloy number (2024, 7075, or 356). ")

#take inputs
lbs = float(input("Please input the weight of the alloy. "))
#Check Inputs
while (lbs <= 0):
    lbs = float(input("Please input a positive, non-zero number for weight. "))

#Print total using the alloyFunct function from the Alloys.py file
print("${0:.2f} is the total cost of the alloy.".format(Alloys.alloyFunct(num, lbs)))
