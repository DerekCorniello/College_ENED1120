import math
def cylinder(radius, height):
    SA = 2*math.pi*radius*height #Professor said that it "was not important to include the bottom and top of cylinder for area"
    V = math.pi*(radius**2)*height
    return SA, V
