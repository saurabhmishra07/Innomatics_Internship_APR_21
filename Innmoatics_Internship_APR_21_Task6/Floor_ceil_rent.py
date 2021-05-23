import numpy
numpy.set_printoptions(legacy='1.13')
arr = numpy.array(input("Enter the number").split(),float)

print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))