#!/usr/bin/env python
import math

number = raw_input("Which number to you wish to find prime factors of? ")
firstPrime = 0

# try and divide by 2, 3, 5, 7

def primeFactor(the):
	oldx = 0
	y = 0
	# sum the digits until only one digit
	for x in xrange(1,len(the)+1):
		if x == 0:
			oldx = x
			continue
		firstPrime = int(x) + int(oldx)
		oldx = x

	print str(firstPrime),
	nextPrime = int(number) / firstPrime
	if len(str(nextPrime)) > 1:
		primeFactor(str(nextPrime))
	else:
		print str(nextPrime),

primeFactor(number)

# % x by 2 and 3 to see if it can be reduced : y

# divide x by y

# repeat --->



# def is_a_prime(x):
#     for i in range(2, x):
#         if x % i == 0:
#             return False
#     return True


# # standard boilerplate
# if __name__ == '__main__':
#     n = int(raw_input('Enter the number to find prime factors of: '))


#     factors = []


#     for i in range(2, n + 1):
#         if n % i == 0:
#             if is_a_prime(i):
#                 factors.append(i)
#                 n /= i
#     print factors
