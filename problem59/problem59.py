def decipher(ciphered_list, key):
    assert len(key) == 3, 'Key size must be 3'
    key_list = [ord(c) for c in key]
    text = ''
    for i in range(len(ciphered_list)):
        text += chr(key_list[i%3] ^ ciphered_list[i])
    return text

f = open('p059_cipher.txt')

ciphered_list = f.readline().strip().split(',')
ciphered_list = [int(s) for s in ciphered_list]
N = len(ciphered_list)
alphabet = range(97,123)


for l in alphabet:
    for m in alphabet:
        for n in alphabet:
            key = chr(l) + chr(m) + chr(n)
            text = decipher(ciphered_list, key)
            count = sum([text.count(s) for s in ['and','And','aNd','anD','ANd','AnD','aND','AND']])
            if count > 2:
                print key, count
                print text
                print 'sum:', sum([ord(c) for c in text]), '\n'

f.close()
