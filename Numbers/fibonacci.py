#!/usr/bin/env python

# Fibonacci Sequence Enter a number and have the program generate the 
# Fibonacci sequence to that number or to the Nth number.

numberOfNumbers = raw_input("How high to you want to calculate Fibonacci? ")
numberOfNumbers = int(numberOfNumbers)

seed0 = 0
seed1 = 1

for x in xrange(1,999):
	if seed0 > numberOfNumbers:
		break
	print seed0,                # Note to self: , space delimets instead of newline
	if seed1 > numberOfNumbers:
		break
	print seed1,
	seed0 = seed0 + seed1
	seed1 = seed1 + seed0