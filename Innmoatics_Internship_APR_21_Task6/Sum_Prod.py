import numpy as np
N,M=map(int,input("Enter the number").split())
arr1=np.array([input("enter the list").split() for i in range(N)],int)

print(np.prod(np.sum(arr1, axis=0),axis=0))