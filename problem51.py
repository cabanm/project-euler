from myMath import primes, isPrime, combinations

abc = 0

print 'Generating primes...'
Primes = primes(1000000)

# This block stores the primes in a dictionary rather than a list.
# It makes "s in Primes" run super fast.
# We equally avoid having to run isPrime(s).
# ------------------------------------------
di = {}
for p in Primes:
	di[p]=0
Primes = di

print 'Done!'
for p in Primes:
#	print 'Prime:', p
	l = list(str(p))
	for comb in combinations(range(len(l))):
		if comb==[]: continue
#		print comb
		col = []
		for x in range(10):
			s = l[:]
			# replace positions (perm) of p by x
			for d in comb:
				s[d] = str(x)
			# check if we shortened the number of digits and if so, ignore this num
			if s[0]=='0': continue
			s = ''.join(s)
#			print s
			if s in Primes: col.append(s)
#		print 'This family:', len(col)
#		raw_input()
		if len(col)==8:
			print 'Found it!', col
			abc = 1
			break
	if abc==1: break
	
