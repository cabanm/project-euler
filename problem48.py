#total = 0
#for n in range(1, 1001):
#	prod = 1
#	for i in range(1,n+1):
#		prod = n*prod%10**10
#	total += prod
#print total%10**10

print sum([reduce(lambda p, prod: p*prod%10**10, n*[n]) for n in range(1, 1001)])%10**10
