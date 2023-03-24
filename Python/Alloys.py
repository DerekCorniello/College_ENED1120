# Homework 1.2: Python Functions
# File: Alloy.py 
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
# Purpose: Compute the total cost of number
# for the total pounds of specified alloy

#funct intakes a string for num and a nonzero positive number for lbs, checked before function call
def alloyFunct(num, lbs):
    if num == "2024":
        cost = lbs*((.935*1.08)+(.044*3.81)+(.015*5.27)+(.006*4))
    elif num == "7075":
        cost = lbs*((.903*1.08)+(.016*3.81)+(.025*5.27)+(.056*1.35))
    else:
        cost = lbs*((.927*1.08)+(.003*5.27)+(.07*5))

    return(cost)
