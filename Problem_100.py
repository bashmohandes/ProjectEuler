#! /usr/bin/env python

from AutoMeasure import AutoMeasure	


@AutoMeasure
def main():
	n = 21
	b = 15
	target = 10 ** 12
	while n < target:
		b_t = 3 * b + 2 * n - 2
		n_t = 4 * b + 3 * n - 3		

		n = n_t
		b = b_t

	print b

if __name__ == "__main__":
	main()