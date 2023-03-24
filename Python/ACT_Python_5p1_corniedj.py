import random

numRolls = int(input("How many times should I roll the dice? "))

while numRolls <= 0:
    numRolls = int(input("Please enter a positive value for the number of dice rolls. "))
    
sumsList = []

for i in range(numRolls):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    sumsList.append(dice1+dice2)

sevenCount = 0

for j in sumsList:
    if j == 7:
        sevenCount += 1

print("The number of sums of 7 in the dice rolls is {0} out of {1} rolls.".format(sevenCount, numRolls))
    
