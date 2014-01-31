#! /usr/bin/env python

__author__ = 'Mohamed'


def main():
    n = 600851475143
    i = 2
    while i * i < n:
        while n % i == 0:
            n /= i
        i += 1
    print n

if __name__ == "__main__":
    main()

