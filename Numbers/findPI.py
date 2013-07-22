#!/usr/bin/env python
import math
from decimal import Decimal

# Find PI to the Nth Digit
# Enter a number and have the program generate PI up to that many decimal places. 
# Keep a limit to how far the program will go.

digitsOfPI = raw_input("How many digits do you want to generate for PI? ")

print "PI: " + str(Decimal(math.pi))[0:int(digitsOfPI)+2]