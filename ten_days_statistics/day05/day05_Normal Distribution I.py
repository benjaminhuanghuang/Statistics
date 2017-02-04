import math

mean = 20
sdev = 2


def normal(x, mean, sdev):
    ans = 0.5 * (1 + math.erf((x - mean) / (sdev * math.sqrt(2))))
    return round(ans, 3)

# Less than  hours:
print normal(19.5, mean, sdev)

# Between  and  hours
print normal(22, mean, sdev) - normal(20, mean, sdev)

'''
0.401
0.341
'''