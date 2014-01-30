#! /usr/bin/env python
from Memoize import Memoize

__author__ = 'mohamed.elsherif'


@Memoize
def fib(n):
    if n < 2:
        return n
    f = fib(n - 1) + fib(n - 2)
    return f


def is_even(n):
    return n % 2 == 0


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

