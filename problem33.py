cur_fracs = []
for q in range(11,99):
	for p in range(10,q):
		try:
			if p-10*(p//10) == 0 and q-10*(q//10) == 0: continue
			if p//10 == q//10 and float(p)/q == float(p-10*(p//10))/(q-10*(q//10)):
				cur_fracs.append([p, q])
				continue
			if p//10 == q-10*(q//10) and float(p)/q == float(p-10*(p//10))/(q//10):
				cur_fracs.append([p, q])
				continue
			if p-10*(p//10) == q//10 and float(p)/q == float(p//10)/(q-10*(q//10)):
				cur_fracs.append([p, q])
				continue
			if p-10*(p//10) == q-10*(q//10) and float(p)/q == float(p//10)/(q//10):
				cur_fracs.append([p, q])
				continue
		except ZeroDivisionError:
			continue
print cur_fracs
