import numpy as np
N=int(input("enter the number"))
arr1=np.array([input("enter the list").split() for i in range(N)],int)
arr2=np.array([input("Enter the list").split() for i in range(N)],int)
print(np.dot(arr1,arr2))





