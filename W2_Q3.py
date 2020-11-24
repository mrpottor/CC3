from math import sqrt
from _functools import reduce
def factors(n):
        step = 2 if n%2 else 1
        return set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))

t = int(input('no of tests to run -'))
for i in range(t):
    n = int(input('number n - '))

    print(factors(n))