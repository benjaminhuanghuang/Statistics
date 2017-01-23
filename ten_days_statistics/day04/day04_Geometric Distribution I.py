'''
the second line contains the inspection we want the probability of being the first defect for:

What is the probability that the 1th defect is found during the "5th" inspection?

https://www.hackerrank.com/challenges/s10-geometric-distribution-1/tutorial

formula:
    g(n, p) = q^(n-1)*p
'''
# numerator, denominator = map(int, raw_input().strip().split(" "))
# n = int(raw_input())

numerator, denominator = 1, 3
n = 5

probability = float(numerator) / denominator

g = (1 - probability) ** (n - 1) * probability

print round(g, 3)
