# add a cut card to the shoe
import random as r
from openpyxl import load_workbook
# cardbase lists and other variable's
aDCards = []
aPCards = []
aSplitPCards = []
sDCards = []
sPCards = []
sSplitPCards = []
simulationHit = []
simulationDouble = []
simulationStand = []
splitSimulationSplit = []
simulationSplit = []
x = []
data = {
    2: {2:'B2', 3:'C2',4:'D2',5:'E2',6:'F2',7:'G2',8:'H2',9:'I2',10:'J2',11:'K2'},
    3: {2:'B3', 3:'C3',4:'D3',5:'E3',6:'F3',7:'G3',8:'H3',9:'I3',10:'J3',11:'K3'},
    4: {2:'B4', 3:'C4',4:'D4',5:'E4',6:'F4',7:'G4',8:'H4',9:'I4',10:'J4',11:'K4'},
    5: {2:'B5', 3:'C5',4:'D5',5:'E5',6:'F5',7:'G5',8:'H5',9:'I5',10:'J5',11:'K5'},
    6: {2:'B6', 3:'C6',4:'D6',5:'E6',6:'F6',7:'G6',8:'H6',9:'I6',10:'J6',11:'K6'},
    7: {2:'B7', 3:'C7',4:'D7',5:'E7',6:'F7',7:'G7',8:'H7',9:'I7',10:'J7',11:'K7'},
    8: {2:'B8', 3:'C8',4:'D8',5:'E8',6:'F8',7:'G8',8:'H8',9:'I8',10:'J8',11:'K8'},
    9: {2:'B9', 3:'C9',4:'D9',5:'E9',6:'F9',7:'G9',8:'H9',9:'I9',10:'J9',11:'K9'},
    10: {2:'B10', 3:'C10',4:'D10',5:'E10',6:'F10',7:'G10',8:'H10',9:'I10',10:'J10',11:'K10'},
    11: {2:'B11', 3:'C11',4:'D11',5:'E11',6:'F11',7:'G11',8:'H11',9:'I11',10:'J11',11:'K11'},
    12: {2:'B12', 3:'C12',4:'D12',5:'E12',6:'F12',7:'G12',8:'H12',9:'I12',10:'J12',11:'K12'},
    13: {2:'B13', 3:'C13',4:'D13',5:'E13',6:'F13',7:'G13',8:'H13',9:'I13',10:'J13',11:'K13'},
    14: {2:'B14', 3:'C14',4:'D14',5:'E14',6:'F14',7:'G14',8:'H14',9:'I14',10:'J14',11:'K14'},
    15: {2:'B15', 3:'C15',4:'D15',5:'E15',6:'F15',7:'G15',8:'H15',9:'I15',10:'J15',11:'K15'},
    16: {2:'B16', 3:'C16',4:'D16',5:'E16',6:'F16',7:'G16',8:'H16',9:'I16',10:'J16',11:'K16'},
    17: {2:'B17', 3:'C17',4:'D17',5:'E17',6:'F17',7:'G17',8:'H17',9:'I17',10:'J17',11:'K17'},
    18: {2:'B18', 3:'C18',4:'D18',5:'E18',6:'F18',7:'G18',8:'H18',9:'I18',10:'J18',11:'K18'},
    19: {2:'B19', 3:'C19',4:'D19',5:'E19',6:'F19',7:'G19',8:'H19',9:'I19',10:'J19',11:'K19'},
    20: {2:'B20', 3:'C20',4:'D20',5:'E20',6:'F20',7:'G20',8:'H20',9:'I20',10:'J20',11:'K20'},
    21: {2:'B21', 3:'C21',4:'D21',5:'E21',6:'F21',7:'G21',8:'H21',9:'I21',10:'J21',11:'K21'}
}
decks = 6
games = 10000
bet = 0
cardBaseOG = decks * [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
cardBase = decks * [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
rightchoice = 0
#functions
def db(y):
    if len(simulationHit) > 0:
        z = 'Hit'
    if len(simulationDouble) > 0:
        z = "Double"
    if len(simulationStand) > 0:
        z = 'Stand'
    if len(splitSimulationSplit) > 0:
        z = 'Split'
    b = data[sum(aPCards)][sum(aDCards)]
    wkbk = load_workbook(filename='BlackJackDataBase.xlsx')
    sheet = wkbk[z]
    value = float(sheet[b].value)
    sheet[b] = (value + y)/2
    wkbk.save(filename='BlackJackDataBase.xlsx')

def sim_endgame():
    if len(simulationHit) > 0:
        y = simulationHit
    if len(simulationDouble) > 0:
        y = simulationDouble
    if len(simulationStand) > 0:
        y = simulationStand
    if len(splitSimulationSplit) > 0:
        y = splitSimulationSplit
    # if main deck loses
    if sum(sDCards) <= 21 and sum(sPCards) < sum(sDCards):
        if y != simulationDouble:
            y.append(-1)
        else: 
            y.append(-2)
        while len(sPCards) != len(aPCards):
            i = len(sPCards) - 1
            cardBase.append(sPCards[i])
            sPCards.remove(sPCards[i])
        while len(sDCards) != len(aDCards):
            i = len(sDCards) - 1
            cardBase.append(sDCards[i])
            sDCards.remove(sDCards[i])
    # if main deck wins
    if sum(sPCards) <= 21 and sum(sPCards) > sum(sDCards):
        if y != simulationDouble:
            y.append(1)
        else:
            y.append(2)
        while len(sPCards) != len(aPCards):
            i = len(sPCards) - 1
            cardBase.append(sPCards[i])
            sPCards.remove(sPCards[i])
        while len(sDCards) != len(aDCards):
            i = len(sDCards) - 1
            cardBase.append(sDCards[i])
            sDCards.remove(sDCards[i])
    #loss
    if sum(sPCards) > 21:
        if y != simulationDouble:
            y.append(-1)
        else:
            y.append(-2)
        while len(sPCards) != len(aPCards):
            i = len(sPCards) - 1
            cardBase.append(sPCards[i])
            sPCards.remove(sPCards[i])
        while len(sDCards) != len(aDCards):
            i = len(sDCards) - 1
            cardBase.append(sDCards[i])
            sDCards.remove(sDCards[i])
    #win
    if sum(sDCards) > 21:
        if y != simulationDouble:
            y.append(1)
        else:
            y.append(2)
        while len(sPCards) != len(aPCards):
            i = len(sPCards) - 1
            cardBase.append(sPCards[i])
            sPCards.remove(sPCards[i])
        while len(sDCards) != len(aDCards):
            i = len(sDCards) - 1
            cardBase.append(sDCards[i])
            sDCards.remove(sDCards[i])
    # if side deck pushes with dealer
    if sum(sPCards) == sum(sDCards):
        y.append(0)
        while len(sPCards) != len(aPCards):
            i = len(sPCards) - 1
            cardBase.append(sPCards[i])
            sPCards.remove(sPCards[i])
        while len(sDCards) != len(aDCards):
            i = len(sDCards) - 1
            cardBase.append(sDCards[i])
            sDCards.remove(sDCards[i])

def simsplit_endgame():
    y = simulationSplit
    # if main deck loses
    if sum(sDCards) <= 21 and sum(sSplitPCards) < sum(sDCards):
        if y != simulationDouble:
            y.append(-1)
        while len(sSplitPCards) != len(aSplitPCards):
            i = len(sSplitPCards) - 1
            cardBase.append(sSplitPCards[i])
            sSplitPCards.remove(sSplitPCards[i])
        while len(sDCards) != len(aDCards):
            i = len(sDCards) - 1
            cardBase.append(sDCards[i])
            sDCards.remove(sDCards[i])
    # if main deck wins
    if sum(sSplitPCards) <= 21 and sum(sSplitPCards) > sum(sDCards):
        if y != simulationDouble:
            y.append(1)
        while len(sSplitPCards) != len(aSplitPCards):
            i = len(sSplitPCards) - 1
            cardBase.append(sSplitPCards[i])
            sSplitPCards.remove(sSplitPCards[i])
        while len(sDCards) != len(aDCards):
            i = len(sDCards) - 1
            cardBase.append(sDCards[i])
            sDCards.remove(sDCards[i])
    #loss
    if sum(sSplitPCards) > 21:
        if y != simulationDouble:
            y.append(-1)
        while len(sSplitPCards) != len(aSplitPCards):
            i = len(sSplitPCards) - 1
            cardBase.append(sSplitPCards[i])
            sSplitPCards.remove(sSplitPCards[i])
        while len(sDCards) != len(aDCards):
            i = len(sDCards) - 1
            cardBase.append(sDCards[i])
            sDCards.remove(sDCards[i])
    #win
    if sum(sDCards) > 21:
        if y != simulationDouble:
            y.append(1)
        while len(sSplitPCards) != len(aSplitPCards):
            i = len(sSplitPCards) - 1
            cardBase.append(sSplitPCards[i])
            sSplitPCards.remove(sSplitPCards[i])
        while len(sDCards) != len(aDCards):
            i = len(sDCards) - 1
            cardBase.append(sDCards[i])
            sDCards.remove(sDCards[i])
    # if side deck pushes with dealer
    if sum(sSplitPCards) == sum(sDCards):
        y.append(0)
        while len(sSplitPCards) != len(aSplitPCards):
            i = len(sSplitPCards) - 1
            cardBase.append(sSplitPCards[i])
            sSplitPCards.remove(sSplitPCards[i])
        while len(sDCards) != len(aDCards):
            i = len(sDCards) - 1
            cardBase.append(sDCards[i])
            sDCards.remove(sDCards[i])

def dealer_sim():
    while sum(sDCards) < 17:
        sDCards.append(r.choice(cardBase))
        i = len(sDCards) - 1
        cardBase.remove(sDCards[i])
     
def sim_hit():
    simulationHit.append(.1)
    while len(simulationHit) < games:
        if len(sPCards) == len(aPCards):
            sPCards.append(r.choice(cardBase))
            i = len(sPCards) - 1
            cardBase.remove(sPCards[i])
        # dealer sim
        dealer_sim()
        # endgame
        sim_endgame()
    y = (sum(simulationHit) / len(simulationHit))
    print('Hit', y)
    db(y)
    simulationHit.clear()
        
def sim_double():
    if len(aPCards) == 2:
        simulationDouble.append(1)
        while len(simulationDouble) < games and len(aPCards) == 2:
            if len(sPCards) == 2:
                sPCards.append(r.choice(cardBase))
                i = len(sPCards) - 1
                cardBase.remove(sPCards[i])
            # dealer sim
            dealer_sim()
            # endgame
            sim_endgame()
        y = (sum(simulationDouble) / len(simulationDouble))
        print('Double', y)
        db(y)
        simulationDouble.clear()
    if len(aPCards) !=2:
        print('Can not double at this time')

def sim_stand():
    simulationStand.append(1)
    while len(simulationStand) < games:
            # dealer sim
        dealer_sim()
        #endgame
        sim_endgame()
    y = (sum(simulationStand) / len(simulationStand))
    print("Stand", y)
    db(y)
    simulationStand.clear()
            
def sim_split():
    splitSimulationSplit.append(1)
    simulationSplit.append(1)
    while len(splitSimulationSplit) < games and aPCards[0] == aPCards[1]:
        sSplitPCards = sPCards.copy()
        sPCards.remove(sPCards[1])
        sSplitPCards.remove(sSplitPCards[1])
        sPCards.append(r.choice(cardBase))
        sSplitPCards.append(r.choice(cardBase))
        #dealer sim
        dealer_sim()
        #endgame
        sim_endgame()
        simsplit_endgame()
    if aPCards[0] == aPCards[1]:
        y = (sum(splitSimulationSplit) / len(splitSimulationSplit))
        b = y
        db(y)
        y = (sum(simulationSplit) / len(simulationSplit))
        db(y)
        print('Split', y)
    if aPCards[0] != aPCards[1]:
        y = 'Can not split cards at this time'
    splitSimulationSplit.clear()
question = input('Do you want to play with computer assistance? ')
initial_Balance = int(input('How much are we betting with today? '))
while initial_Balance > 0:
    '''if bet > 0: 
        quit = input('Would you like to quit? ')'''
    bet = int(input('How much do you want to bet? '))
    '''if quit == 'yes':
        wks.update_acell('M2', initial_Balance)
        break'''
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
        sPCards = aPCards.copy()
    #Dealer
    while len(aDCards) != 1:
        aDCards.append(r.choice(cardBase))
        if len(cardBase) <= 4:
            print('No cards main in the shoe, adding more. ')
            cardBase = cardBaseOG.copy()
        cardBase.remove(aDCards[0])
        sDCards = aDCards.copy()
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
    if question == 'yes':
        print('SIMULATION DATA')
        sim_double()
        sim_hit()
        sim_stand()
        sim_split()
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
        sPCards = aPCards.copy()
        sSplitPCards = aSplitPCards.copy()
        print('Your main hand is, ', aPCards[0], aPCards[1],
                'Your right hand is, ', aSplitPCards[0], aSplitPCards[1])
        if aPCards.count(11) and sum(aPCards) > 21 and aPCards[0] != aPCards[1]:
            print('The Players cards are ', aPCards[0], aPCards[1])
            aPCards.remove(11)
            aPCards.append(1)
        if sum(aPCards) == 21:
            print('BlackJack')
            rightchoice = input('What is your move for your right hand? ')
        if sum(aPCards) != 21:
            choice = input('What is your move for your main hand? ')
        if question == 'yes':
            print('SIMULATION DATA')
            sim_double()
            sim_hit()
            sim_stand()
            sim_split()
        while choice == 'split':
            choice = input('You can not split after splitting already. ')
        while choice != 'stand' and choice != 'double' and choice != 'hit':
            choice = input('Please enter hit, split, stand, or double. ')
    # stand
    if choice == 'stand' and len(aPCards) == 2:
        print('Ok')
        if len(aSplitPCards) == 2:
            rightchoice = input('What is your move for your right hand? ')
            if question == 'yes':
                print('SIMULATION DATA')
                sim_double()
                sim_hit()
                sim_stand()
                sim_split()
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
            if question == 'yes':
                print('SIMULATION DATA')
                sim_double()
                sim_hit()
                sim_stand()
                sim_split()
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
            sPCards = aPCards.copy()
            if sum(aPCards) < 21:     
                print('Your next card for your hand is, ', aPCards[i])   
                choice = input('What is your next move? ')
                if question == 'yes':
                    print('SIMULATION DATA')
                    sim_double()
                    sim_hit()
                    sim_stand()
                    sim_split()
                while choice == 'split' or choice == 'double':
                    choice = input('You can not split or double after hitting. ')
                while choice != 'stand' and choice != 'double' and choice != 'hit':
                    choice = input('Please enter hit, split, stand, or double. ')
            if sum(aPCards) >= 21:
                if sum(aPCards) == 21:
                    print('Your next card for your hand is, ', aPCards[i], '\nYou hit 21')
                    if len(aSplitPCards) == 2:
                        rightchoice = input('What is your move for your right deck? ')
                        if question == 'yes':
                            print('SIMULATION DATA')
                            sim_double()
                            sim_hit()
                            sim_stand()
                            sim_split()
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
                        sPCards = aPCards.copy()
                        choice = input('What is your next move? ')
                        if question == 'yes':
                            print('SIMULATION DATA')
                            sim_double()
                            sim_hit()
                            sim_stand()
                            sim_split()
                        while choice == 'split' or choice == 'double':
                            choice = input('You can not split or double after hitting. ')
                        while choice != 'stand' and choice != 'double' and choice != 'hit':
                            choice = input('Please enter hit, split, stand, or double. ')
                    if sum(aPCards) > 21:
                        print('Your next card for your hand is, ', aPCards[i], '\nBust')
                        if len(aSplitPCards) == 2:
                            rightchoice = input('What is your move for your right deck? ')
                            if question == 'yes':
                                print('SIMULATION DATA')
                                sim_double()
                                sim_hit()
                                sim_stand()
                                sim_split()
                            while rightchoice == 'split':
                                rightchoice = input('You can not split after splitting already. ')
                            while rightchoice != 'hit' and rightchoice != 'stand' and rightchoice != 'double':
                                rightchoice = input('Please choose hit, stand, or double. ')
                            break
                        break
                    if len(aSplitPCards) == 2:
                        rightchoice = input('What is your move for your right deck? ')
                        if question == 'yes':
                            print('SIMULATION DATA')
                            sim_double()
                            sim_hit()
                            sim_stand()
                            sim_split()
                        while rightchoice == 'split':
                            rightchoice = input('You can not split after splitting already. ')
                        while rightchoice != 'hit' and rightchoice != 'stand' and rightchoice != 'double':
                            rightchoice = input('Please choose hit, stand, or double. ')
            # after hit stand  
            if choice == 'stand':
                print('ok')
                if len(aSplitPCards) == 2:
                    rightchoice = input('What is your move for your right deck? ')
                    if question == 'yes':
                        print('SIMULATION DATA')
                        sim_double()
                        sim_hit()
                        sim_stand()
                        sim_split()
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
                if question == 'yes':
                    print('SIMULATION DATA')
                    sim_double()
                    sim_hit()
                    sim_stand()
                    sim_split()
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
                        if question == 'yes':
                            print('SIMULATION DATA')
                            sim_double()
                            sim_hit()
                            sim_stand()
                            sim_split()
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
