#! /usr/bin/env python
from Memoize import Memoize
from utils import is_even
__author__ = 'mohamed.elsherif'


def main():
    i = 1
    result_sum = 0
    while True:
        f = fib(i)
        i += 1
        if f < 4000000:
            if is_even(f):
                result_sum += f
        else:
            break
    print result_sum


if __name__ == "__main__":
    main()

