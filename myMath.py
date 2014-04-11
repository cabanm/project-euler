from time import time
from math import sqrt

# Time some code
def timeIt(code):
	start = time()
	exec code
	return time()-start

# Find primes up to a certain number and output a list of them as strings
def primes(top):
	sieve = range(2, top+1)
	for m in range(2, top+1):
		for n in range(m, top//m+1):
			p = m*n
			if p<=top: sieve[p-2] = 0
	primes = []
	for i in range(top-1):
		if sieve[i] != 0: primes.append(str(sieve[i]))
	return primes

# Find primes up to a certain number and output a list of them as numbers
def primesNum(top):
	sieve = [0]*top
	for m in range(2, top+1):
		if sieve[m-1] == 0: # if m prime
			for n in range(m, top//m+1):
				p = m*n
				sieve[p-1] = 1
	primes = []
	for i in range(2,top+1):
		if sieve[i-1] == 0: primes.append(i)
	return primes

# Find Pythagorean triplets with short sides up to and equal to max side
def pythTrips(maxSide):
	triples = []
	for a in range(1, maxSide+1):
		for b in range(1, a):
			c = sqrt(a**2+b**2)
			if c == int(c): triples.append((a,b,int(c)))
	return triples

# Find Pythagorean triplets with max perimeter specified
def pythTripsPerim(p):
	triples = []
	for a in range(1, p):
		for b in range(1, a):
			c = sqrt(a**2+b**2)
			if c == int(c) and a+b+c <= p: triples.append((a,b,int(c)))
	return triples

# Checks if the input string is a pandigital number
def isPandigital(n):
	if n.count('0') != 0: return 0
	for digit in range(1,10):
		if n.count(str(digit)) > 1:
			return 0
	return 1

# Checks if input number is prime
def isPrime(n):
	n = abs(n)
	if n==0 or n==1: return 0
	#print 'Checking primality:', n
	maxm = int(sqrt(n))+1
	for d in range(2, maxm):
		#if (d*100//maxm)%10 == 0: print d/1.0/maxm
		if n%d == 0: return 0
	return 1

# Returns the prime factors of a number given a set of primes
def pFactors(n,primes):
	i = 0
	divs = []
	while n != 1:
		p = primes[i]
		if n%p == 0:
			divs.append(p)
			n = n/p
			i = 0
		else:
			i += 1
	return divs

# Returns the number of unique prime factors for numbers up to and incl. top
def pFactors2(top):
	sieve = [0]*top
	sieve[0] = 1
	for m in range(2, top+1):
		if sieve[m-1] == 0: # if m is prime
			for n in range(2, top//m+1):
				p = m*n
				sieve[p-1] += 1
	return sieve

# Checks if a number is pentagonal
def isPent(n):
	d = sqrt(1.+24*n)
	if d%1 == 0 and (d+1)%6 == 0: return 1
	return 0

# Returns a list of the amount of each digit a number has
# Note: a method with purely mathematical operations took longer than using strings!!!!
def digSig(n):
	sig = [0]*10
	for d in str(n):
		sig[int(d)] += 1
	return sig

# Returns the set of digits in a number
def digits(n):
	return set([int(ch) for ch in str(n)])

# Returns the number of digits in a number
def digNum(n):
	return len(str(n))

# Returns factorial of number
def factorial(n):
	out=1
	for x in range(1,abs(n)+1):
		out = out*x
	return out
	
# The combinatoric formula, that will work well for large n and reasonable r
def nCr(n,r):
	if n<r:
		return "n must be leq r"
	out=1
	for x in range(n-r+1,n+1):
		out = out*x
	return out/factorial(r)

# Returns all possible combinations of a list
def combinations(s): # Rename to subsets!!!!!
	yield []
	for i, d in enumerate(s):
		for comb in combinations(s[i+1:]):
			yield [d] + comb

# Returns whether a number is a palindrome
def isPalindromic(n):
	n=str(n)
	if n==''.join([n[-i-1] for i in range(len(n))]): return 1
	return 0

# Returns the reverse of an integer
def reverse(n):
	n=str(n)
	return int(''.join([n[-i-1] for i in range(len(n))]))

# Returns the digital sum of a number
def digSum(n):
	total = 0
	for m,n in enumerate(digSig(n)):
		total += m*n
	return total

# Returns whether a number is square
def isSquare(n):
	# Perfect squares end in 0, 1, 4, 9 in hexadecimal
	# Thus we check this first, then apply general method
	if hex(n)[-1] in ['0','1','4','9']:
		if int(n**0.5)**2 == n: return 1
	return 0
