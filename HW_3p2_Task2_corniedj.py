# Homework 3.2: Python Lists
# File:    HW3p2_Task2_corniedj.py 
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
# Purpose: Read temperatures from a .txt file and
#          Output the averages to a different .txt file

# open the file with all the data in it
readFile = open("Task2.txt", "r")
data = readFile.readlines() #read all tbe lines and store in a var
readFile.close()

# reset the variable values in order to get correct values
currentYear = "1950"
janSum = 0
julySum = 0
avgJanList = []
avgJulyList = []
years = []
years.append("1950") #We need to add 1950 to the years list or else the
                     #following loop will not work

for i in range(len(data)):
    line = data[i].split() #iterate through the rows of data and
                           #split the data between the columns and
                           #store it in a variable

    #Check to see if the line we are on has a different year than the prev line
    #Also check to see if we are on the last line
    if (currentYear != line[0]) or (i == len(data)-1):
        
        if(i == len(data)-1):
            #if we are iterating on the last line, we want to make sure that
            #the final datapoint is added before calculating the average.
            janSum += float(line[1])
            julySum += float(line[2])

        #Add this year to the list of years to print later
        years.append(line[0])
        #Set current year to the year of the line we are on
        currentYear = line[0]

        #calculate the average over the 31 day period
        janAvg = janSum / (31)
        julyAvg = julySum / (31)

        #add the averages to the list of averages for each month
        avgJanList.append(janAvg)
        avgJulyList.append(julyAvg)

        #reset the sum
        janSum = 0
        julySum = 0

    #Now since we have calculated the averages and reset them,
    #we are still on the same line, we need to add these to
    #the total. These lines have no affect on the last iteration.
    janSum += float(line[1])
    julySum += float(line[2])
        

#Create or open a file to write the data to
writeFile = open("Task2_Results.txt", "w")
writeFile.write("{0:6} {1:8} {2:10}\n".format("Year", "    JanAvg", "    JulyAvg")) #Titles with some spacing

for j in range(len(avgJanList)): #iterate through the list of data and print out each with some space between
    writeFile.write("{0:6} {1:8.1f} {2:10.1f}\n".format(years[j], avgJanList[j], avgJulyList[j]))

writeFile.close()


