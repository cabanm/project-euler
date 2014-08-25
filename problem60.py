from myMath import primes, isPrime, nCr
from itertools import combinations
from time import time

def valid_pair(x,y):
    if isPrime(int(x + y)) and isPrime(int(y + x)): return True
    return False

start = time()

P = 10000

plist = primes(P)
plist.pop(0) # rid of 2
plist.pop(1) # rid of 5

valid_pairs = {}
print 'Searching through...', nCr(P, 2)
for subset in combinations(plist, 2):
    if valid_pair(subset[0], subset[1]): valid_pairs[subset] = 0
print 'All pairs found: ', len(valid_pairs)
print 'time: ', time()-start

valid_fours = []
print 'Searching through...', nCr(len(valid_pairs), 2)
for subset in combinations(valid_pairs, 2):
    if set(subset[0] + subset[1]) in valid_fours: continue
    count = 0
    for x in subset[0]:
        for y in subset[1]:
            if x != y:
                if (x,y) in valid_pairs or (y,x) in valid_pairs: count += 1
    if count == 4: valid_fours.append(set(subset[0] + subset[1]))
print 'All fours found: ', len(valid_fours)
print 'time: ', time()-start

valid_fives = []
print 'Searching through...', len(valid_fours)*P
for four in valid_fours:
    for p in plist:
        count = 0
        for n in four:
            if (n,p) in valid_pairs or (p,n) in valid_pairs: count += 1
        if count == 4: valid_fives.append(list(four) + [p])
print 'Done.'
print 'time: ', time()-start

assert(len(valid_fives) != 0), 'No five valid primes found. Increase prime range.'
sums = [sum([int(n) for n in s]) for s in valid_fives]
print 'Smallest sum:', min(sums)
print 'The primes:', valid_fives[sums.index(min(sums))]

# ------------------------------------------------------------
# The brue-force approach that didn't even finish in one night
# ------------------------------------------------------------

#for subset in combinations(plist, N):
#    print subset
#    good_pairs = 0
#    for pair in combinations(subset, 2):
#        if not isPrime(int(pair[0] + pair[1])): break
#        if not isPrime(int(pair[1] + pair[0])): break
#        good_pairs += 1
#    print good_pairs
#    if good_pairs == nCr(N, 2):
#        print subset, sum([int(s) for s in subset])
#        print 'time:', time()-start
#        break
