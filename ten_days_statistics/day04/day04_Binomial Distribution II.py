def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


def combination(n, x):
    return factorial(n) / (factorial(x) * factorial(n - x))


def binomial(x, n, p):
    '''
        x : The number of successes
        n : The total number of trials
        p : The probability of success of 1 trial
        https://www.hackerrank.com/challenges/s10-binomial-distribution-1/tutorial
        The binomial distribution is the probability distribution for the binomial random variable,
        given by the following probability mass function:
    '''
    return combination(n, x) * p ** x * (1 - p) ** (n - x)


# p, n = map(float, raw_input().split(" "))
p = 12
n = 10
ans = sum([binomial(i, n, float(p) / 100) for i in range(3)])
print round(ans, 3)

ans = sum([binomial(i, n, float(p) / 100) for i in range(2, n + 1)])
print round(ans, 3)
