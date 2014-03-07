#! /usr/bin/env python
from AutoMeasure import AutoMeasure

@AutoMeasure
def main():
	max_seq = 0
	max_i = 0
	for i in range(10, 0, -1):
		if max_seq >= i:
			break
		reminders = [ 0 for x in range(i) ]
		value = 1
		pos = 0

		while not reminders[value] and value != 0:			
			reminders[value] = pos
			value *= 10
			value %= i
			pos += 1		
		if pos - reminders[value] > max_seq:
			max_seq = pos -reminders[value]
			max_i = i

	print "The number with max sequence is %d, maximum sequence length is %d" % (max_i, max_seq)

if __name__ == "__main__":
	main()

