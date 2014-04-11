total = 0
for n in range(2,10000000):
	#if not(n%1000): print n
	if sum([int(c)**5 for c in list(str(n))]) == n:
		print n
		total += n
print 'Sum:', total
