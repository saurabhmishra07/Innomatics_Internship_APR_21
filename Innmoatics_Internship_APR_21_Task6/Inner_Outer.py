import numpy as np
A = np.array(input("Enter the number").split(), int)
B = np.array(input("Enter the number").split(), int)
print(np.inner(A,B))
print(np.outer(A,B))