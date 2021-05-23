import numpy
poly= list(map(float,input().split()))
val=float(input())
print(numpy.polyval(poly,val))