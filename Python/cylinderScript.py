import cylinderFunct 

r = float(input("Enter Radius: "))
h = float(input("Enter Height: "))

while r <= 0:
    r = float(input("Please enter a positive, non-zero number for Radius: "))

while h <= 0:
    h = float(input("Please enter a positive, non-zero number for Height: "))

[SA, V] = cylinderFunct.cylinder(r,h)

print("The surface area is {0:.1f} and the volume is {1:.1f} for a cylinder with radius {2:.1f} and a height of {3:.1f} \n".format(SA, V, r, h))
