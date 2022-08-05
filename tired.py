from posixpath import split
import random as r  
dealerCards = []
personalCards = [6 , 6]
splitPersonalCards = []
question = input('Would you like to play blackjack? ')
initialBalance = float(input('What is your initial balance? '))
while question != 'no':
    if initialBalance < 0:
        print('You are out of money')
        question = input('Play Again?')      
    bet = float(input('How much do you want to bet? '))
    initialBalance -= bet
    print('Your balance is, ' , initialBalance)
    # Display cards
    while len(dealerCards) != 2:
        personalCards.append(r.randint(2, 11))
        dealerCards.append(r.randint(2, 11))
    dealer = sum(dealerCards)
    personal = sum(personalCards)
    print('The dealer\'s card is', dealerCards[0],
        'Your cards are', personalCards[0], 'and', personalCards[1]
        )
    # normal rules
        # blackjack
    if dealer or personal == 21:
        if dealer == 21 and dealerCards[0] == 11:
            print('Blackjack, You lose')
            personalCards.clear()
            dealerCards.clear()
            question = input('Play again? ')
        elif personal == 21:
            print('BlackJack, You win')
            initialBalance += bet * 3/2
            print(initialBalance)
            personalCards.clear()
            dealerCards.clear()
            question = input('Play again? ')
        # insurance
    if dealerCards[0] == 11:
        choice = input('Do you want to take insurance? ')
        if choice == 'yes':
            insurance = float(input('How much do you want to pay for insurance? '))
            initialBalance = initialBalance - insurance
            if dealer == 21:
                initialBalance += insurance * 2      
            else:
                print('The dealer does not have 21, your balance is,', initialBalance) 
        elif choice == 'no':
            if dealer == 21:
                print('You Lose',
                    'The hidden card is', dealerCards[1],
                    'Your total is', initialBalance
                    )
                question = input('Play Again? ')
                personalCards.clear()
                dealerCards.clear()
            else:  
                print('OK ')              
        # Soft ace
    if personalCards.count(11) and personal > 21:
        personalCards.remove(11)
        personalCards.append(1)
    choice = input('What is your move? ')
    # split
    while choice == 'split' and personalCards[0] == personalCards[1]:
        splitPersonalCards.append(personalCards [1])
        personalCards.pop(0)
        splitPersonalCards.append(r.randint(1, 11))
        personalCards.append(r.randint(1, 11))
        print('Your right hand is, ', personalCards[0], 'and ', personalCards[1], 'len', len(personalCards))
        choice = input('What is your move? ')
        while personal < 21 and choice == 'hit':
            personalCards.append(r.randint(2, 11))
            i = len(personalCards) - 1
            personal = sum(personalCards)
            print('Your next card is, ', personalCards[i],
                '\nYour total is ', personal
                )
    # hit
    while personal < 21 and choice == 'hit':
        personalCards.append(r.randint(2, 11))
        i = len(personalCards) - 1
        personal = sum(personalCards)
        print('Your next card is, ', personalCards[i],
            '\nYour total is ', personal
            )
            # hit end game
        if personal >= 21:
            # player win
            if personal == 21 and dealer != 21:
                personalCards.clear()
                dealerCards.clear()
                splitPersonalCards.clear()
                initialBalance += bet * 2
                print(initialBalance,
                'dealer total is', dealer,
                'player total is', personal, 
                '\nYou win'
                )
                question = input('Play again? ') 
                break  
        # Stand after hit
        else:
            choice = input('What is your next move? ')
            if choice == 'stand':
                print(initialBalance)
                print('The hidden dealer card is', dealerCards[1])
            while dealer < 17 and choice == 'stand':
                dealerCards.append(r.randint(2, 11))
                i = len(dealerCards) - 1 
                dealer = sum(dealerCards)
                print('The next dealer card is', dealerCards[i],
                    '\nThe dealer\'s total is ', dealer
                    )
                # stand end game
            if dealer == personal or dealer >= 21 or (dealer > personal and dealer < 17) or (dealer < personal and dealer >= 17):
                # push
                if dealer == personal:
                    print(initialBalance,
                    'dealer total is', dealer,
                    'player total is', personal, 
                    '\nPush'
                    )
                    personalCards.clear()
                    dealerCards.clear()
                    splitPersonalCards.clear()
                    initialBalance += bet
                    print(initialBalance)
                    question = input('Play again? ')
                    break
                # dealer win
                elif dealer > personal and dealer <= 21 or personal > 21:
                    personalCards.clear()
                    dealerCards.clear()
                    splitPersonalCards.clear()
                    print(initialBalance,
                    'dealer total is', dealer,
                    'player total is', personal, 
                    '\nYou lose'
                    )
                    question = input('Play again? ')
                    break
                elif  dealer < personal and personal <= 21 or dealer >= 17:
                    personalCards.clear()
                    dealerCards.clear()
                    splitPersonalCards.clear()
                    print(initialBalance,
                    'dealer total is', dealer,
                    'player total is', personal, 
                    '\nYou lose'
                    )
                    question = input('Play again? ')
                    break
    # double
    if choice == 'double':
        initialBalance -= bet
        bet *= 2
        print(initialBalance)
        personalCards.append(r.randint(2, 11))
        personal = sum(personalCards)
        print('Your next card is', personalCards[2])
        while dealer < 17:
                dealerCards.append(r.randint(2, 11))
                i = len(dealerCards) - 1 
                dealer = sum(dealerCards)
                print('The next dealer card is', dealerCards[i],
                    '\nThe dealer\'s total is ', dealer
                    )
        if dealer == personal or dealer >= 21 or personal >= 21 or (dealer > personal and dealer < 21):
                # push
                if dealer == personal:
                    print(initialBalance,
                          'dealer total is', dealer,
                          'player total is', personal, 
                          '\nPush'
                          )
                    personalCards.clear()
                    dealerCards.clear()
                    splitPersonalCards.clear()
                    initialBalance += bet
                    print(initialBalance)
                    question = input('Play again? ')
                # dealer win
                elif dealer > personal and dealer <= 21 or personal > 21:
                    personalCards.clear()
                    dealerCards.clear()
                    splitPersonalCards.clear()
                    print(initialBalance,
                          'dealer total is', dealer,
                          'player total is', personal, 
                          '\nYou lose'
                          )
                    question = input('Play again? ')
                # player win
                elif dealer < personal and personal <= 21 or dealer > 21:
                    personalCards.clear()
                    dealerCards.clear()
                    splitPersonalCards.clear()
                    initialBalance += bet * 2
                    print(initialBalance,
                          'dealer total is', dealer,
                          'player total is', personal, 
                          '\nYou win')
                    question = input('Play again? ')  
    # stand
    if choice == 'stand':
        print(initialBalance)
        i = len(dealerCards) - 1
        print('The hidden dealer card is', dealerCards[i])
        while dealer < 17 and choice == 'stand':
            dealerCards.append(r.randint(2, 11))
            i = len(dealerCards) - 1 
            dealer = sum(dealerCards)
            print('The next dealer card is', dealerCards[i],
                '\nThe dealer\'s total is ', dealer
                )
            # Who won
        if dealer == personal or dealer >= 21 or personal >= 21 or (dealer > personal and dealer < 21):
            # push
            if dealer == personal:
                print(initialBalance,
                        'dealer total is', dealer,
                        'player total is', personal, 
                        '\nPush'
                        )
                personalCards.clear()
                dealerCards.clear()
                splitPersonalCards.clear()
                initialBalance += bet
                print(initialBalance)
                question = input('Play again? ')
            # dealer win
            elif dealer > personal and dealer <= 21 or personal > 21:
                personalCards.clear()
                dealerCards.clear()
                splitPersonalCards.clear()
                print(initialBalance,
                        'dealer total is', dealer,
                        'player total is', personal, 
                        '\nYou lose'
                        )
                question = input('Play again? ')
            # player win
            elif dealer < personal and personal <= 21 or dealer > 21:
                personalCards.clear()
                dealerCards.clear()
                splitPersonalCards.clear()
                initialBalance += bet * 2
                print(initialBalance,
                        'dealer total is', dealer,
                        'player total is', personal, 
                        '\nYou win'
                        )
                question = input('Play again? ')       
