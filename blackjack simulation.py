import random as r
# simulation loops
simulationSplit = []
splitSimulationSplit = []
simulationDouble = []
simulationHit = []
simulationStand = []
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
#indefinite while loop question
question = input('Do you want to play blackjack? ')
#settings
if question == 'settings':
    decks = input('How many decks do you want in play? ')
    games = input('How many simulations do you want in play? ')
    cardBaseOG = decks * [2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A]
    cardBase = decks * [2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A]
#display cards
if len(cardBase) == 0:
    print('The deck has run out, reshuffling')
    cardBase = cardBaseOG.copy()
#  random selected cards
while len(aPCards) != 2:
    aDCards.append(3)
    aPCards.append(2)
    sPCards = aPCards.copy()
    sDCards = aDCards.copy()
    i = len(aPCards) - 1
    cardBase.remove(aPCards[i])
    cardBase.remove(aDCards[i])
    # displaying cards 
print('The first dealer card is', aDCards[0], 'The hidden dealer card is', aDCards[1],
    'Your first card is', aPCards[0], 'and your second card is', aPCards[1])
# simulation code
# move loop
    #simulationSplit
#simulation main deck side  
if aPCards[0] == aPCards[1] and len(aSplitPCards) != 2:
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
    simulationSplitNum = sum(splitSimulationSplit) / len(splitSimulationSplit)
    split += simulationSplitNum
    print('split', split)
    simulationSplit.clear()
    splitSimulationSplit.clear()
    #simulationDouble
while len(simulationDouble) < games:
    if len(sPCards) == 2:
        sPCards.append(r.choice(cardBase))
        i = len(sPCards) - 1
        cardBase.remove(sPCards[i])
    # dealer sim
    while sum(sDCards) < 17:
        sDCards.append(r.choice(cardBase))
        i = len(sDCards) - 1
        cardBase.remove(sDCards[i])
    # if main double deck wins
    if sum(sPCards) <= 21 and sum(sPCards) > sum(sDCards):
        simulationDouble.append(2)
        while len(sPCards) != 2:
            i = len(sPCards) - 1
            cardBase.append(sPCards[i])
            sPCards.remove(sPCards[i])
        while len(sDCards) != 2:
            i = len(sDCards) - 1
            cardBase.append(sDCards[i])
            sDCards.remove(sDCards[i])
    # if main double deck busts
    elif sum(sPCards) > 21:
        simulationDouble.append(0)
        while len(sPCards) != 2:
            i = len(sPCards) - 1
            cardBase.append(sPCards[i])
            sPCards.remove(sPCards[i])
        while len(sDCards) != 2:
            i = len(sDCards) - 1
            cardBase.append(sDCards[i])
            sDCards.remove(sDCards[i])
    # if main double deck loses
    elif sum(sPCards) <= 21 and sum(sPCards) < sum(sDCards):
        simulationDouble.append(0)
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
        simulationDouble.append(1)
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
    #simulationHit
while len(simulationHit) < games:
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
    if len(sPCards) == 2:
        simulationHit.append(-1)
        continue
    # if main deck wins
    if sum(sPCards) <= 21 and sum(sPCards) > sum(sDCards):
        simulationHit.append(1)
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
        simulationHit.append(0)
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
        simulationHit.append(0)
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
        simulationHit.append(0.5)
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
    #simulationStand
while len(simulationStand) < games:
    # dealer sim
    while sum(sDCards) < 17:
        sDCards.append(r.choice(cardBase))
        i = len(sDCards) - 1
        cardBase.remove(sDCards[i])
    # if main deck wins
    if sum(sPCards) <= 21 and sum(sPCards) > sum(sDCards):
        simulationStand.append(1)
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
        simulationStand.append(0)
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
        simulationStand.append(0)
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
stand = (sum(simulationStand) / len(simulationStand))
print('stand', stand)
simulationStand.clear()
