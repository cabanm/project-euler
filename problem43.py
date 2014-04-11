from time import time
from itertools import permutations

start = time()

summ = 0
for seq in permutations([1,2,3,4,5,6,7,8,9,0]):
	seq = list(seq)
	if seq[3]%2 != 0: continue
	if (seq[2]+seq[3]+seq[4])%3 != 0: continue
	if seq[5]%5 != 0: continue
	if (seq[4]*100+seq[5]*10+seq[6])%7 != 0: continue
	if (seq[5]*100+seq[6]*10+seq[7])%11 != 0: continue
	if (seq[6]*100+seq[7]*10+seq[8])%13 != 0: continue
	if (seq[7]*100+seq[8]*10+seq[9])%17 != 0: continue
	for i,x in enumerate(seq):
		summ += x*10**(9-i)

print 'Result:', summ
print 'Time taken:', time()-start
