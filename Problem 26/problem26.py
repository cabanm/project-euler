# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

maxi=[0,0]
for d in range(1,1001):
	rems=[]
	r=1

	while rems.count(r)<=1 and r!=0:
		if r//d==0:
			r=r*10
		else:
			r=r%d
			rems.append(r)

	if r!=0:
		dist = rems[rems.index(r)+1:].index(r)+1
		if dist > maxi[1]: maxi=[d,dist]
		print d, '--->', dist
	else:
		print d, '---> 0'
print ''
print 'Largest recurring sequence at', maxi[0], 'with size', maxi[1]
