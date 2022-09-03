import random as r

cardBase = 6 * [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
cardCount = []
cardCountNum = 0
decks = 6
games = 10000
sPCards = [5,6]
sDCards = [2]
aPCards = [5,6]
aDCards = [2]
simulationDouble = []
def sim_double(sPCards, sDCards, aPCards):
        # simulationDouble
    while len(simulationDouble) < games and len(aPCards) == 2:
        if len(sPCards) == 2:
            sPCards.append(r.choice(cardBase))
            i = len(sPCards) - 1
            cardBase.remove(sPCards[i])
        # dealer sim
        while sum(sDCards) < 17:
            sDCards.append(r.choice(cardBase))
            i = len(sDCards) - 1
            cardBase.remove(sDCards[i])
        # if main double deck loses
        if sum(sPCards) > 21 or (sum(sPCards) < sum(sDCards) and sum(sDCards) <=21):
            simulationDouble.append(-2)
            while len(sPCards) != 2:
                i = len(sPCards) - 1
                cardBase.append(sPCards[i])
                sPCards.remove(sPCards[i])
            while len(sDCards) != 2:
                i = len(sDCards) - 1
                cardBase.append(sDCards[i])
                sDCards.remove(sDCards[i])
        # if main double deck wins
        elif sum(sDCards) > 21 or (sum(sPCards) > sum(sDCards) and sum(sPCards) <=21):
            simulationDouble.append(2)
            while len(sPCards) != 2:
                i = len(sPCards) - 1
                cardBase.append(sPCards[i])
                sPCards.remove(sPCards[i])
            while len(sDCards) != 2:
                i = len(sDCards) - 1
                cardBase.append(sDCards[i])
                sDCards.remove(sDCards[i])
        # if main double deck pushes with dealer
        elif sum(sPCards) == sum(sDCards):
            simulationDouble.append(0)
            while len(sPCards) != 2:
                i = len(sPCards) - 1
                cardBase.append(sPCards[i])
                sPCards.remove(sPCards[i])
            while len(sDCards) != 2:
                i = len(sDCards) - 1
                cardBase.append(sDCards[i])
                sDCards.remove(sDCards[i])
    double = (sum(simulationDouble) / len(simulationDouble))
    print('double', double)
    simulationDouble.clear()
while len(sPCards) != 2:
    sDCards.append(r.choice(cardBase))
    sPCards.append(r.choice(cardBase))
    aPCards = sPCards.copy()
    aDCards = sDCards.copy()
sim_double(sPCards, sDCards, aPCards)

