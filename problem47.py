# Solves Problem 47 - Distinct primes factors

from time import time
from myMath import primesNum, pFactors, pFactors2

# Slow shit
# ---------
start = time()

primes = primesNum(1000000)

cnsc = 0 # consecutive numbers to have 4 divisors

for n in range(1,1000000):
	if len(list(set(pFactors(n, primes)))) == 4:
		cnsc += 1
	else:
		cnsc = 0
	if cnsc == 4: break
print n-3

print 'Time taken:', time()-start
# ---------

# Fast? Yeah, fast.
# -----------------
start = time()
sieve = pFactors2(1000000)
for i in range(1000000-3):
	if sieve[i]==4 and sieve[i+1]==4 and sieve[i+2]==4 and sieve[i+3]==4: break
print i+1
	
print 'Time taken:', time()-start
# -----------------
