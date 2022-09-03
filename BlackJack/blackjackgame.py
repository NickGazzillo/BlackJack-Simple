# put totals on endgame statements
# put rules/ insurance into the game
# make sure the game is infinite
# make all chocies go to one endgame
# add a cut card to the shoe
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
try:
    initial_Balance = int(input('How much money are you starting with today? '))
except:
    initial_Balance = int(input('Please use a numeric value ')) 
while initial_Balance > 0:
    try:
        bet = int(input('How much do you want to bet on this hand? '))
    except:
        bet = int(input('Please use a numeric value ')) 
    initial_Balance -= bet
    print(initial_Balance)
    while len(aPCards) != 2:
        aDCards.append(r.choice(cardBase))
        aPCards.append(r.choice(cardBase))
        if len(cardBase) <= 4:
            print('No cards left in the shoe, adding more. ')
            cardBase = cardBaseOG.copy()
        i = len(aPCards) - 1
        cardBase.remove(aPCards[i])
        cardBase.remove(aDCards[i])
    # normal rules
        # blackjack
    if sum(aDCards)or sum(aPCards)== 21:
        if sum(aDCards)== 21 and aDCards[0] == 11:
            print('Blackjack, You lose')
            aPCards.clear()
            aDCards.clear()
            question = input('Play again? ')
        elif sum(aPCards)== 21:
            print('BlackJack, You win')
            initialBalance += bet * 3/2
            print(initialBalance)
            aPCards.clear()
            aDCards.clear()
            question = input('Play again? ')
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
                question = input('Play Again? ')
                aPCards.clear()
                aDCards.clear()
            else:  
                print('OK ')              
        # Soft ace
        #personal
    if aPCards.count(11) and sum(aPCards)> 21:
        print('The Players cards are ', aPCards[0], aPCards[1])
        aPCards.remove(11)
        aPCards.append(1)
        if aDCards.count(11) is not True:
            print('The dealer cards are ', aDCards[0], aDCards[1])
        #dealer
    elif aDCards.count(11) and sum(aDCards)> 21:
        print('The dealer cards are ', aDCards[0], aDCards[1])
        aDCards.remove(11)
        aDCards.append(1)
        if aPCards.count(11) and sum(aPCards)> 21:
            print('The Players cards are ', aPCards[0], aPCards[1])
    else:
        print('The dealer cards are ', aDCards[0], aDCards[1],
            'The Players cards are ', aPCards[0], aPCards[1])
    choice = input('What is your move? ')
    # split
    if choice == 'split' and aPCards[0] == aPCards[1]:
        initial_Balance -= bet
        aSplitPCards = aPCards.copy()
        aSplitPCards.remove(aSplitPCards[1])
        aPCards.remove(aPCards[1])
        if len(cardBase) <= 4:
                print('No cards left in the shoe, adding more. ')
                cardBase = cardBaseOG.copy()
        aSplitPCards.append(r.choice(cardBase))
        aPCards.append(r.choice(cardBase))
        cardBase.remove(aSplitPCards[1])
        cardBase.remove(aPCards[1])
        print('Your left hand is, ', aPCards[0], aPCards[1],
                'Your right hand is, ', aSplitPCards[0], aSplitPCards[1])
        leftchoice = input('What is your move for your left hand? ')
        # split main deck double
        if leftchoice == 'double':
            if len(cardBase) <= 4:
                print('No cards left in the shoe, adding more. ')
                cardBase = cardBaseOG.copy()
            aPCards.append(r.choice(cardBase))
            cardBase.remove(aPCards[2])
            print('Your next card for your left hand is, ', aPCards[2])
            rightchoice = input('What is the move for your right hand ?')
        # split main deck hit
        if leftchoice == 'hit':
            while leftchoice == 'hit':
                i = len(aPCards)
                if len(cardBase) <= 4:
                    print('No cards left in the shoe, adding more. ')
                    cardBase = cardBaseOG.copy()
                aPCards.append(r.choice(cardBase))
                cardBase.remove(aPCards[i])
                if sum(aPCards) >= 21:
                    if sum(aPCards) == 21:
                        print('Your next card for your left hand is, ', aPCards[i], '\You hit 21')
                        rightchoice = input('What is the move for your right hand? ')
                        break
                    if sum(aPCards) > 21:
                        print('Your next card for your left hand is, ', aPCards[i],'\nBust')
                        rightchoice = input('What is the move for your right hand? ')
                        break
                if sum(aPCards) < 21:        
                    print('Your next card is ', aPCards[i])
                    leftchoice = input('What is your next move? ')
                    continue 
        # split main deck stand     
        if leftchoice == 'stand':
            print('ok')
            rightchoice = input('What is your move for your right hand? ')
        # split side deck double        
        if rightchoice == 'double':
            if len(cardBase) <= 4:
                print('No cards left in the shoe, adding more. ')
                cardBase = cardBaseOG.copy()
            aSplitPCards.append(r.choice(cardBase))
            cardBase.remove(aSplitPCards[2])
            print('Your next card for your right hand is, ', aSplitPCards[2])
        # split side deck hit  
        if rightchoice == 'hit':
            while rightchoice == 'hit':
                i = len(aSplitPCards)
                if len(cardBase) <= 4:
                    print('No cards left in the shoe, adding more. ')
                    cardBase = cardBaseOG.copy()
                aSplitPCards.append(r.choice(cardBase))
                cardBase.remove(aSplitPCards[i])
                if sum(aSplitPCards) >= 21:
                    if sum(aPCards) == 21:
                        print('Your next card for your hand is, ', aPCards[i], '\nYou hit 21')
                        break
                    if sum(aPCards) > 21:
                        print('Your next card for your hand is, ', aPCards[i], '\nBust')
                if sum(aSplitPCards) < 21:        
                    print('Your next card is ', aSplitPCards[i])
                    rightchoice = input('What is your next move? ')
                    continue
        # split side deck stand  
        elif rightchoice == 'stand':
            print('ok')
        # dealer plays
        while sum(aDCards) < 17:
            i = len(aDCards)
            if len(cardBase) <= 4:
                print('No cards left in the shoe, adding more. ')
                cardBase = cardBaseOG.copy()
            aDCards.append(r.choice(cardBase))
            cardBase.remove(aDCards[i])
            if aDCards.count(11) and sum(aDCards)> 21:
                    aDCards.remove(11)
                    aDCards.append(1)
            print('The next dealer card is ', aDCards[i])
            sum(aDCards)
        # Normal deck
        # if main deck wins
        while len(aPCards) > 0:
            if sum(aPCards) <= 21 and sum(aPCards) > sum(aDCards):
                aPCards.clear()
                initial_Balance += bet * 2
                print('Your left hand wins with your total ', sum(aPCards), 'and dealer total ', sum(aDCards))
                break
            # if main deck busts
            elif sum(aPCards) > 21:
                aPCards.clear()
                print('Your left hand loses ', sum(aPCards), 'and dealer total ', sum(aDCards))
                break
            # if dealer busts
            if sum(aDCards) > 21:
                aPCards.clear()
                initial_Balance += bet * 2
                print('Your left hand wins')
                break
            # if main deck loses
            elif sum(aPCards) <= 21 and sum(aPCards) < sum(aDCards):
                aPCards.clear()
                print('Your left hand loses')
                break
            # if main deck pushes with dealer
            elif sum(aPCards) == sum(aDCards):
                aPCards.clear()
                initial_Balance += bet
                print('Your left hand pushes')
                break
        #split deck
        while len(aSplitPCards) > 0:
            # if dealer busts
            if sum(aDCards) > 21:
                aSplitPCards.clear()
                aDCards.clear()
                initial_Balance += bet * 2
                
                break
            # if split deck busts
            if sum(aSplitPCards) > 21 and len(aSplitPCards) > 0:
                aSplitPCards.clear()
                aDCards.clear()
                
                break
            # if split deck loses
            if sum(aSplitPCards) <= 21 and sum(aSplitPCards) < sum(aDCards):
                aSplitPCards.clear()
                aDCards.clear()
                
                break
            # if split deck pushes with dealer
            if sum(aSplitPCards) == sum(aDCards):
                aSplitPCards.clear()
                aDCards.clear()
                initial_Balance += bet
                
                break
            # if split deck wins
            if sum(aSplitPCards) <= 21 and sum(aSplitPCards) > sum(aDCards):
                    aSplitPCards.clear()
                    aDCards.clear()
                    initial_Balance += bet * 2
                    
                    break
    # double
    if choice == 'double' and len(aPCards) == 2:
        initial_Balance -= bet
        bet += bet 
        if len(cardBase) <= 4:
                print('No cards left in the shoe, adding more. ')
                cardBase = cardBaseOG.copy()
        aPCards.append(r.choice(cardBase))
        cardBase.remove(aPCards[2])
        print('Your next card for your hand is, ', aPCards[2])
    # dealer plays
        while sum(aDCards) < 17:
            i = len(aDCards)
            if len(cardBase) <= 4:
                print('No cards left in the shoe, adding more. ')
                cardBase = cardBaseOG.copy()
            aDCards.append(r.choice(cardBase))
            cardBase.remove(aDCards[i])
            if aDCards.count(11) and sum(aDCards)> 21:
                    aDCards.remove(11)
                    aDCards.append(1)
            print('The dealer\'s next card is ', aDCards[i])
            sum(aDCards)
        while len(aPCards) > 0:
            #Normal
            # if dealer deck busts
            if sum(aDCards) > 21:
                aPCards.clear()
                aDCards.clear()
                initial_Balance += bet * 2
                print('Your hand wins')
                
                break
            # if main deck wins
            if sum(aPCards) <= 21 and sum(aPCards) > sum(aDCards):
                aPCards.clear()
                aDCards.clear()
                initial_Balance += bet * 2
                print('Your hand wins')
                
                break
            # if main deck busts
            if sum(aPCards) > 21:
                aPCards.clear()
                aDCards.clear()
                print('Your hand loses')
                
                break
            # if main deck loses
            if sum(aPCards) <= 21 and sum(aPCards) < sum(aDCards):
                aPCards.clear()
                aDCards.clear()
                print('Your hand loses')
                
                break
            # if main deck pushes with dealer
            if sum(aPCards) == sum(aDCards):
                aPCards.clear()
                aDCards.clear()
                initial_Balance += bet
                print('Your hand pushes')
                
                break
    # hit
    if choice == 'hit':
        while choice == 'hit':
            i = len(aPCards)
            if len(cardBase) <= 4:
                print('No cards left in the shoe, adding more. ')
                cardBase = cardBaseOG.copy()
            aPCards.append(r.choice(cardBase))
            cardBase.remove(aPCards[i])
            if sum(aPCards) >= 21:
                if sum(aPCards) == 21:
                    print('Your next card for your hand is, ', aPCards[i], '\nYou hit 21')
                    break
                if sum(aPCards) > 21:
                    print('Your next card for your hand is, ', aPCards[i], '\nBust')
                    break
            if sum(aPCards) < 21:        
                print('Your next card is ', aPCards[i])
                choice = input('What is your next move? ')
            # after hit stand  
            if choice == 'stand':
                print('ok')
            # dealer plays
        while sum(aDCards) < 17:
            i = len(aDCards)
            if len(cardBase) <= 4:
                print('No cards left in the shoe, adding more. ')
                cardBase = cardBaseOG.copy()
            aDCards.append(r.choice(cardBase))
            cardBase.remove(aDCards[i])
            if aDCards.count(11) and sum(aDCards)> 21:
                    aDCards.remove(11)
                    aDCards.append(1)
            print('The next dealer card is ', aDCards[i])
            sum(aDCards)
        while len(aPCards) > 0:
            #Normal
            # if dealer deck busts
            if sum(aDCards) > 21:
                aPCards.clear()
                aDCards.clear()
                initial_Balance += bet * 2
                print('Your hand wins')
                
                break
            # if main deck wins
            if sum(aPCards) <= 21 and sum(aPCards) > sum(aDCards):
                aPCards.clear()
                aDCards.clear()
                initial_Balance += bet * 2
                print('Your hand wins')
                
                break
            # if main deck busts
            if sum(aPCards) > 21:
                aPCards.clear()
                aDCards.clear()
                print('Your hand loses')
                
                break
            # if main deck loses
            if sum(aPCards) <= 21 and sum(aPCards) < sum(aDCards):
                aPCards.clear()
                aDCards.clear()
                print('Your hand loses')
                
                break
            # if main deck pushes with dealer
            if sum(aPCards) == sum(aDCards):
                aPCards.clear()
                aDCards.clear()
                initial_Balance += bet
                print('Your hand pushes')
                
                break
    # stand
    # dealer plays
    if choice == 'stand' and len(aPCards) == 2:
        while sum(aDCards) < 17:
            i = len(aDCards)
            if len(cardBase) <= 4:
                print('No cards left in the shoe, adding more. ')
                cardBase = cardBaseOG.copy()
            aDCards.append(r.choice(cardBase))
            cardBase.remove(aDCards[i])
            if aDCards.count(11) and sum(aDCards) > 21:
                    aDCards.remove(11)
                    aDCards.append(1)
            print('The next dealer card is ', aDCards[i])
            sum(aDCards)
        while len(aPCards) > 0:
        #Normal
            # if dealer deck busts
            if sum(aDCards) > 21:
                aPCards.clear()
                aDCards.clear()
                initial_Balance += bet * 2
                print('Your hand wins')
                
                break
            # if main deck wins
            if sum(aPCards) <= 21 and sum(aPCards) > sum(aDCards):
                aPCards.clear()
                aDCards.clear()
                initial_Balance += bet * 2
                print('Your hand wins')
                
                break
            # if main deck busts
            if sum(aPCards) > 21:
                aPCards.clear()
                aDCards.clear()
                print('Your hand loses')
                
                break
            # if main deck loses
            if sum(aPCards) <= 21 and sum(aPCards) < sum(aDCards):
                aPCards.clear()
                aDCards.clear()
                print('Your hand loses')
                
                break
            # if main deck pushes with dealer
            if sum(aPCards) == sum(aDCards):
                aPCards.clear()
                aDCards.clear()
                initial_Balance += bet
                print('Your hand pushes')
                
                break
                