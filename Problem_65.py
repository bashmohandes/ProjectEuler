#! /usr/bin/env python
from fractions import Fraction
from AutoMeasure import AutoMeasure

__author__ = 'Mohamed.Elsherif'


@AutoMeasure
def main():
    MAX  = 99
    terms = [j for (i, j) in zip(range(MAX), E_terms())]
    result = 2 + convergent(terms)
    n = result.numerator
    s = 0
    while n > 0:
        s += n % 10
        n /= 10
    print s


def convergent(terms):
    if  len(terms) == 1:
        return Fraction(1, terms[0])

    return Fraction(1, terms[0] + convergent(terms[1:]))


class E_terms:
    def __init__(self):
        self._current = 0
        self._k = 1

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if self._current == 1:
            k = self._k
            self._k += 1
            result =  2 * k
        else:
            result = 1
        self._current = (self._current + 1) % 3
        return result


if __name__ == "__main__":
    main()