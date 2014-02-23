#! /usr/bin/env python

from AutoMeasure import AutoMeasure	

@AutoMeasure
def main():
	s = set()
	start = 2
	finish = 100
	possible = range(start, finish + 1)	
	for x in possible:
		for y in possible:
			s.add(x ** y)
	
	print len(s)



if __name__ == "__main__":
	main()