#! /usr/bin/env python
from Memoize import Memoize
from AutoMeasure import AutoMeasure
__author__ = 'mohamed.elsherif'

cache = {89: True, 1: False}


def next_number_in_chain(start):
    tmp = start
    result = 0
    while tmp > 0:
        r = tmp % 10
        result += r * r
        tmp /= 10
    return result


def ends_in_89(start):
    d = start
    while True:
        if d in cache:
            cache[start] = cache[d]
            return cache[d]
        d = next_number_in_chain(d)


@AutoMeasure
def main():
    count = 0
    for x in xrange(1, 10000001):
        if ends_in_89(x):
            count += 1
    print count


if __name__ == "__main__":
    main()