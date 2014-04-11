# Find the sum of all the positive integers which
# cannot be written as the sum of two abundant numbers.
#
# Facts:
# All integers greater than 28123 can be
# written as the sum of two abundant numbers.
# Abundant number = sum of proper divisors of n exceed n.
#
# Find all abundant numbers up to and including 28123
# Add all combinations of these and store if not greater then 28123
# Add all integers <= 28123 not in the list to get required sum

from myMath import *

abundants = list()
for n in range(1, 28123 + 1):
    if sum(int(n).properDivisors()) > n:
        abundants.append(n)
print('stage 1 complete --', 'number of abundants = ', len(abundants))

sums = list()
for i, n in enumerate(abundants):
    for m in abundants[i:]:
        if n+m <= 28123:
            sums.append(n+m)
sums = sorted(set(sums))
print('stage 2 complete --', 'number of sums of abundants = ', len(sums))

sumsIndeces = [0]*(28123 + 1)
for i, n in enumerate(sums):
    sumsIndeces.pop(n)
    sumsIndeces.insert(n,1) # places a one at every index that is sum of abundants
    if i%1000 == 0:
        print(i)
print('stage 3 complete')

total = 0
for n in range(len(sumsIndeces)):
    if sumsIndeces[n] == 0:
        total += n
print('sum = ', total)
