import math
AB=int(input("Enter the number"))
BC=int(input("Enter the number"))
a=math.atan2(AB,BC)
b=math.degrees(a)
c=round(b)
d=int(c)
e=str(d)
f=e+u'\N{DEGREE SIGN}'
print(f)