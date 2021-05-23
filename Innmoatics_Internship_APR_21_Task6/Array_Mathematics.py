import numpy as np

N,M=(map(int,input("enter the dimension").split()))
arr1=np.array([list(map(int, input("Enter the list").split())) for i in range(N)])
arr2=np.array([list(map(int, input("Enter the list1 4").split())) for i in range(N)])
print(np.add(arr2,arr1))
print(np.subtract(arr1,arr2))
print(np.multiply(arr2,arr1))
print(arr1//arr2)
print(np.mod(arr1,arr2))
print(arr1**arr2)