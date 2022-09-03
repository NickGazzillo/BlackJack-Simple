import random as r
simulationStand = []
decks = 6
games = 10000
sPCards = [10, 11]
sDCards = [10,7]
aPCards = []
aDCards = []
sSplitPCards = []
cardBase = 6 * [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
def sim_stand(sPCards, sDCards):
    while len(simulationStand) < games:
            # dealer sim
            while sum(sDCards) < 17:
                sDCards.append(r.choice(cardBase))
                i = len(sDCards) - 1
                cardBase.remove(sDCards[i])
            # if main deck loses
            if sum(sPCards) > 21 or (sum(sPCards) < sum(sDCards) and sum(sDCards) <=21):
                simulationStand.append(0)
                while len(sPCards) != 2:
                    i = len(sPCards) - 1
                    cardBase.append(sPCards[i])
                    sPCards.remove(sPCards[i])
                while len(sDCards) != 2:
                    i = len(sDCards) - 1
                    cardBase.append(sDCards[i])
                    sDCards.remove(sDCards[i])
            # if main deck wins
            elif sum(sDCards) > 21 or (sum(sPCards) > sum(sDCards) and sum(sPCards) <=21):
                simulationStand.append(1)
                while len(sPCards) != 2:
                    i = len(sPCards) - 1
                    cardBase.append(sPCards[i])
                    sPCards.remove(sPCards[i])
                while len(sDCards) != 2:
                    i = len(sDCards) - 1
                    cardBase.append(sDCards[i])
                    sDCards.remove(sDCards[i])
            # if side deck pushes with dealer
            elif sum(sPCards) == sum(sDCards):
                simulationStand.append(0)
                while len(sPCards) != 2:
                    i = len(sPCards) - 1
                    cardBase.append(sPCards[i])
                    sPCards.remove(sPCards[i])
                while len(sDCards) != 2:
                    i = len(sDCards) - 1
                    cardBase.append(sDCards[i])
                    sDCards.remove(sDCards[i])   
while len(sPCards) != 2:
    sDCards.append(r.choice(cardBase))
    sPCards.append(r.choice(cardBase))
    aPCards = sPCards.copy()
    aDCards = sDCards.copy()
sim_stand(sPCards, sDCards)  
stand = (sum(simulationStand) / len(simulationStand))
print('stand', stand)