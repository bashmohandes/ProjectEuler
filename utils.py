__author__ = 'Mohamed'

from math import sqrt
from Memoize import Memoize
import fractions

@Memoize
def fib(n):
    if n < 2:
        return n
    f = fib(n - 1) + fib(n - 2)
    return f


def is_even(n):
    return n % 2 == 0


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if is_even(n):
        return False
    for i in range(3, int(sqrt(n) + 1), 2):
        if n != i and n % i == 0:
            return False
    return True


def gcd(l):
    return reduce(fractions.gcd, l)


def lcm(a, b):
    g = fractions.gcd(a, b)
    if g == 0:
        return 0
    return abs(a * b) / g


def lcm_list(l):
    return reduce(lcm, l)


@Memoize
def fact(n):
    if n == 0:
        return 1
    result = 1
    for i in xrange(1, n + 1):
        result *= i
    return result


class OrderedPermutations:
    def __init__(self, start):
        self.start = start
        self.current = None

    def __iter__(self):
        return self

    def reversed_xrange(self, n):
        for i in xrange(n - 1, -1, -1):
            yield i        

    def next(self):
        if not self.current:
            self.current = self.start
            return self.start
        for k in self.reversed_xrange(len(self.current) - 1):
            if self.current[k] < self.current[k + 1]:
                for j in self.reversed_xrange(len(self.current)):
                    if self.current[k] < self.current[j]:
                        self.current[k], self.current[j] = self.current[j], self.current[k]
                        self.current = self.current[:k+1] + self.current[k+1:][::-1]                        
                        return self.current
        return self.current



