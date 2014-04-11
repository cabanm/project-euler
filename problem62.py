from myMath import digSig

d = {}
n = 0
size = 0

while size < 5:
	sig = tuple(digSig(n**3)) # store signature of the number's cube
	if sig not in d: d[sig] = [] # if the signature is not in our database, add it
	d[sig].append(n) # add the current number - every number here has same sig of it's cube
	n += 1 # next number
	size = len(d[sig])
print 'Set of cube roots:', d[sig]
print 'Smallest cube:', d[sig][0]**3
