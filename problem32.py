sums = []
for m in range(1,10000):
	print '-----', m
	for n in range(m,10000):
		p = m*n
		nums = list(str(m)+str(n)+str(p))
		if len(nums) == 9:
			nums.sort()
			if nums == ['1','2','3','4','5','6','7','8','9']:
				print p
				sums.append(p)
print sum(set(sums))
