import numpy as np
N,M=map(int,input("Enter the number").split())
arr=np.array([input("Enter the array").strip().split() for i in range(N)] , int)
print(arr.transpose())
print(arr.flatten())
