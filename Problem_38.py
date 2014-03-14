#! /usr/bin/env python
from AutoMeasure import AutoMeasure

__author__ = 'Mohamed.Elsherif'

'''
A bit of analysis
-----------------

to get a 9 digit number D from this formula
D = concat_product(X, [1 ... n]) where n > 1
1- so if n > 1 X has to be 5 digit number at most,
2- We already have a candidate in the example of a 9 digit
pandigital number which is 918273645, so the number we're looking
for (D) must be more than this number.
which means D has to start with 9
3- For D to start with 9, we need X to start with 9 as well.
4- For D to be 9 digits, X has to be 4 digits and n = 2.
    ** if X is 1 digit (which means X = 9 given the finding in #3) the max number will be the one given in the example
    ** if X is 2 digits (98 ~ 91) there is no value of n that can produce a D with 9 digits
    ** if X is 3 digits (987 ~ 912) there is no value of n that can produce a D with 9 digits
    ** if X is 4 digits (9876 ~ 9123) the only value of n > 1 to produce D with 9 digits is n = 2
    ** if X is 5 digits (98765 ~ 91234) there is no value of n that can produce D with 9 digits

So from previous analysis the only range of X that has the right value is (9876 to 9123) with n = 2
'''


@AutoMeasure
def main():
    max_range = 9876
    min_range = 9123
    for i in xrange(max_range, min_range - 1, -1):
        candidate = product_concat(i, [1, 2])
        if is_pandigital(candidate):
            print candidate
            return


def product_concat(x, l):
    products = map(lambda e: x * e, l)
    return reduce(lambda prev, e: prev + str(e), products, "")


def is_pandigital(x):
    s = set(str(x))
    for i in range(1, 10):
        if str(i) not in s:
            return False
    return True


if __name__ == "__main__":
    main()