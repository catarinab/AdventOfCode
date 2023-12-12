'''
five of a kind -> 0
four of a kind -> 1
full house -> 2
three of a kind -> 3
two pair -> 4
one pair -> 5
high card -> 6
'''


cardValues = {"A": 12, "K": 11, "Q": 10, "T": 8, "9": 7, "8": 6, "7": 5, "6": 4, "5": 3, "4": 2, "3": 1, "2": 0, "J": -1}

class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.type = 6
        self.freq = []
        self.jokerFreq = 0
    
    def __str__(self):
        return "Bid: " + str(self.bid) + ", cards:" + str(self.cards) + ", type:" + str(self.type) + ", frequencies:" + str(self.freq)
    
    def __lt__(self, other):
        if(self.type == other.type):
            for idx in range(5):
                if(self.cards[idx] != other.cards[idx]):
                    return cardValues[self.cards[idx]] < cardValues[other.cards[idx]]
            return False
        else:
            return self.type > other.type
    
    def checkFrequency(self):
        freqs = {}
        jokerFreq = 0
        for card in self.cards:
            if(card == "J"):
                jokerFreq += 1
                continue
            if(card not in freqs):
                freqs[card] = 1
            else:
                freqs[card] += 1
        self.freq = sorted(freqs.items(), key=lambda x:x[1], reverse=True)
        self.jokerFreq = jokerFreq
    

    def checkType(self):
        if(self.checkFiveOfAKind()):
            return
        elif(self.checkFourOfAKind()):
            return
        elif(self.checkFullHouse()):
            return
        elif(self.checkThreeOfAKind()):
            return
        elif(self.checkTwoPair()):
            return
        elif(self.checkOnePair()):
            return
    
    def checkFiveOfAKind(self):
        if(self.jokerFreq == 5 or self.freq[0][1] == 5 or self.freq[0][1] + self.jokerFreq == 5):
            self.type = 0
            return True
        return False
    
    
    def checkFourOfAKind(self):
        if(self.jokerFreq == 4 or self.freq[0][1] == 4 or (self.freq[0][1] + self.jokerFreq == 4)):
            self.type = 1
            return True
        return False
    

    def checkFullHouse(self):
        if(len(self.freq) < 2):
            if((self.freq[0][1] == 3 and self.jokerFreq == 2) or (self.freq[0][1] == 2 and self.jokerFreq == 3)):
                self.type = 2
                return True
            return False
        

        if(self.freq[0][1] == 3 and self.freq[1][1] == 2):
            self.type = 2
            return True
        
        dist1 = 3 - self.freq[0][1]
        dist2 = 2 - self.freq[1][1]
        if(dist1 + dist2 <= self.jokerFreq):
            self.type = 2
            return True
        
        return False
    
    
    def checkThreeOfAKind(self):
        if(self.jokerFreq == 3 or self.freq[0][1] == 3 or self.freq[0][1] + self.jokerFreq == 3):
            self.type = 3
            return True
        return False
    
    
    def checkTwoPair(self):
        if(len(self.freq) < 2):
            if(self.freq[0][1] == 2 and self.jokerFreq == 2):
                self.type = 2
                return True
            return False
        

        if(self.freq[0][1] == 2 and self.freq[1][1] == 2):
            self.type = 4
            return True
        
        dist1 = 2 - self.freq[0][1]
        dist2 = 2 - self.freq[1][1]
        if(dist1 + dist2 <= self.jokerFreq):
            self.type = 4
            return True
        return False
    
    
    def checkOnePair(self):
        if(self.freq[0][1] == 2 or self.freq[0][1] + self.jokerFreq == 2):
            self.type = 5
            return True
        else:
            return False




f = open("inputs/day7test.txt", "r")
lines = f.readlines()
f.close()

hands = []

for line in lines:
    hand = line.split(" ")
    bid = hand[1]
    hand = Hand([*hand[0]], bid)
    hand.checkFrequency()
    hand.checkType()
    hands.append(hand)

hands.sort()
res = 0
for i in range(len(hands)):
    res += (i+1) * int(hands[i].bid)
print(res)



