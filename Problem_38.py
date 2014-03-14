#! /usr/bin/env python
import itertools
from AutoMeasure import AutoMeasure

__author__ = 'Mohamed.Elsherif'


@AutoMeasure
def main():
    max_range = 9876
    min_range = 9123
    for i in xrange(max_range, min_range - 1, -1):
        c = product_concat(i, [1, 2])
        if is_pandigital(c):
            print c
            return


def product_concat(x, l):
    m = map(lambda e: x * e, l)
    return reduce(lambda e, p: e + str(p), m, "")


def is_pandigital(x):
    s = set(str(x))
    for i in range(1, 10):
        if str(i) not in s:
            return False
    return True


if __name__ == "__main__":
    main()