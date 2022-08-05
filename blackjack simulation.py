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
games = 10000
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
displayCards = input('Do you want cards to be random? ')
    #  random selected cards
if displayCards == 'yes':
    while len(sPCards) != 2:
       aDCards.append(r.choice(cardBase))
       aPCards.append(r.choice(cardBase))
       sPCards = aPCards.copy()
       sDCards = aDCards.copy()
    # displaying cards 
    print('The first dealer card is', sDCards[0], 'The hidden dealer card is', sDCards[1],
        'Your first card is', sPCards[0], 'and your second card is', sPCards[1])
    #  player selected cards
elif displayCards != 'yes':
    sDCards.append(int(input('What is the dealer card? ')))
    hiddenCard = input('Do we know the hidden dealer card? ')
    if hiddenCard == 'yes':
        sDCards.append(int(input('What is the hidden dealer card? ')))
        sPCards.append(int(input('What is your first card?')))
        sPCards.append(int(input('What is your second card?')))
        aDCards = sDCards.copy()
        aPCards = sPCards.copy()
        print('The first dealer card is', sDCards[0], 'The hidden dealer card is', sDCards[1],
        'Your first card is', sPCards[0], 'and your second card is', sPCards[1])   
    else:
        print('OK')
    sPCards.append(int(input('What is your first card?')))
    sPCards.append(int(input('What is your second card?')))
    aDCards = sDCards.copy()
    aPCards = sPCards.copy()
    # Displaying cards
    print('The first dealer card is', sDCards[0],
        'Your first card is', sPCards[0], 'and your second card is', sPCards[1])
# simulation code
    #simulationSplit
    #simulation main deck side  
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
# actual blackjack game

    #Split
    
    #Double
    
    #Hit
    
    #Stand
