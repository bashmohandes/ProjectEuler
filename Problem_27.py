#! /usr/bin/env python
from utils import is_prime
from AutoMeasure import AutoMeasure

__author__ = "Mohamed Elsherif"


def quadratic(n, a, b):
	return n * n + a * n + b


def number_of_consequetive_primes(a, b):
	n = 0
	while is_prime(quadratic(n, a, b)):
		n += 1
	return n


@AutoMeasure
def main():
	print "Problem 27 started"
	max_n = 0
	max_a = 0
	max_b = 0
	N = 1000
	for a in range(-N, N):
		for b in range(-N, N):		
			primes_num = number_of_consequetive_primes(a, b)
			if primes_num > max_n:
				max_a = a
				max_b = b
				max_n = primes_num				
	print max_a * max_b
		


if __name__ == "__main__":
	main()