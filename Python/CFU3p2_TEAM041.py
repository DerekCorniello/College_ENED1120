# CFU 3.2: Python I/O
# File:    CFU3p2_TEAM041.py 
# Date:    1 25 2023
# By:      Team 041
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
# Purpose: Compute the maximum time constants from a text file

readFile = open("RC.txt", "r")
data = readFile.readlines()
readFile.close()

rcList = []
for i in range(len(data)):
    line = data[i].split()
    timeConst = float(line[0])*float(line[1])
    rcList.append(timeConst)

    print("Tau: {0}. R: {1}. C: {2}.".format(timeConst, float(line[0]), float(line[1])))

writeFile = open("CFU3p2.txt", "w")

for j in range(len(rcList)):
    writeFile.write("{0:.2f}\n".format(rcList[j]))
    
writeFile.close()
