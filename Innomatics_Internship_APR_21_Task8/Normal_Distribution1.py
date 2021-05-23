from math import sqrt,erf
mean = 20
stdev = 2
test1 = 19.5
testA = 20
testB = 22
print(round(0.5*(1+erf((test1-mean)/(sqrt(2)*stdev))),3))
print(round(0.682689492137/2,3))