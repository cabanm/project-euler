from time import time
start = time()

count = 1 # The 2 pound coin

for a in range(200/100+1):
	for b in range((200-a*100)/50+1):
		for c in range((200-b*50-a*100)/20+1):
			for d in range((200-c*20-b*50-a*100)/10+1):
				for e in range((200-d*10-c*20-b*50-a*100)/5+1):
					for f in range((200-e*5-d*10-c*20-b*50-a*100)/2+1):
						count += 1 # We can always complete our amount here with a bunch of ones

print 'Total combinations:', count
print 'Time taken:', time()-start
