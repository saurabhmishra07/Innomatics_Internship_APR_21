import numpy as np
N,M=map(int,input("Enter the number").split())
arr1=np.array([input("Enter the list").split() for i in range(N)],int)
print(np.max(np.min(arr1,axis=1)))