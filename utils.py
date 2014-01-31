from math import sqrt

__author__ = 'Mohamed'


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

