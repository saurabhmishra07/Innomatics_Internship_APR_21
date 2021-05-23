import numpy as np
N,M=map(int,input("Enter the dimensions").split())
arr1=np.array([input().split() for i in range(N)],int)
print(np.mean(arr1,axis=1))
print(np.var(arr1,axis=0))
compute_std=round(np.std(arr1,axis=None),11)
print(compute_std)