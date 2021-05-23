import math
import statistics
n = int(input("Enter the number").strip())
X = [float(i) for i in input("Enter input").split()]
Y = [float(i) for i in input("enter input").split()]

def get_pcor(X,Y,n):
    x = statistics.mean(X)
    y = statistics.mean(Y)
    a = statistics.pstdev(X)
    b = statistics.pstdev(Y)
    sum = 0
    for i in range(n):
        cov = (X[i]- x)*(Y[i]-y)
        sum+= cov
    print (round(sum/(n*a*b),3))
get_pcor(X,Y,n)