import random as r
# simulation loops
simulationSplit = []
splitSimulationSplit = []
simulationDouble = []
simulationHit = []
simulationStand = []
simulationInsurance = []
# cardbase lists and other variable's
sDCards = []
sPCards = []
sSplitPCards = []
decks = 2
games = 10000
cardBaseOG = decks * [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
cardBase = decks * [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
weightedCardAverage = ((2 * cardBase.count(2) + 3 * cardBase.count(3) + 4 * cardBase.count(4) + 5 * cardBase.count(
    5) + 6 * cardBase.count(6) + 7 * cardBase.count(7) + 8 * cardBase.count(8) + 9 * cardBase.count(
    9) + 10 * cardBase.count(10) + 11 * cardBase.count(11)) / (decks * 13))
#Card dealing method
question = input('Do you want to pick cards? ')
#settings
if question == 'settings':
    decks = input('How many decks do you want in play? ')
    games = input('How many simulations do you want in play? ')
    cardBaseOG = decks * [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    cardBase = decks * [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
# person selects cards
if question == 'yes':
    pFCard = int(input('What is your first card? '))
    pSCard = int(input('What is your second card? '))
    dCard = int(input('What is the Dealers card? '))
    sPCards.append(pFCard)
    sPCards.append(pSCard)
    sDCards.append(dCard)
    cardBase.remove(pFCard)
    cardBase.remove(pSCard)
    cardBase.remove(dCard)   
if question == 'no':
    #  random selected cards
    while len(sPCards) != 2:
        sPCards.append(r.choice(cardBase))
        i = len(sPCards) - 1
        cardBase.remove(sPCards[i])
    while len(sDCards) != 1:
        sDCards.append(r.choice(cardBase))
        i = len(sDCards) - 1
        cardBase.remove(sDCards[i])
# normal rules
    # blackjack
if sum(sDCards) or sum(sPCards) == 21:
    if sum(sDCards)== 21 and sDCards[0] == 11:
        sPCards.clear()
        sDCards.clear()
    elif sum(sPCards)== 21:
        print('Blackjack')
        sPCards.clear()
        sDCards.clear()           
    # Soft ace
    #personal
if sPCards.count(11) and sum(sPCards)> 21:
    sPCards.remove(11)
    sPCards.append(1)
    #dealer
elif sDCards.count(11) and sum(sDCards)> 21:
    print('The dealer cards are ', sDCards[0], sDCards[1])
    sDCards.remove(11)
    sDCards.append(1)
    if sPCards.count(11) and sum(sPCards)> 21:
        print('The Players cards are ', sPCards[0], sPCards[1])
else:
    print('The dealer cards are ', sDCards[0],
        'The Players cards are ', sPCards[0], sPCards[1])
# simulation code
# move loop
    #simulationSplit
#simulation main deck side  
if sPCards[0] == sPCards[1] and len(sSplitPCards) != 2:
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
    if sum(sPCards) == sum(sDCards):
        simulationHit.append(0.5)
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
    if len(sPCards) == 2:
        sPCards.append(r.choice(cardBase))
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
    if sum(sPCards) == sum(sDCards):
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
    if sum(sPCards) == sum(sDCards):
        simulationHit.append(0.5)
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
sPCards.clear()
sDCards.clear()
