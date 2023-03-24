
#enter initial pressure
p1 = float(input("Enter the current pressure: "))
#Check for positive pressure
while p1<0:
    p1 = float(input("Please enter a positive pressure: "))

#Enter units the pressure is in
units = input("Enter the units of the value entered: ")
#Check for correct units
while (units != "Pa" and units != "psi"):
    units = input("Please enter 'Pa' or 'psi' for the units entered: ")
    
#Enter units that you want 
desUnits = input("Enter the units you want: ")
#Check for correcct units
while (desUnits != "Pa" and desUnits != "psi"):
    units = input("Please enter 'Pa' or 'psi' for the units desired: ")

if units == "Pa": #if it is in Pa, convert to psi
    p2 = p1 * 0.000145038
else: #If it is in psi, convert to Pa
    p2 = p1 * 6894.76

#Print converted units
print("Converted pressure is {0:.2f} in {1}".format(p2, desUnits))
