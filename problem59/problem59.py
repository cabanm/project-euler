def xor(m,n):
	out = '0b'
	m = bin(m)[2:]
	n = bin(n)[2:]
	lenm = len(m)
	lenn = len(n)
	if lenm > lenn:
		for i in range(lenm-lenn):
			n += n[i]
	if lenn > lenm:
		for i in range(lenn-lenm):
			m += '0'+m
	return int('0b'+''.join([str(int(i!=j)) for i,j in zip(m,n)]),2)
