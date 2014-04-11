from math import factorial

total = 0
dict = {}
for i in range(10):
	dict[str(i)] = factorial(i)

for n in range(3,1000000):
	if not(n%10000): print n
	if sum([dict[c] for c in list(str(n))]) == n:
		print '----->', n
		total += n
print 'Sum', total