#! /usr/bin/env python

from AutoMeasure import AutoMeasure

@AutoMeasure
def main():
	corner = 1
	corners = []
	corners.append(corner)
	for i in range(2, 1001, 2):				
		for j in range(4):			
			corner += i
			corners.append(corner)
	#print corners
	print sum(corners)
	


if __name__ == "__main__":
	main()