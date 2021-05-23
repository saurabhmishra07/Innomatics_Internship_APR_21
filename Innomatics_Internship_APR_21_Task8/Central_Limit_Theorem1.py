import math
weights = 9800
boxes = 49
mean = 205
stdDev = 15
adjustedMean = 49*205
adjustedStdDev = math.sqrt(49) * 15
ans = 1/2 * (1 + math.erf((weights - adjustedMean)/(adjustedStdDev * math.sqrt(2))))
print("%.4f" % ans)