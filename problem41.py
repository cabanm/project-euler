from math import sqrt
from time import time

def isPandigital(n):
    n = str(n)
    if n.count('0') != 0: return 0
    for digit in range(1,8):
        if n.count(str(digit)) != 1:
            return 0
    return 1

def pandigitPrimes(top):
	seive = list(range(2, top+1))
	print('Creating seive...')
	for m in range(2, top+1):
	    for n in range(m, top//m+1):
                p = m*n
                if p<=top: seive[p-2] = 0
	primes = []
	print('Done.')
	for i in range(top-1):
		if seive[i] != 0 and isPandigital(seive[i]): primes.append(seive[i])
	return primes

print(pandigitPrimes(7654321)[-1])
