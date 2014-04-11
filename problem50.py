# Solves Problem 50 - Consecutive prime sum

from myMath import primesNum

primesOrig = primesNum(1000000)
print 'Primes generated'

i_max = 0
for start in range(1000000):
	primes = primesOrig[start:]
	p = primes[0]
	prod = i_max*p
	print i_max, p, prod
	if prod > 1000000: break
	S = 0
	for i in range(len(primes)):
		if S >= 1000000: break
		if S in primes and i > i_max:
			i_max = i
			print S, i
		S += primes.pop(0)
print 'Done'
