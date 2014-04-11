# Solves Problem 52 - Permuted multiples
from time import time
from myMath import digSig

start = time()

for n in xrange(1,1000000):
	if digSig(n) == digSig(2*n) == digSig(3*n) == digSig(4*n) == digSig(5*n) == digSig(6*n): break
print n
print 'Time taken:', time()-start
