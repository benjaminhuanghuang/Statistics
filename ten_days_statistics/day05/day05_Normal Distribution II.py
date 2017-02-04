import math

'''
1: P(x > 80) = P(80 < x <= max_score) = F(max_score) - F(80) = 1 - cdf(80)
2: P(x >= 60) = P(60 <= x <= max_score) = F(max_score) - F(60) = 1 - cdf(60)
3: P(60) = cdf(60)


70 10
80
60

15.87
84.13
15.87

'''

u = 70
sdev = 10


# Cumulative Distribution Function (CDF)?

def cdf(x, mean, sdev):
    ans = 0.5 * (1 + math.erf((x - mean) / (sdev * math.sqrt(2)))) *100
    return round(ans, 2)


print 100 - cdf(80, u, sdev)
print 100 - cdf(60, u, sdev)
print cdf(60, u, sdev)
