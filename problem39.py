from time import time
from myMath import pythTripsPerim
start = time()

maximum = [0, 0]
perims = [sum(x) for x in pythTripsPerim(1000)]

for l in [[x, perims.count(x)] for x in perims]:
	if l[1] > maximum[1]: maximum = l

print 'Number of triples maximized at perimeter', maximum[0], 'with', maximum[1]
print 'Time taken:', time()-start
