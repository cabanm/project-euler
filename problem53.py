# Solves Problem 53 of Project Euler

from myMath import nCr

total=0

for n in range(1,101):
	for r in range(0,n+1):
		print n,r
		if nCr(n,r)>1000000:
			total += n+1-2*r
			print total
#			raw_input()
			break
print "---------"
print total
