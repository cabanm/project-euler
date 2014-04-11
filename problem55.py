from myMath import reverse, isPalindromic

count = 0
for n in range(10000):
	print n
	for i in range(50):
		tot = n + reverse(n)
#		print n, reverse(n), tot
#		raw_input()
		if isPalindromic(tot): # True = is not a Lychrel number
			break
		n = tot
	if i==49: count += 1 # Never formed a palindrome => is a Lychrel
print 'Lychrel numbers below 10,000:', count
