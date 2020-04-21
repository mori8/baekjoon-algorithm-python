import operator as op
from functools import reduce
import sys


def combination(n, r):
    if n < 1 or r < 0 or n < r:
        raise ValueError
    r = min(r, n-r)
    numerator = reduce(op.mul, range(n, n-r, -1), 1)
    denominator = reduce(op.mul, range(1, r+1), 1)
    return numerator // denominator % 1000000007


a, b = map(int, sys.stdin.readline().split())
print(combination(a, b))
