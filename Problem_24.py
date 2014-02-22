#! /usr/bin/env python
from AutoMeasure import AutoMeasure
from utils import fact,OrderedPermutations

import itertools


def reversed_xrange(n):
    for i in xrange(n - 1, -1, -1):
        yield i

"""
	Faster implementation, I think the Iterator utils.OrderedPermutations adds a little bit of overhead.
"""
def next_perm(l):
    for k in reversed_xrange(len(l) - 1):
        if l[k] < l[k + 1]:
            for j in reversed_xrange(len(l)):
                if l[k] < l[j]:
                    l[k], l[j] = l[j], l[k]
                    l = l[:k+1] + l[k+1:][::-1]                    
                    return l
    return l


@AutoMeasure
def main():
    input = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    i = 1
    for p in OrderedPermutations(input):
        if i == 1000000:
        	break
        i += 1
    print i,p


if __name__ == "__main__":
    main()