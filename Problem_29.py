#! /usr/bin/env python

from AutoMeasure import AutoMeasure	
import itertools

@AutoMeasure
def main():
	start = 2
	finish = 100
	print len(set([ c[0] ** c[1] for c in itertools.product(range(start, finish + 1), repeat=2)]))


if __name__ == "__main__":
	main()