N = int(input("Please enter 'N': "))

while N <= 0:
    N = int(input("Please enter a positive, no-zero integer for 'N': "))

fibList = []
n1 = 0
n2 = 1

for i in range(N):
    
