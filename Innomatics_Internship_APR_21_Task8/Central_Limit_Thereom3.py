import math
mean=500
population=100
stddev=80
adj_mean=500*100  #mean*population
adj_std=math.sqrt(100)*80
interval=0.95
z=1.96
A=(adj_mean-adj_std*z)/(math.sqrt(population))
B=(adj_mean+adj_std*z)/(math.sqrt(population))
c=('%.2f' % A)
d=('%.2f' % B)
print(c)
print(d)

