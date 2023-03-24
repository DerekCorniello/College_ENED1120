readFile = open("TempC.txt", "r")
data = readFile.readlines()
readFile.close()

tempF = []
for i in range(len(data)):
    newTemp = (float(data[i])*1.8)+32
    tempF.append(newTemp)
 
writeFile = open("TempF.txt", "w")
for j in range(len(tempF)):
    writeFile.write("{0:.0f}\n".format(tempF[j]))
    
writeFile.close()
