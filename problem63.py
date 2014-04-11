from myMath import digNum

count = 0
for b in range(1,22):
	for a in range(1,10):
		if digNum(a**b) == b: count += 1
print 'Total:', count
