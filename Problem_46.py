#! /usr/bin/env python
from math import sqrt
from AutoMeasure import AutoMeasure
from utils import is_prime, is_even, is_square

__author__ = 'Mohamed.Elsherif'


cache = {}

def is_prime_c(n):
    if n in cache:
        return cache[n]
    cache[n] = is_prime(n)
    return cache[n]


@AutoMeasure
def main():
    current_odd = 9
    while True:
        if not is_prime_c(current_odd) and not conjecture_correct(current_odd):
            print current_odd
            return
        current_odd += 2


def conjecture_correct(current_odd):
    for i in xrange(1, current_odd - 1):
        if not is_prime_c(i):
            continue
        r = current_odd - i
        if not is_even(r):
            continue
        r /= 2
        if is_square(r):
            #print "%d = %d + 2 * %d" % (current_odd, i, r)
            return True
    return False


if __name__ == "__main__":
    main()