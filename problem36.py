total = 0
for n10 in range(1, 1000000, 2):
	n10s = str(n10)
	if n10s == n10s[::-1]:
		n2 = bin(n10)[2:]
		if n2 == n2[::-1]:
			total += n10
print total
