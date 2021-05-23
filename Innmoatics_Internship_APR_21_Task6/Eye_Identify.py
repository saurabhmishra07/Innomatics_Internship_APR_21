import numpy as np
np.set_printoptions(sign=' ')
N, M = map(int,input("Enter the number").split())

print (np.eye(N, M, k = 0))