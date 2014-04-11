# Project Euler - Problem 46
# --------------------------
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

from myMath import isPrime
from time import time

# Find primes up to a certain number and output a list of them
def primes(top):
	seive = range(2, top+1)
	for m in range(2, top+1):
		for n in range(m, top//m+1):
			p = m*n
			if p<=top: seive[p-2] = 0
	primes = []
	for i in range(top-1):
		if seive[i] != 0: primes.append(seive[i])
	return primes

p_max = 10000 # These have to be high enough for the program to produce the correct answer
s_max = 1000 # => 10000, 100

start_tot = time()

prime_list = primes(p_max)[1:] # Remove the number 2
can_be_written = []

# Get a large list of composites that we can write in such a way
for p in prime_list:
	for s in range(1,s_max+1):
		n = p + 2*s**2
		if not isPrime(n): can_be_written.append(n)

# Get large list of odd composites and check whether each element is in the "can_be_written" list
max_comp = p_max+2*s_max**2
for n in [n for n in range(1,max_comp,2) if not isPrime(n)]: # The [...] generates odd composites
	if n not in can_be_written:
		print n
		break
print "Time taken:", time()-start_tot
