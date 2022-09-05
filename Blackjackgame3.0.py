# add a cut card to the shoe
import random as r
# cardbase lists and other variable's
aDCards = [2]
aPCards = [11,11]
aSplitPCards = []
decks = 6
cardBaseOG = decks * [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
cardBase = decks * [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
rightchoice = 0
initial_Balance = int(input('How much money are you starting with today? '))
while initial_Balance > 0:
    bet = int(input('How much do you want to bet on this hand? '))
    while bet > initial_Balance:
        bet = int(input('Please only bet what you have. '))
    initial_Balance -= bet
    print('Your balance is, ', initial_Balance)
    # display cards
    #Personal
    while len(aPCards) != 2:
        aPCards.append(r.choice(cardBase))
        if len(cardBase) <= 4:
            print('No cards main in the shoe, adding more. ')
            cardBase = cardBaseOG.copy()
        i = len(aPCards) - 1
        cardBase.remove(aPCards[i])
    #Dealer
    while len(aDCards) != 1:
        aDCards.append(r.choice(cardBase))
        if len(cardBase) <= 4:
            print('No cards main in the shoe, adding more. ')
            cardBase = cardBaseOG.copy()
        cardBase.remove(aDCards[0])
    # rules
    # blackjack
    if sum(aPCards)== 21:
        aDCards.append(r.choice(cardBase))
        cardBase.remove(aDCards[1])
        if sum(aPCards) == sum(aDCards):
            print('The dealer card is ', aDCards[0], aDCards[1],
            'The Players cards are ', aPCards[0], aPCards[1])
            print('You pushed')
            initial_Balance += bet
        print('The dealer card is ', aDCards[0], aDCards[1],
            'The Players cards are ', aPCards[0], aPCards[1])
        print('BlackJack, You win')
        initial_Balance += bet * 3/2
        print(initial_Balance)
        aPCards.clear()
        aDCards.clear()
        initial_Balance
        continue
        # insurance
    if aDCards[0] == 11:
        choice = input('Do you want to take insurance? ')
        if choice == 'yes':
            insurance = int(input('How much do you want to pay for insurance? '))
            initial_Balance = initial_Balance - insurance
            aDCards.append(r.choice(cardBase))
            if sum(aDCards) == 21:
                initial_Balance += insurance * 2
                print('The dealer has blackjack, your balance is ', initial_Balance)
                continue      
            else:
                print('The dealer does not have 21, your balance is,', initial_Balance) 
        if choice == 'no':
            if sum(aDCards) == 21:
                print('You Lose',
                    'The hidden card is', aDCards[1],
                    'Your total is', initial_Balance
                    )
                question = input('Play Again? ')
                aPCards.clear()
                aDCards.clear()
            else:  
                print('OK ')              
        # Soft ace
        #personal
    if aPCards.count(11) and sum(aPCards) > 21 and aPCards[0] != aPCards[1]:
        print('The Players cards are ', aPCards[0], aPCards[1])
        aPCards.remove(11)
        aPCards.append(1)
        if aDCards.count(11) is not True:
            print('The dealer card is ', aDCards[0])
        #normal
    else:
        print('The dealer card is ', aDCards[0],
            'The Players cards are ', aPCards[0], aPCards[1])
    # move input
    if sum(aPCards) != 21 or sum(aDCards) != 21:
        choice = input('What is your move? ')
        while choice != 'split' and choice != 'stand' and choice != 'double' and choice != 'hit':
            choice = input('Please enter hit, split, stand, or double. ')
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
                while choice == 'split' or choice == 'double':
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
                        while choice == 'split' or choice == 'double':
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
    if rightchoice == 'stand':
        print('Ok')
    # dealer plays
    if len(aDCards) != 2:
        aDCards.append(r.choice(cardBase))
        print('The hidden card is, ', aDCards[1])
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
    # Game over
if initial_Balance <= 0: 
    print('You lossed your total is', initial_Balance)
