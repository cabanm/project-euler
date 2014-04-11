def isPandigit(n):
	n = str(n)
	if n.count('0') != 0: return 0
	for digit in range(1,10):
		if n.count(str(digit)) != 1:
			return 0
	return 1

mult = [1]
maxi = 0
conctd = 0

a=2
while conctd < 987654321:
	mult += [a]
	a += 1
	for n in range(10**(9//mult[-1]-1), 10**(9//mult[-1]+1)):
		conctd = ''
		for m in mult:
			conctd += str(n*m)
		conctd = int(conctd)
		if isPandigit(conctd) and conctd > maxi: maxi = conctd
		print maxi


