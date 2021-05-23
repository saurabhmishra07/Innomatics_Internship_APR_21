import numpy as np
N = int(input("Enter the number"))
A = np.array([input().split() for i in range(N)],float)

print(np.linalg.det(A))
