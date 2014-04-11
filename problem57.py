from myMath import digNum

expansions = range(1000) # expansion to do

count = 0 # counts the number of time numerator has more digits than denominator
for j in expansions:
	n = [1,2] # start
	for i in range(j-1):
		n[0] += 2*n[1] # add 2 to fraction
		n[0], n[1] = n[1], n[0] # invert fraction
	n[0] += n[1] # add 1 to fraction
	if digNum(n[0]) > digNum(n[1]):
		count += 1
		# print n[0],'/',n[1],'=',n[0]*1./n[1]
print 'Total number:', count
