import numpy
N,M,P=map(int,input("Enter the no. and dimensions").split())
arr1=numpy.array([input("enter the array").split() for i in range(N)],int)
arr2=numpy.array([input("Enter the array").split() for i in range(M)],int)
print(numpy.concatenate((arr1,arr2),axis=0))

