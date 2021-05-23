from sklearn.linear_model import LinearRegression
X,Y = [int(x) for x in input().split()]
A = []
B = []
for i in range(Y):
    new_row = [float(x) for x in input().split()]
    A.append(new_row[:-1])
    B.append(new_row[-1])
lm = LinearRegression()
lm.fit(A, B)
a = lm.intercept_
b = lm.coef_
test1 = []
p = int(input())
for i in range(p):
    row = [float(x) for x in input().split()]
    print(lm.predict(row)[0])