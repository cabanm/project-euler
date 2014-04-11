from math import sqrt

# This function returns the canonical continued fraction representation of a root
def sqrtContFraction(n):
	a = [int(sqrt(n))]
	remainders = []
	rem = ()
	while rem not in remainders:
		
