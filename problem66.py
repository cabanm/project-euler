from myMath import isSquare

x2max = 0
Dmax = 0

def search(D):
	i = 0 # counter
	x = 2
	while i < 10000000:
		x2 = x*x
		if (x2-1)%D == 0:
	                if isSquare((x2-1)/D):
        			return x2
		x += 1
		i += 1
	return None

for D in range(1,1001):
	if isSquare(D): continue
	x2 = search(D)
	if x2 == None: continue # occurs for non-squares that don't have a solution
	print x2, D
	if x2 > x2max:
		x2max = x2
		Dmax = D
	

print 'xMax^2 =', x2max, 'occurs for D =', Dmax
