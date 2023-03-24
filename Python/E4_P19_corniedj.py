# Exam 4
# File: E4_P19_corniedj.py 
# Date:    2 13 2023
# By:      Derek Corniello
# Section: 003
# Team:    041
# 
# ELECTRONIC SIGNATURE
# DC
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# Purpose: use prompted inputs to calculate and print the maximum height and range of a rocket

def Rocket(initialVelo, numAngs):
    import math
    g = 9.81
    
    for i in range(numAngs):
        angleDeg = -1
        
        while(angleDeg <= 0 or angleDeg >= 90):
            angleDeg = float(input("Input the angle you used (Between 0 and 90 degrees, non-inclusive): "))

        angleRad = angleDeg*(math.pi/180)
        maxHeight = ((initialVelo**2)*(math.sin(angleRad)**2))/(2*g)
        maxRange = 2*((initialVelo**2)*(math.cos(angleRad)*math.sin(angleRad))/g)

        print("Vo = {0:.1f} m/s, Th = {1:.1f} deg., MaxHeight = {2:.1f} m, MaxRange = {3:.1f} m".format(initialVelo, angleDeg, maxHeight, maxRange))
              
