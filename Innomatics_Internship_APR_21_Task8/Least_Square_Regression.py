n = 5
y1 = [85, 95, 70, 65, 70]
x1 = [95, 85, 80, 70, 60]
mean1 = sum(y1)/n
mean2 = sum(x1)/n
diff1 = [(x - mean1) for x in y1]
diff2 = [(x - mean2) for x in x1]
sd1 = pow(sum([pow(x, 2) for x in diff1])/n, 0.5)
sd2 = pow(sum([pow(x, 2) for x in diff2])/n, 0.5)

result= sum(diff1[i]*diff2[i] for i in range(n))/(n*sd1*sd2)
b = result*(sd1/sd2)
a = mean1 - b*mean2

answer = a + b*80
print(round(answer, 3))