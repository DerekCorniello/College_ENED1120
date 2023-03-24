A = [1, 2, 3, 4, 5]
B = []
for i in A:
    B.append(i**2)

for j in range(len(A)):
    print("A = {0:.2f} and A^2 = {1:.2f} \n".format(A[j], B[j]))
