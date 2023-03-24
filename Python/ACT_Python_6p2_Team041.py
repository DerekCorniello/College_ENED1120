readFile = open("Snow_Fall.txt", "r")
data = readFile.readlines()
readFile.close()

maxSnow = 0
maxSnowDate = ""
daysOfOne = 0

for i in range(len(data)):
    line = data[i].split()
    if float(line[1]) > float(maxSnow):
        maxSnow = line[1]
        maxSnowDate = line[0]
    if float(line[1]) > 1:
        daysOfOne += 1
        
percentage = (daysOfOne / len(data))*100

print("{0} inches of snow on {1}.".format(maxSnow, maxSnowDate))
print("Percentage of days that exceeded snowfall of one inch: {0:.2f}%.".format(percentage))
