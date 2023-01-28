# Homework 2.1: Python Lists
# File: HW2p1_Task3_corniedj.py 
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
# Purpose: Output resistor values for series and in parallel

R = [[100, 200], [810, 560], [470, 360]]

for i in R: #loop through big list of smaller lists
    sumSeries = 0
    sumParallel = 0 #reset values
    for j in i:
        sumSeries += j #use loop to add in series
    sumParallel = 1/((1/i[0])+(1/i[1])) #Use equation to find parallel

    print("R1 = {0:.0f}; R2 = {1:.0f}; Rseries = {2:.0f}; Rparallel = {3:.1f}\n".format(i[0], i[1], sumSeries, sumParallel))
    #print out information for each loop so we can reset values after printing
    







    
        


