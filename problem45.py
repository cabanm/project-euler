from time import time
from math import sqrt

start = time()

for q in range(143,100000):
	p=(1-sqrt(1-12*(-4*q**2+2*q)))/6
	if p>0 and p == int(p):
		n=(-1-sqrt(1-4*(-3*p**2+p)))/2
		if n>0 and n == int(n):
			print int(n),int(p),int(q)
			print int(n*(n+1)/2)
		n=(-1+sqrt(1-4*(-3*p**2+p)))/2
		if n>0 and n == int(n):
			print int(n),int(p),int(q)
			print int(n*(n+1)/2)
	p=(1+sqrt(1-12*(-4*q**2+2*q)))/6
	if p>0 and p == int(p):
		n=(-1-sqrt(1-4*(-3*p**2+p)))/2
		if n>0 and n == int(n):
			print int(n),int(p),int(q)
			print int(n*(n+1)/2)
		n=(-1+sqrt(1-4*(-3*p**2+p)))/2
		if n>0 and n == int(n):
			print int(n),int(p),int(q)
			print int(n*(n+1)/2)

print 'Done.'
print 'Time taken:', time()-start
