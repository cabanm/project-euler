from myMath import *
pList = primes(1000000)

# Filter through primes list
i=0
while True:
	try:
		p = pList[i]
		if p[0]==1 or p[-1:]==1 or ('2' in p and p[0] != '2') or '4' in p or '6' in p or '8' in p or '0' in p:
			del pList[i]
			continue
		i+=1
	except: break

nums = []
for p in pList[4:]:
	nums.append(p)
	for i in range(len(p)-1):
		if p[i+1:] not in pList or p[:-i-1] not in pList:
			nums.remove(p)
			break
print nums
print 'Sum:', sum([int(s) for s in nums])
