import random as r
# simulation loops
simulationSplit = []
simulationDouble = []
simulationHit = []
simulationStand = []
splitSimulationSplit = []
# cardbase lists and other variable's
sDCards = []
sPCards = []
sSplitPCards = []
aDCards = []
aPCards = []
aSplitPCards = []
J = 10
Q = 10
K = 10
A = 11
decks = 6
games = 1
cardBaseOG = decks * [2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A]
cardBase = decks * [2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A]
weightedCardAverage = ((2 * cardBase.count(2) + 3 * cardBase.count(3) + 4 * cardBase.count(4) + 5 * cardBase.count(
    5) + 6 * cardBase.count(6) + 7 * cardBase.count(7) + 8 * cardBase.count(8) + 9 * cardBase.count(
    9) + 10 * cardBase.count(10) + 11 * cardBase.count(11)) / (decks * 13))
# Normal deck
# if main deck wins
if sum(aPCards) <= 21 and sum(aPCards) > sum(aDCards):
    aPCards.clear()
    aDCards.clear()
    print('Your left hand wins')
# if main deck busts
elif sum(aPCards) > 21:
    aPCards.clear()
    aDCards.clear()
    print('Your left hand loses')
# if dealer busts
if sum(aDCards) > 21:
    aPCards.clear()
    aDCards.clear()
    print('Your left hand wins')
# if main deck loses
elif sum(aPCards) <= 21 and sum(aPCards) < sum(aDCards):
    aPCards.clear()
    aDCards.clear()
    print('Your left hand loses')
# if main deck pushes with dealer
elif sum(aPCards) == sum(aDCards):
    aPCards.clear()
    aDCards.clear()
    print('Your left hand pushes')