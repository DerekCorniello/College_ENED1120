# Homework 1.2: Python Functions
# File: Algebra.py 
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
# Purpose: Develop an algorithm to compute the unique solution
# to two linear equations

#take inputs into function
#in std form
def algebraFunct(a1, a2, b1, b2, c1, c2):
    if((a1*b2)-(a2*b1)) != 0: #this checks if there is a solution
        y = ((c2*a1)-(c1*a2))/((a1*b2)-(a2*b1))
        x = ((c2*b1)-(c1*b2))/((a2*b1)-(a1*b2))
        return("{0:.3f}".format(x),"{0:.3f}".format(y)) #this line returns the x & y coordinate
    else:
        print("There is no unique solution for the provided values")
        
    
