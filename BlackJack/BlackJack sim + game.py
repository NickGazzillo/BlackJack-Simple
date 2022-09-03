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
sSplitCards = []
aPCards = []
aDCards = []
aSplitCards = []
decks = 2
games = 10000
cardBaseOG = decks * [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
cardBase = decks * [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
weightedCardAverage = ((2 * cardBase.count(2) + 3 * cardBase.count(3) + 4 * cardBase.count(4) + 5 * cardBase.count(
    5) + 6 * cardBase.count(6) + 7 * cardBase.count(7) + 8 * cardBase.count(8) + 9 * cardBase.count(
    9) + 10 * cardBase.count(10) + 11 * cardBase.count(11)) / (decks * 13))
#Card dealing method
initial_Balance = int(input("How much is your initial balance today? "))
#settings
if initial_Balance == 10101010:
    decks = input('How many decks do you want in play? ')
    games = input('How many simulations do you want in play? ')
    cardBaseOG = decks * [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    cardBase = decks * [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
while initial_Balance > 0:  
    bet = int(input('How much do you want to bet on this hand? '))
    while bet > initial_Balance:
        bet = int(input('Please only bet what you have. '))
    initial_Balance -= bet
    print('Your balance is, ', initial_Balance)
    # move input
    if sum(aPCards) != 21 or sum(aDCards) != 21:
        choice = input('What is your move? ')
        while choice != 'split' and choice != 'stand' and choice != 'double' and choice != 'hit':
            choice = input('Please enter hit, split, stand, or double. ')
    # deal cards
    while len(sPCards) != 2:
        sPCards.append(r.choice(cardBase))
        i = len(sPCards) - 1
        cardBase.remove(sPCards[i])
        aPCards = sPCards.copy()
    while len(sDCards) != 1:
        sDCards.append(r.choice(cardBase))
        i = len(sDCards) - 1
        cardBase.remove(sDCards[i])
        aDCard = sDCards.copy()
    # normal rules
        # blackjack
    if sum(sPCards) == 21:
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
     # insurance
    if aDCards[0] == 11:
        choice = input('Do you want to take insurance? ')
        if choice == 'yes':
            insurance = float(input('How much do you want to pay for insurance? '))
            initialBalance = initialBalance - insurance
            if sum(aDCards)== 21:
                initialBalance += insurance * 2      
            else:
                print('The dealer does not have 21, your balance is,', initialBalance) 
        elif choice == 'no':
            if sum(aDCards)== 21:
                print('You Lose',
                    'The hidden card is', aDCards[1],
                    'Your total is', initialBalance
                    )
                aPCards.clear()
                aDCards.clear()
            else:  
                print('OK ')              
    print('Your personal cards are, ', aPCards[0], aPCards[1],
        'and your dealer\'s card is ', aDCard[0])
    # split
    if choice == 'split' and aPCards[0] == aPCards[1] and len(aPCards) == 2 and (initial_Balance > bet *2):
        initial_Balance -= bet
        aSplitPCards = aPCards.copy()
        aSplitPCards.remove(aSplitPCards[1])
        aPCards.remove(aPCards[1])
        if len(cardBase) <= 4:
            print('No cards main in the shoe, adding more. ')
            cardBase = cardBaseOG.copy()
        aSplitPCards.append(r.choice(cardBase))
        aPCards.append(r.choice(cardBase))
        cardBase.remove(aSplitPCards[1])
        cardBase.remove(aPCards[1])
        print('Your main hand is, ', aPCards[0], aPCards[1],
                'Your right hand is, ', aSplitPCards[0], aSplitPCards[1])
        choice = input('What is your move for your main hand? ')
        while choice == 'split':
            choice = input('You can not split after splitting already. ')
        while choice != 'stand' and choice != 'double' and choice != 'hit':
            choice = input('Please enter hit, split, stand, or double. ')
    # stand
    if choice == 'stand' and len(aPCards) == 2:
        print('Ok')
        if len(aSplitPCards) == 2:
            rightchoice = input('What is your move for your right hand? ')
            while rightchoice == 'split':
                rightchoice = input('You can not split after splitting already. ')
            while rightchoice != 'hit' and rightchoice != 'stand' and rightchoice != 'double':
                rightchoice = input('Please choose hit, stand, or double. ')
    # split stand
    if rightchoice == 'stand' and len(aSplitPCards) == 2:
        print('Ok')
    # double
    if choice == 'double' and len(aPCards) == 2 and (initial_Balance > bet *2):
        initial_Balance -= bet
        bet += bet 
        if len(cardBase) <= 4:
                print('No cards main in the shoe, adding more. ')
                cardBase = cardBaseOG.copy()
        aPCards.append(r.choice(cardBase))
        cardBase.remove(aPCards[2])
        if aPCards.count(11) and sum(aPCards)> 21:
            print('Your next card is ', aPCards[2])
            aPCards.remove(11)
            aPCards.append(1)
        else:
            print('Your next card is ', aPCards[2])
        if len(aSplitPCards) == 2:
            rightchoice = input('What is your move for your right hand? ')
            while rightchoice == 'split':
                rightchoice = input('You can not split after splitting already. ')
            while rightchoice != 'hit' and rightchoice != 'stand' and rightchoice != 'double':
                rightchoice = input('Please choose hit, stand, or double. ')
    # split double
    if rightchoice == 'double' and len(aSplitPCards) == 2:
        initial_Balance -= bet
        bet += bet 
        if len(cardBase) <= 4:
                print('No cards main in the shoe, adding more. ')
                cardBase = cardBaseOG.copy()
        aSplitPCards.append(r.choice(cardBase))
        cardBase.remove(aSplitPCards[2])
        if aSplitPCards.count(11) and sum(aSplitPCards)> 21:
            print('Your next card is ', aSplitPCards[2])
            aSplitPCards.remove(11)
            aSplitPCards.append(1)
        else:
            print('Your next card is ', aSplitPCards[2])
    # hit
    if choice == 'hit':
        while choice == 'hit':
            i = len(aPCards)
            if len(cardBase) <= 4:
                print('No cards main in the shoe, adding more. ')
                cardBase = cardBaseOG.copy()
            aPCards.append(r.choice(cardBase))
            cardBase.remove(aPCards[i])
            if sum(aPCards) < 21:     
                print('Your next card for your hand is, ', aPCards[i])   
                choice = input('What is your next move? ')
                while choice == 'split' or 'double':
                    choice = input('You can not split or double after hitting. ')
                while choice != 'stand' and choice != 'double' and choice != 'hit':
                    choice = input('Please enter hit, split, stand, or double. ')
            if sum(aPCards) >= 21:
                if sum(aPCards) == 21:
                    print('Your next card for your hand is, ', aPCards[i], '\nYou hit 21')
                    if len(aSplitPCards) == 2:
                        rightchoice = input('What is your move for your right deck? ')
                        while rightchoice == 'split':
                            rightchoice = input('You can not split after splitting already. ')
                        while rightchoice != 'hit' and rightchoice != 'stand' and rightchoice != 'double':
                            rightchoice = input('Please choose hit, stand, or double. ')
                    break
                if sum(aPCards) > 21:
                    if aPCards.count(11):
                        print('Your next card for your hand is, ', aPCards[i])
                        aPCards.remove(11)
                        aPCards.append(1)
                        choice = input('What is your next move? ')
                        while choice == 'split' or 'double':
                            choice = input('You can not split or double after hitting. ')
                        while choice != 'stand' and choice != 'double' and choice != 'hit':
                            choice = input('Please enter hit, split, stand, or double. ')
                    if sum(aPCards) > 21:
                        print('Your next card for your hand is, ', aPCards[i], '\nBust')
                        if len(aSplitPCards) == 2:
                            rightchoice = input('What is your move for your right deck? ')
                            while rightchoice == 'split':
                                rightchoice = input('You can not split after splitting already. ')
                            while rightchoice != 'hit' and rightchoice != 'stand' and rightchoice != 'double':
                                rightchoice = input('Please choose hit, stand, or double. ')
                            break
                        break
                    if len(aSplitPCards) == 2:
                        rightchoice = input('What is your move for your right deck? ')
            # after hit stand  
            if choice == 'stand':
                print('ok')
                if len(aSplitPCards) == 2:
                    rightchoice = input('What is your move for your right deck? ')
                    while rightchoice == 'split':
                        rightchoice = input('You can not split after splitting already. ')
                    while rightchoice != 'hit' and rightchoice != 'stand' and rightchoice != 'double':
                        rightchoice = input('Please choose hit, stand, or double. ')
    # split hit
    if rightchoice == 'hit':
        while rightchoice == 'hit':
            i = len(aSplitPCards)
            if len(cardBase) <= 4:
                print('No cards main in the shoe, adding more. ')
                cardBase = cardBaseOG.copy()
            aSplitPCards.append(r.choice(cardBase))
            cardBase.remove(aSplitPCards[i])
            if sum(aSplitPCards) < 21:    
                print('Your next card for your hand is, ', aSplitPCards[i])
                rightchoice = input('What is your next move? ')
                while rightchoice == 'split':
                    rightchoice = input('You can not split after splitting already. ')
                while rightchoice != 'hit' and rightchoice != 'stand' and rightchoice != 'double':
                    rightchoice = input('Please choose hit, stand, or double. ')
            if sum(aSplitPCards) >= 21:
                if sum(aSplitPCards) == 21:
                    print('Your next card for your hand is, ', aSplitPCards[i], '\nYou hit 21')
                    break
                if sum(aSplitPCards) > 21:
                    if aSplitPCards.count(11):  
                        print('Your next card is ', aSplitPCards[i])
                        aSplitPCards.remove(11)
                        aSplitPCards.append(1)
                        rightchoice = input('What is your next move? ')
                        while rightchoice == 'split':
                            rightchoice = input('You can not split after splitting already. ')
                        while rightchoice != 'hit' and rightchoice != 'stand' and rightchoice != 'double':
                            rightchoice = input('Please choose hit, stand, or double. ')
                        continue
                    if sum(aSplitPCards) > 21:
                        print('Your next card for your hand is, ', aSplitPCards[i], '\nBust')
                    break
            # after hit stand  
            if rightchoice == 'stand':
                print('ok')
    # split double
    if rightchoice == 'double' and len(aSplitPCards) == 2:
        initial_Balance -= bet
        bet += bet 
        if len(cardBase) <= 4:
                print('No cards main in the shoe, adding more. ')
                cardBase = cardBaseOG.copy()
        aSplitPCards.append(r.choice(cardBase))
        cardBase.remove(aSplitPCards[2])
        if aSplitPCards.count(11) and sum(aSplitPCards)> 21:
            print('Your next card is ', aSplitPCards[2])
            aSplitPCards.remove(11)
            aSplitPCards.append(1)
        else:
            print('Your next card is ', aSplitPCards[2])
    # split stand
    if rightchoice == 'stand' and len(aSplitPCards) == 2:
        print('Ok')
    # hidden dealer card
    if len(aDCards) != 2:
        aDCards.append(r.choice(cardBase))
        print('The hidden card is, ', aDCards[1])
    # dealer plays
    while sum(aDCards) < 17:
        i = len(aDCards)
        if len(cardBase) <= 4:
            print('No cards left in the shoe, adding more. ')
            cardBase = cardBaseOG.copy()
        aDCards.append(r.choice(cardBase))
        cardBase.remove(aDCards[i])
        if aDCards.count(11) and sum(aDCards)> 21:
            print('The next dealer card is ', aDCards[i])
            aDCards.remove(11)
            aDCards.append(1)
            print('The dealer total is, ', sum(aDCards))
        else:
            print('The next dealer card is ', aDCards[i])
            print('The dealer total is, ', sum(aDCards))
        sum(aDCards)
    # endgame
    # split deck
    if len(aSplitPCards) > 0:
        # if split deck loses
        if sum(aSplitPCards) > 21 or (sum(aSplitPCards) < sum(aDCards) and sum(aDCards) <=21):
            print('Your right hand loses with your total being ', sum(aSplitPCards), 'and the dealer total being, ', sum(aDCards))
        # if split deck wins
        elif sum(aDCards) > 21 or (sum(aSplitPCards) > sum(aDCards) and sum(aSplitPCards) <=21):
            print('Your right hand wins with your total being ', sum(aSplitPCards), 'and the dealer total being, ', sum(aDCards))
            initial_Balance += bet * 2
        # if split deck pushes with dealer
        elif sum(aSplitPCards) == sum(aDCards):
            print('Your right hand pushes with your total being ', sum(aSplitPCards), 'and the dealer total being, ', sum(aDCards))
            initial_Balance += bet
    aSplitPCards.clear()
    # Normal
    if len(aPCards) > 0:
    # if main deck loses
        if sum(aPCards) > 21 or (sum(aPCards) < sum(aDCards) and sum(aDCards) <=21):
            print('Your main hand loses with your total being ', sum(aPCards), 'and the dealer total being, ', sum(aDCards))
        # if main deck wins
        elif sum(aDCards) > 21 or (sum(aPCards) > sum(aDCards) and sum(aPCards) <=21):
            print('Your main hand wins with your total being ', sum(aPCards), 'and the dealer total being, ', sum(aDCards))
            initial_Balance += bet * 2
        # if main deck pushes with dealer
        elif sum(aPCards) == sum(aDCards):
            print('Your main hand pushes with your total being ', sum(aPCards), 'and the dealer total being, ', sum(aDCards))
            initial_Balance += bet
    print('Your balance is, ', initial_Balance)
    aPCards.clear()
    aDCards.clear()
    # simulation code
    # move loop
        #simulationSplit
    #simulation main deck side  
    if sPCards[0] == sPCards[1] and len(aPCards) == 2:
        sSplitCards = sPCards.copy()
        sPCards.remove(sPCards[1])
        aPCards.remove(aPCards[1])
        sSplitCards.remove(sSplitCards[1])
        sPCards.append(r.choice(cardBase))
        sSplitCards.append(r.choice(cardBase))
        aPCards = sPCards.copy()
        aSplitCards = sSplitCards.copy()
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
            while (weightedCardAverage + sum(sSplitCards)) <= 21:
                sSplitCards.append(r.choice(cardBase))
                weightedCardAverage = ((2 * cardBase.count(2) + 3 * cardBase.count(3) + 4 * cardBase.count(4) + 5 * cardBase.count(
                5) + 6 * cardBase.count(6) + 7 * cardBase.count(7) + 8 * cardBase.count(8) + 9 * cardBase.count(
                9) + 10 * cardBase.count(10) + 11 * cardBase.count(11)) / (len(cardBase)))
                i = len(sSplitCards) - 1
                cardBase.remove(sSplitCards[i])
            # dealer sim
            while sum(sDCards) < 21:
                sDCards.append(r.choice(cardBase))
                i = len(sDCards) - 1
                cardBase.remove(sDCards[i])
            # if side deck wins
            if sum(sSplitCards) <= 21 and sum(sSplitCards) > sum(sDCards):
                splitSimulationSplit.append(1)
                while len(sSplitCards) != 2:
                    i = len(sSplitCards) - 1
                    cardBase.append(sSplitCards[i])
                    sSplitCards.remove(sSplitCards[i])
                while len(sDCards) != 2:
                    i = len(sDCards) - 1
                    cardBase.append(sDCards[i])
                    sDCards.remove(sDCards[i])
            # if side deck busts
            elif sum(sSplitCards) > 21:
                splitSimulationSplit.append(0)
                while len(sSplitCards) != 2:
                    i = len(sSplitCards) - 1
                    cardBase.append(sSplitCards[i])
                    sSplitCards.remove(sSplitCards[i])
                while len(sDCards) != 2:
                    i = len(sDCards) - 1
                    cardBase.append(sDCards[i])
                    sDCards.remove(sDCards[i])
            # if side deck loses
            elif sum(sSplitCards) <= 21 and sum(sSplitCards) < sum(sDCards):
                splitSimulationSplit.append(0)
                while len(sSplitCards) != 2:
                    i = len(sSplitCards) - 1
                    cardBase.append(sSplitCards[i])
                    sSplitCards.remove(sSplitCards[i])
                while len(sDCards) != 2:
                    i = len(sDCards) - 1
                    cardBase.append(sDCards[i])
                    sDCards.remove(sDCards[i])
            # if side deck pushes with dealer
            elif sum(sSplitCards) == sum(sDCards):
                splitSimulationSplit.append(0.5)
                while len(sSplitCards) != 2:
                    i = len(sSplitCards) - 1
                    cardBase.append(sSplitCards[i])
                    sSplitCards.remove(sSplitCards[i])
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
        if len(sPCards) != len(aPCards):
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
    # Game over
if initial_Balance <= 0: 
    print('You lossed your total is', initial_Balance)