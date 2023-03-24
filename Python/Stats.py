# Homework 2.1: Python Lists
# File: Stats.py 
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
# Purpose: Function to output stdev and mean

import math

def statFunct(statList):
    
    mean = 0 #reset mean value
    for i in statList: #iterate through the list
        mean += i #add each list value
    mean = mean / len(statList) #divide it by the population

    sumsq = 0 #reset the sumsquared value
    for j in statList: #iterate through the list
        sumsq += ((j - mean)**2) #perform calc

    stdev = math.sqrt(sumsq/len(statList)) #calc stdev

    return(mean, stdev) #return solutions
