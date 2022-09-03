import random as r
simulationHit = []
decks = 6
games = 10000
sPCards = [2, 2]
sDCards = [2]
aPCards = [2, 2]
aDCards = [2]
sSplitPCards = []
cardBase = 6 * [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
weightedCardAverage = ((2 * cardBase.count(2) + 3 * cardBase.count(3) + 4 * cardBase.count(4) + 5 * cardBase.count(
    5) + 6 * cardBase.count(6) + 7 * cardBase.count(7) + 8 * cardBase.count(8) + 9 * cardBase.count(
    9) + 10 * cardBase.count(10) + 11 * cardBase.count(11)) / (decks * 13))

def sim_hit(sPCards, sDCards, aPCards):
    #simulationHit
    while len(simulationHit) < games:
        if len(sPCards) != len(aPCards):
            sPCards.append(r.choice(cardBase))
            i = len(sPCards) - 1
            cardBase.remove(sPCards[i])
        # dealer sim
        while sum(sDCards) < 17:
            sDCards.append(r.choice(cardBase))
            i = len(sDCards) - 1
            cardBase.remove(sDCards[i])
        # if main deck wins
        if sum(sPCards) <= 21 and sum(sPCards) > sum(sDCards) or sum(sDCards) > 21:
            simulationHit.append(1)
            while len(sPCards) != 2:
                i = len(sPCards) - 1
                cardBase.append(sPCards[i])
                sPCards.remove(sPCards[i])
            while len(sDCards) != 2:
                i = len(sDCards) - 1
                cardBase.append(sDCards[i])
                sDCards.remove(sDCards[i])
        # if main deck loses
        if sum(sPCards) <= 21 and sum(sPCards) < sum(sDCards) or sum(sPCards) > 21:
            simulationHit.append(-1)
            while len(sPCards) != 2:
                i = len(sPCards) - 1
                cardBase.append(sPCards[i])
                sPCards.remove(sPCards[i])
            while len(sDCards) != 2:
                i = len(sDCards) - 1
                cardBase.append(sDCards[i])
                sDCards.remove(sDCards[i])
        # if side deck pushes with dealer
        if sum(sPCards) == sum(sDCards):
            simulationHit.append(0)
            while len(sPCards) != 2:
                i = len(sPCards) - 1
                cardBase.append(sPCards[i])
                sPCards.remove(sPCards[i])
            while len(sDCards) != 2:
                i = len(sDCards) - 1
                cardBase.append(sDCards[i])
                sDCards.remove(sDCards[i])
    hit = (sum(simulationHit) / len(simulationHit))
    print('hit', hit) 
    simulationHit.clear()
while len(sPCards) != 2:
    sDCards.append(r.choice(cardBase))
    sPCards.append(r.choice(cardBase))
    aPCards = sPCards.copy()
    aDCards = sDCards.copy()     
sim_hit(sPCards, sDCards, aPCards)