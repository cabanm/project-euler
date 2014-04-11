from time import time

start = time()

f = open('words.txt')
words = [w[1:-1] for w in f.readline().split(',')]

#words = ['SKY']

for i, word in enumerate(words):
	n = 0
	for c in word:
		n += ord(c)+1-ord('A') # normalize the ord function so 'A' gives 1
	words[i] = n

n, t = 1, 1
triangles = []
while t <= max(words):
	triangles.append(int(t))
	n += 1
	t = 1.0/2*n*(n+1)

n = 0
for t in triangles:
	print t, n, words.count(t)
	n += words.count(t)
print n

print 'Result:', n
print 'Found in:', time()-start
