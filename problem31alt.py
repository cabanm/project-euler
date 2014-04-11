from time import time
start = time()

count = 1 # The 2 pound coin

for a in range(200/100+1):
	for b in range(200/50+1):
		for c in range(200/20+1):
			for d in range(200/10+1):
				for e in range(200/5+1):
					for f in range(200/2+1):
						for g in range(200/1+1):
							summ = a*100+b*50+c*20+d*10+e*5+f*2+g*1
							#print a,b,c,d,e,f,g
							if summ == 200: count += 1

print 'Total combinations:', count
print 'Time taken:', time()-start
