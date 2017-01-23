'''
What is the probability that the  defect is found during the "first 5" inspections?
'''
# numerator, denominator = map(int, raw_input().strip().split(" "))
# n = int(raw_input())

numerator, denominator = 1, 3
n = 5

probability = float(numerator) / denominator

ans = 0
for n in range(1, 6):
    ans += (1 - probability) ** (n - 1) * probability

print round(ans, 3)
