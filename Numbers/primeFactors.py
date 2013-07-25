#!/usr/bin/env python
import math

# number = raw_input("Which number to you wish to find prime factors of? ")
# firstPrime = 0

# # try and divide by 2, 3, 5, 7

# def primeFactor(the):
# 	oldx = 0
# 	y = 0
# 	# sum the digits until only one digit
# 	for x in xrange(1,len(the)+1):
# 		if x == 0:
# 			oldx = x
# 			continue
# 		firstPrime = int(x) + int(oldx)
# 		oldx = x

# 	print str(firstPrime),
# 	nextPrime = int(number) / firstPrime
# 	if len(str(nextPrime)) > 1:
# 		primeFactor(str(nextPrime))
# 	else:
# 		print str(nextPrime),

# primeFactor(number)

# noprimes = [j for i in range(2, 8) for j in range(i*2, 5000, i)]
# primes = [x for x in range(2, 5000) if x not in noprimes]
# primes = [2, 3, 5, 7, 9, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

number = int(raw_input("Which number to you wish to find prime factors of? "))

def the_prime_is(num):
	da_numbers = range(2,num+1)
	for i in range(len(da_numbers)):
		if num % da_numbers[i] == 0:
			return da_numbers[i]

primesInNumber = []
all_primes_not_found = True

while all_primes_not_found:
	prime = the_prime_is(number)
	primesInNumber.append(prime)

	for i in range(number):
		number = number/prime
		prime = the_prime_is(number)
		if prime < 0:
			all_primes_not_found = False
			break

		primesInNumber.append(prime)

print primesInNumber

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
