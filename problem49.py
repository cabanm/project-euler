# Solves Project Euler problem 49

from myMath import digSig, primesNum

primes = primesNum(9999)
primes = [p for p in primes if p>999]

sigs = [digSig(p) for p in primes]


for m in sigs:
	seq = []
	for i,n in enumerate(sigs):
		if m==n:
			seq.append(primes[i])
	for j in seq:
		for k in seq:
			if j==k: continue
			for l in seq:
				if l==k: continue
				if l-k<0: continue
				if l-k==k-j:
					print j,k,l
					print str(j)+str(k)+str(l)
		
		
		
