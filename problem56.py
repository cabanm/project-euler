from myMath import digSum

mmax = 0
for a in range(100):
	for b in range(100):
		m = digSum(a**b)
		if m > mmax: mmax = m
print mmax
