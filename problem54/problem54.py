class hand:
    def __init__(self, string):
        self.values = None
        self.sets = None
        values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        suits = ['H','D','S','C']
        self.values = [string.count(x) for x in values]
        self.suits = [string.count(x) for x in suits]

def highCard(hand):
    for i,x in enumerate(hand):
        

def onepair(hand):
    return 2 in hand.values

def twopair(hand):
    return hand.values.count(2) == 2

def triple(hand):
    return 3 in hand.values

def straight(hand):
    for i in range(len(hand.values)-4):
        if hand.values[i:i+5] == [1]*5: return True
    return False

def flush(hand):
    if 5 in hand.suits: return (hand.suits.index(5))

def fullhouse(hand):
    return onepair(hand) and triple(hand)

def quad(hand):
    return 4 in hand.values

def str8flush(hand):
    return straight(hand) and flush(hand)

def royalflush(hand):
    return flush(hand) and hand.values[-5:] == [1]*5

def compareHighCards(hand1, hand2):
    high1 = high2 = 0
    if hand1.values.pop(-1) != 0: high1 = 1
    if hand2.values.pop(-1) != 0: high2 = 1
    if high1 > high2: return 0
    if high1 < high2: return 1
    compareHighCards(hand1, hand2)

def rank(hand):
    if royalflush(hand): return 9
    if str8flush(hand): return 8
    if quad(hand): return 7
    if fullhouse(hand): return 6
    if flush(hand): return 5
    if straight(hand): return 4
    if triple(hand): return 3
    if twopair(hand): return 2
    if onepair(hand): return 1
    return 0

f = open('poker.txt')

count1 = count2 = 0

for line in f:
    line = line.split()
    hand1 = hand(' '.join(line[:5]))
    hand2 = hand(' '.join(line[5:]))
    rank1 = rank(hand1)
    rank2 = rank(hand2)
    print rank1, rank2
    if rank1 > rank2:
        count1 += 1
        continue
    if rank1 < rank2:
        count2 += 1
        continue
    if compareHighCards(hand1, hand2) == 0:
        count1 += 1
    else:
        count2 += 1
    print count1, count2

f.close()
