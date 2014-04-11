# Find primes up to a certain number and output a list of them as strings
def primes(top):
	seive = range(2, top+1)
	for m in range(2, top+1):
		for n in range(m, top//m+1):
			p = m*n
			if p<=top: seive[p-2] = 0
	primes = []
	for i in range(top-1):
		if seive[i] != 0: primes.append(str(seive[i]))
	return primes

prime_list = primes(1000000)

# Clear primes with any even number
i = 0
while True:
	try:
		p = prime_list[i]
		if p.count('0') != 0:
			prime_list.pop(i)
			continue
		if p.count('2') != 0:
			prime_list.pop(i)
			continue
		if p.count('4') != 0:
			prime_list.pop(i)
			continue
		if p.count('6') != 0:
			prime_list.pop(i)
			continue
		if p.count('8') != 0:
			prime_list.pop(i)
			continue
		i += 1
	except IndexError:
		break

# 2 will have been removed, so add it back
prime_list.append('2')

# Solve problem
circular_primes = []
for p in prime_list:
	print 'Current prime:', p
	if p not in circular_primes:
		perms = [p]
		for i in range(len(p)-1):
			p = p[1:]+p[0]
			if p in prime_list: perms.append(p)
		if len(perms) == len(p):
			circular_primes.extend(perms)
			print 'Added'

circular_primes = set(circular_primes)
print circular_primes
print 'Answer:', len(circular_primes)
