# Homework 3.2: Python Lists
# File:    HW3p2_Task1_corniedj.py 
# Date:    1 27 2023
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
# Purpose: Sort through a .txt file and write out the
#          result of the equation to a .txt file.

#Read a data from a file and store it in a var
readFile = open("Task1.txt", "r")
data = readFile.readlines()
readFile.close()

#create some empty lists to store data in for writing later
substances = []
temps = []
pressures = []

for i in range(len(data)): #iterate through the rows of data
    if(i != 0):            #Because the file contains headers, we will have to
                           #skip the first row of "data"
        
        line = data[i].split() #Split the columns of data in the row into separate points

        #add these datapoints to their respective lists.
        #and since we are not doing calculations with them,
        #we can leave them as strings.
        substances.append(line[0])
        temps.append(line[6])

        #Check to make sure the temp is between the min and max temp
        if (float(line[6]) > float(line[4]) and float(line[6]) < float(line[5])):
            #if it is calculate the pressure according to the equation
            P = 10**(float(line[1])-(float(line[2])/(float(line[3])+float(line[6]))))
        else:
            #if not, store -9999 for invalid temp
            P = -9999
        #Add the pressure to the list to write to a file later no matter it's value
        pressures.append(P)

#Create or write to a file with the data
writeFile = open("Task1_Results.txt", "w")
writeFile.write("{0:20} {1:15} {2:10}\n".format("Substance", " T", "   P")) #Headers
for j in range(len(substances)): #iterate through the lists
    writeFile.write("{0:20} {1:11} {2:10.2f}\n".format(substances[j], temps[j], pressures[j])) #data

writeFile.close()
