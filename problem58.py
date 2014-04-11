from myMath import isPrime

ndiag = 0
nprime = 0
l = 0 # starting layer
n = 1 # starting number is the center

ratio = 1.
while ratio >= 0.1:
	if ndiag%4 == 0: l += 1 # move to next layer every four diagonal numbers
	n += 2*l # move to next diagonal number
	ndiag += 1 # increase number of diagonals traversed
	if isPrime(n): nprime += 1 # if prime, increase their count
	if ndiag%4 == 0: # run only when a loop is complete
		ratio = nprime*1./(ndiag+1) # update ratio, include the starting "1" in the diagonal count
		print 'Last number:', n, '   Layer:', l, '   Side length:', 2*l+1, '   Ratio:', ratio
