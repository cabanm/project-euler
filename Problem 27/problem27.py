# Considering quadratics of the form:

#    n**2 + an + b, where |a| < 1000 and |b| < 1000

#    where |n| is the modulus/absolute value of n
#    e.g. |11| = 11 and |-4| = 4

# Find the product of the coefficients, a and b,
# for the quadratic expression that produces the
# maximum number of primes for consecutive values of n, starting with n = 0.

import math

def prime(x): # returns 1 if x is prime, else 0
	x=abs(x)
	out = 1
	for i in range(2,x//2+1):
		if x%i==0: out = 0
	return out

def primeList(x): # Returns a list of all primes <= x
	x=abs(x)
	sieve=[]
	primes=[]
	for i in range(2,x//2+1):
		for j in range(i,x//i+1):
			sieve.append(i*j)
	sieve=sorted(set(sieve))
	for n in range(2,x+1):
		if len(sieve)!=0:
			if n!=sieve[0]:
				primes.append(n)
			else:
				del sieve[0]
	return primes

n_max=0
a_max=0
b_max=0

primes = primeList(999)
b_list = primes
b_list.extend([-1*x for x in primes])

a_list = range(-999,1000,2)

for b in sorted(b_list):
	for a in sorted(a_list):
		if not (a+1)%10: print b,a
		n = 0
		while prime(n**2+a*n+b):
			n+=1
		if n >= n_max:
			n_max = n
			a_max = a
			b_max = b

print ''
print 'Max consecutive primes:', n_max
print 'Coefficients:', a_max,b_max
print 'Product of coefficients:', a_max*b_max

