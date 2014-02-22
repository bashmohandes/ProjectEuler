__author__ = 'Mohamed'

from math import sqrt
from Memoize import Memoize


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


@Memoize
def fact(n):
    if n == 0:
        return 1
    result = 1
    for i in xrange(1, n + 1):
        result *= i
    return result
