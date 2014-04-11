from time import time

# Dirty
# -----
start = time()
s = ''
n = 1
while len(s) < 1000000:
	s += str(n)
	n += 1
	#print s
product = 1
for p in range(7):
	product = product * int(s[10**p-1])
print 'Time taken, method 1:', time()-start
print product

# Nice
# ----

def nthDig(n):
	d=1
	#print 'Input:', n
	while n-9*10**(d-1)*d > 0:
		n -= 9*10**(d-1)*d
		d += 1
		#print n, d
	num = 10**(d-1)+(n-1)//d
	#print 'Number:', num
	#print 'Digit:', (n-1)%d
	return (num//10**(d-1-(n-1)%d))%10

start = time()
product = 1
for p in range(7):
	product = product * nthDig(10**p)
print 'Time taken, method 2:', time()-start
print product

