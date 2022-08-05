import random as r

dealerCard = []
playerCard = []
cardBase = 6 * [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
cardCount = []
cardCountNum = 0
originalDCard = []
originalPCard = []
# while len(playerCard) != 2:
# i = len(playerCard)
# dealerCard.append(r.choice(cardBase))
# playerCard.append(r.choice(cardBase))
# while len(cardBase):
# i = len(playerCard)
# cardBase.remove(dealerCard[i])
# cardBase.remove(playerCard[i])
# cardCount.append(dealerCard[i])
# cardCount.append(playerCard[i])
# for x in cardCount:
#   if 2 <= x <= 6:
#      cardCountNum += 1
# elif 10 <= x <= 11:
#    cardCountNum -= 1

simulationSplit = []
splitSimulationSplit = []
decks = 6
games = 10000
sPCards = [2, 2]
sDCards = [2]
aPCards = [2, 2]
aDCards = []
sSplitPCards = []
weightedCardAverage = ((2 * cardBase.count(2) + 3 * cardBase.count(3) + 4 * cardBase.count(4) + 5 * cardBase.count(
    5) + 6 * cardBase.count(6) + 7 * cardBase.count(7) + 8 * cardBase.count(8) + 9 * cardBase.count(
    9) + 10 * cardBase.count(10) + 11 * cardBase.count(11)) / (decks * 13))

while len(sDCards) != 2:
    sDCards.append(r.choice(cardBase))

if aPCards[0] == aPCards[1]:
    sSplitPCards = sPCards.copy()
    sPCards.remove(sPCards[1])
    sSplitPCards.remove(sSplitPCards[1])
    sPCards.append(r.choice(cardBase))
    sSplitPCards.append(r.choice(cardBase))
    while len(simulationSplit) < games:
        # main deck split sim
        while (weightedCardAverage + sum(sPCards)) <= 21:
            sPCards.append(r.choice(cardBase))
            weightedCardAverage = ((2 * cardBase.count(2) + 3 * cardBase.count(3) + 4 * cardBase.count(4) + 5 * cardBase.count(
            5) + 6 * cardBase.count(6) + 7 * cardBase.count(7) + 8 * cardBase.count(8) + 9 * cardBase.count(
            9) + 10 * cardBase.count(10) + 11 * cardBase.count(11)) / (len(cardBase)))
            i = len(sPCards) - 1
            cardBase.remove(sPCards[i])
        # dealer sim
        while sum(sDCards) < 17:
            sDCards.append(r.choice(cardBase))
            i = len(sDCards) - 1
            cardBase.remove(sDCards[i])
        # if main deck wins
        if sum(sPCards) <= 21 and sum(sPCards) > sum(sDCards):
            simulationSplit.append(1)
            while len(sPCards) != 2:
                i = len(sPCards) - 1
                cardBase.append(sPCards[i])
                sPCards.remove(sPCards[i])
            while len(sDCards) != 2:
                i = len(sDCards) - 1
                cardBase.append(sDCards[i])
                sDCards.remove(sDCards[i])
        # if main deck busts
        elif sum(sPCards) > 21:
            simulationSplit.append(0)
            while len(sPCards) != 2:
                i = len(sPCards) - 1
                cardBase.append(sPCards[i])
                sPCards.remove(sPCards[i])
            while len(sDCards) != 2:
                i = len(sDCards) - 1
                cardBase.append(sDCards[i])
                sDCards.remove(sDCards[i])
        # if main deck loses
        elif sum(sPCards) <= 21 and sum(sPCards) < sum(sDCards):
            simulationSplit.append(0)
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
            simulationSplit.append(0.5)
            while len(sPCards) != 2:
                i = len(sPCards) - 1
                cardBase.append(sPCards[i])
                sPCards.remove(sPCards[i])
            while len(sDCards) != 2:
                i = len(sDCards) - 1
                cardBase.append(sDCards[i])
                sDCards.remove(sDCards[i])           
    while len(splitSimulationSplit) < games:
        # side deck split sim
        while (weightedCardAverage + sum(sSplitPCards)) <= 21:
            sSplitPCards.append(r.choice(cardBase))
            weightedCardAverage = ((2 * cardBase.count(2) + 3 * cardBase.count(3) + 4 * cardBase.count(4) + 5 * cardBase.count(
            5) + 6 * cardBase.count(6) + 7 * cardBase.count(7) + 8 * cardBase.count(8) + 9 * cardBase.count(
            9) + 10 * cardBase.count(10) + 11 * cardBase.count(11)) / (len(cardBase)))
            i = len(sSplitPCards) - 1
            cardBase.remove(sSplitPCards[i])
        # dealer sim
        while sum(sDCards) < 21:
            sDCards.append(r.choice(cardBase))
            i = len(sDCards) - 1
            cardBase.remove(sDCards[i])
        # if side deck wins
        if sum(sSplitPCards) <= 21 and sum(sSplitPCards) > sum(sDCards):
            splitSimulationSplit.append(1)
            while len(sSplitPCards) != 2:
                i = len(sSplitPCards) - 1
                cardBase.append(sSplitPCards[i])
                sSplitPCards.remove(sSplitPCards[i])
            while len(sDCards) != 2:
                i = len(sDCards) - 1
                cardBase.append(sDCards[i])
                sDCards.remove(sDCards[i])
        # if side deck busts
        elif sum(sSplitPCards) > 21:
            splitSimulationSplit.append(0)
            while len(sSplitPCards) != 2:
                i = len(sSplitPCards) - 1
                cardBase.append(sSplitPCards[i])
                sSplitPCards.remove(sSplitPCards[i])
            while len(sDCards) != 2:
                i = len(sDCards) - 1
                cardBase.append(sDCards[i])
                sDCards.remove(sDCards[i])
        # if side deck loses
        elif sum(sSplitPCards) <= 21 and sum(sSplitPCards) < sum(sDCards):
            splitSimulationSplit.append(0)
            while len(sSplitPCards) != 2:
                i = len(sSplitPCards) - 1
                cardBase.append(sSplitPCards[i])
                sSplitPCards.remove(sSplitPCards[i])
            while len(sDCards) != 2:
                i = len(sDCards) - 1
                cardBase.append(sDCards[i])
                sDCards.remove(sDCards[i])
        # if side deck pushes with dealer
        elif sum(sSplitPCards) == sum(sDCards):
            splitSimulationSplit.append(0.5)
            while len(sSplitPCards) != 2:
                i = len(sSplitPCards) - 1
                cardBase.append(sSplitPCards[i])
                sSplitPCards.remove(sSplitPCards[i])
            while len(sDCards) != 2:
                i = len(sDCards) - 1
                cardBase.append(sDCards[i])
                sDCards.remove(sDCards[i])   
split = (sum(simulationSplit) / len(simulationSplit))
simulationSplit = sum(splitSimulationSplit) / len(splitSimulationSplit)
split += simulationSplit 
print('split', split)
