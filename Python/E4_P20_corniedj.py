# Exam 4
# File: E4_P20_corniedj.py 
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
# Purpose: read data from a .txt file and determine the error and write it to another file

readFile = open("Robot.txt", "r")
data = readFile.readlines() 
readFile.close()

goodXTrials = 0
goodYTrials = 0
goodBothTrials = 0

writeFile = open("E4_corniedj.txt", "w")

writeFile.write("Trial Number: Xerror: Yerror:\n")

for i in range(len(data)):
    line = data[i].split()

    if (float(line[0]) >= 19.125 and float(line[0]) <= 19.5 and float(line[1]) >= 58 and float(line[1]) <= 59):
        goodBothTrials += 1
    elif (float(line[0]) >= 19.125 and float(line[0]) <= 19.5):
        goodXTrials += 1
    elif (float(line[1]) >= 58 and float(line[1]) <= 59):
        goodYTrials += 1

    xerror = float(line[0])-19.3125
    yerror = float(line[1])-59
    
    writeFile.write("{0:12} {1:8.4f} {2:8.4f}\n".format((i+1), xerror, yerror))
    
    
writeFile.close()
print("Good Trials for X: {0}\nGood Trials for y: {1}\nGood Trials for Both: {2}".format(goodXTrials, goodYTrials, goodBothTrials))

    
