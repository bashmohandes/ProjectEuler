#! /usr/bin/env python

__author__ = 'mohamed.elsherif'

memo = {}


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


def fib(n):
    if n in memo:
        return memo[n]
    if n < 2:
        return n
    f = fib(n - 1) + fib(n - 2)
    memo[n] = f
    return f


def is_even(n):
    return n % 2 == 0


if __name__ == "__main__":
    main()

