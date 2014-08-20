class hand:
    def __init__(self, string):
        self.string = string
        self.values = None
        self.sets = None
        values = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
        suits = ['H','D','S','C']
        self.values = [string.count(x) for x in values]
        self.suits = [string.count(x) for x in suits]

def nthIndex(n, x, List):
    if n==-1: return len(List)-List[::-1].index(x)-1
    last = 0
    for i in range(n):
        last = List.index(x, last) + 1
    return last-1

def onepair(hand):
    if 2 in hand.values:
        return [1, hand.values.index(2)]
    return []

def twopair(hand):
    if hand.values.count(2) == 2:
        return [2, nthIndex(2,2,hand.values), nthIndex(1,2,hand.values)]
    return []

def triple(hand):
    if 3 in hand.values:
        return [3, hand.values.index(3)]
    return []

def straight(hand):
    for i in range(len(hand.values)-4):
        if hand.values[i:i+5] == [1]*5:
            return [4, nthIndex(-1,1,hand.values)]
    return []

def flush(hand):
    if 5 in hand.suits: return [5, nthIndex(-1,1,hand.values)]
    return []

def fullhouse(hand):
    if onepair(hand)!=[] and triple(hand)!=[]:
        return [6, hand.values.index(3), hand.values.index(2)]
    return []

def quad(hand):
    if 4 in hand.values: return [7, hand.values.index(4)]
    return []

def str8flush(hand):
    if straight(hand)!=[] and flush(hand)!=[]:
        return [8, nthIndex(-1,1,hand.values)]
    return []

def royalflush(hand):
    if flush(hand) and hand.values[-5:] == [1]*5: return [9]
    return []

def rank(hand):
    plays = [royalflush, str8flush, quad, fullhouse, flush, straight, triple, twopair, onepair]
    for fn in plays:
        score = fn(hand)
        if len(score)!=0: break
    if len(score)==0: score=[0]
    return score + [1 if x>0 else 0 for x in hand.values[::-1]]

f = open('poker.txt')

count1 = count2 = 0

for line in f:
    line = line.split()
    hand1 = hand(' '.join(line[:5]))
    hand2 = hand(' '.join(line[5:]))
    rank1 = rank(hand1)
    rank2 = rank(hand2)
    print rank1
    print rank2
    for i in range(len(rank1)):
        if rank1[i]>rank2[i]:
            count1 += 1
            break
        elif rank2[i]>rank1[i]:
            count2 += 1
            break
    print count1, count2

f.close()
