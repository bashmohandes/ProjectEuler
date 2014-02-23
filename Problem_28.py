#! /usr/bin/env python

from AutoMeasure import AutoMeasure

@AutoMeasure
def main():
	corner = 1	
	sum_of_corners = corner
	for i in range(2, 1001, 2):
		for j in range(4):			
			corner += i
			sum_of_corners += corner	
	print sum_of_corners
	


if __name__ == "__main__":
	main()