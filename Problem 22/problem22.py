from combSort import *
import string

valueMap = dict()
for index, letter in enumerate(string.ascii_uppercase):
    valueMap[letter] = index + 1

f = open('./names.txt', 'r')
names = sorted(f.read().lstrip('"').rstrip('"').split('","'))

#print(names)

totalScore = 0

for i in range(len(names)):
    name = names[i]
    nameScore = 0
    for j in range(len(name)):
        nameScore += valueMap[name[j]]
        #print(j, name[j], valueMap[name[j]])
    totalScore += (i+1)*nameScore
    #print(totalScore)
    if (i+1)//100 == (i+1)/100:
        print(i+1)
print('score', totalScore)
