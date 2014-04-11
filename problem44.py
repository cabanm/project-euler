from time import time
from myMath import isPent
from math import sqrt

start = time()

l, D_min = 5000, 10**10

pents = [n*(3*n-1)/2 for n in xrange(1,l+1)]
for j in xrange(1,l):
	for k in xrange(j+1, l):
		D = pents[k]-pents[j]
		if isPent(D) and isPent(pents[j]+pents[k]):
			print pents[j],pents[k],D
			if D < D_min: D_min = D

print 'Lowest difference:', D_min
print 'Time taken:', time()-start

D_min = 10**10

start = time()
for j in xrange(1,l):
	for k in xrange(j+1,l):
		if sqrt(1.+12*(k*(3*k-1)-j*(3*j-1)))%6 == 5:
			if sqrt(1.+12*(j*(3*j-1)+k*(3*k-1)))%6 == 5:
				D = k*(3*k-1)/2-j*(3*j-1)/2
				print k*(3*k-1)/2, j*(3*j-1)/2, D
				if D < D_min: D_min = D

print 'Lowest difference:', D_min
print 'Time taken:', time()-start
