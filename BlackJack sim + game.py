# add a cut card to the shoe
import random as r
import gspread as g
# cardbase lists and other variable's
aDCards = [2]
aPCards = [11,11]
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
decks = 6
games = 10000
cardBaseOG = decks * [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
cardBase = decks * [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
rightchoice = 0
question = str(input('Would you like to play with simulation assistance? '))
while question != 'yes' and question != 'no':
    question = str(input('Please answer \'yes\' or \'no\' '))
initial_Balance = int(input('How much money are you starting with today? '))
#functions
def db(aDCards, aPCards, y):
    if len(simulationHit) > 0:
        z = 'Hit'
    if len(simulationDouble) > 0:
        z = "Double"
    if len(simulationStand) > 0:
        z = 'Stand'
    if len(splitSimulationSplit) > 0:
        z = 'Split'
    sa = g.service_account(filename='blackjackddatabase.json')
    sh = sa.open('Blackjack')
    wks = sh.worksheet(str(z))
    if sum(aPCards) == 2:
        if sum(aDCards) == 2:
            find = 'B3'
        if sum(aDCards) == 3:
            find = 'C3'
        if sum(aDCards) == 4:
            find = 'D3'
        if sum(aDCards) == 5:
            find = 'E3'
        if sum(aDCards) == 6:
            find = 'F3'
        if sum(aDCards) == 7:
            find = 'G3'
        if sum(aDCards) == 8:
            find = 'H3'
        if sum(aDCards) == 9:
            find = 'I3'
        if sum(aDCards) == 10:
            find = 'J3'
        if sum(aDCards) == 11:
            find = 'K3'
    if sum(aPCards) == 3:
        if sum(aDCards) == 2:
            find = 'B4'
        if sum(aDCards) == 3:
            find = 'C4'
        if sum(aDCards) == 4:
            find = 'D4'
        if sum(aDCards) == 5:
            find = 'E4'
        if sum(aDCards) == 6:
            find = 'F4'
        if sum(aDCards) == 7:
            find = 'G4'
        if sum(aDCards) == 8:
            find = 'H4'
        if sum(aDCards) == 9:
            find = 'I4'
        if sum(aDCards) == 10:
            find = 'J4'
        if sum(aDCards) == 11:
            find = 'K4'
    if sum(aPCards) == 4:
        if sum(aDCards) == 2:
            find = 'B5'
        if sum(aDCards) == 3:
            find = 'C5'
        if sum(aDCards) == 4:
            find = 'D5'
        if sum(aDCards) == 5:
            find = 'E5'
        if sum(aDCards) == 6:
            find = 'F5'
        if sum(aDCards) == 7:
            find = 'G5'
        if sum(aDCards) == 8:
            find = 'H5'
        if sum(aDCards) == 9:
            find = 'I5'
        if sum(aDCards) == 10:
            find = 'J5'
        if sum(aDCards) == 11:
            find = 'K5'
    if sum(aPCards) == 5:
        if sum(aDCards) == 2:
            find = 'B6'
        if sum(aDCards) == 3:
            find = 'C6'
        if sum(aDCards) == 4:
            find = 'D6'
        if sum(aDCards) == 5:
            find = 'E6'
        if sum(aDCards) == 6:
            find = 'F6'
        if sum(aDCards) == 7:
            find = 'G6'
        if sum(aDCards) == 8:
            find = 'H6'
        if sum(aDCards) == 9:
            find = 'I6'
        if sum(aDCards) == 10:
            find = 'J6'
        if sum(aDCards) == 11:
            find = 'K6'
    if sum(aPCards) == 6:
        if sum(aDCards) == 2:
            find = 'B7'
        if sum(aDCards) == 3:
            find = 'C7'
        if sum(aDCards) == 4:
            find = 'D7'
        if sum(aDCards) == 5:
            find = 'E7'
        if sum(aDCards) == 6:
            find = 'F7'
        if sum(aDCards) == 7:
            find = 'G7'
        if sum(aDCards) == 8:
            find = 'H7'
        if sum(aDCards) == 9:
            find = 'I7'
        if sum(aDCards) == 10:
            find = 'J7'
        if sum(aDCards) == 11:
            find = 'K7'
    if sum(aPCards) == 7:
        if sum(aDCards) == 2:
            find = 'B8'
        if sum(aDCards) == 3:
            find = 'C8'
        if sum(aDCards) == 4:
            find = 'D8'
        if sum(aDCards) == 5:
            find = 'E8'
        if sum(aDCards) == 6:
            find = 'F8'
        if sum(aDCards) == 7:
            find = 'G8'
        if sum(aDCards) == 8:
            find = 'H8'
        if sum(aDCards) == 9:
            find = 'I8'
        if sum(aDCards) == 10:
            find = 'J8'
        if sum(aDCards) == 11:
            find = 'K8'
    if sum(aPCards) == 8:
        if sum(aDCards) == 2:
            find = 'B9'
        if sum(aDCards) == 3:
            find = 'C9'
        if sum(aDCards) == 4:
            find = 'D9'
        if sum(aDCards) == 5:
            find = 'E9'
        if sum(aDCards) == 6:
            find = 'F9'
        if sum(aDCards) == 7:
            find = 'G9'
        if sum(aDCards) == 8:
            find = 'H9'
        if sum(aDCards) == 9:
            find = 'I9'
        if sum(aDCards) == 10:
            find = 'J9'
        if sum(aDCards) == 11:
            find = 'K9'
    if sum(aPCards) == 9:
        if sum(aDCards) == 2:
            find = 'B10'
        if sum(aDCards) == 3:
            find = 'C10'
        if sum(aDCards) == 4:
            find = 'D10'
        if sum(aDCards) == 5:
            find = 'E10'
        if sum(aDCards) == 6:
            find = 'F10'
        if sum(aDCards) == 7:
            find = 'G10'
        if sum(aDCards) == 8:
            find = 'H10'
        if sum(aDCards) == 9:
            find = 'I10'
        if sum(aDCards) == 10:
            find = 'J10'
        if sum(aDCards) == 11:
            find = 'K10'
    if sum(aPCards) == 10:
        if sum(aDCards) == 2:
            find = 'B11'
        if sum(aDCards) == 3:
            find = 'C11'
        if sum(aDCards) == 4:
            find = 'D11'
        if sum(aDCards) == 5:
            find = 'E11'
        if sum(aDCards) == 6:
            find = 'F11'
        if sum(aDCards) == 7:
            find = 'G11'
        if sum(aDCards) == 8:
            find = 'H11'
        if sum(aDCards) == 9:
            find = 'I11'
        if sum(aDCards) == 10:
            find = 'J11'
        if sum(aDCards) == 11:
            find = 'K11'
    if sum(aPCards) == 11:
        if sum(aDCards) == 2:
            find = 'B12'
        if sum(aDCards) == 3:
            find = 'C12'
        if sum(aDCards) == 4:
            find = 'D12'
        if sum(aDCards) == 5:
            find = 'E12'
        if sum(aDCards) == 6:
            find = 'F12'
        if sum(aDCards) == 7:
            find = 'G12'
        if sum(aDCards) == 8:
            find = 'H12'
        if sum(aDCards) == 9:
            find = 'I12'
        if sum(aDCards) == 10:
            find = 'J12'
        if sum(aDCards) == 11:
            find = 'K12'
    if sum(aPCards) == 12:
        if sum(aDCards) == 2:
            find = 'B13'
        if sum(aDCards) == 3:
            find = 'C13'
        if sum(aDCards) == 4:
            find = 'D13'
        if sum(aDCards) == 5:
            find = 'E13'
        if sum(aDCards) == 6:
            find = 'F13'
        if sum(aDCards) == 7:
            find = 'G13'
        if sum(aDCards) == 8:
            find = 'H13'
        if sum(aDCards) == 9:
            find = 'I13'
        if sum(aDCards) == 10:
            find = 'J13'
        if sum(aDCards) == 11:
            find = 'K13'   
    if sum(aPCards) == 13:
        if sum(aDCards) == 2:
            find = 'B14'
        if sum(aDCards) == 3:
            find = 'C14'
        if sum(aDCards) == 4:
            find = 'D14'
        if sum(aDCards) == 5:
            find = 'E14'
        if sum(aDCards) == 6:
            find = 'F14'
        if sum(aDCards) == 7:
            find = 'G14'
        if sum(aDCards) == 8:
            find = 'H14'
        if sum(aDCards) == 9:
            find = 'I14'
        if sum(aDCards) == 10:
            find = 'J14'
        if sum(aDCards) == 11:
            find = 'K14'
    if sum(aPCards) == 14:
        if sum(aDCards) == 2:
            find = 'B15'
        if sum(aDCards) == 3:
            find = 'C15'
        if sum(aDCards) == 4:
            find = 'D15'
        if sum(aDCards) == 5:
            find = 'E15'
        if sum(aDCards) == 6:
            find = 'F15'
        if sum(aDCards) == 7:
            find = 'G15'
        if sum(aDCards) == 8:
            find = 'H15'
        if sum(aDCards) == 9:
            find = 'I15'
        if sum(aDCards) == 10:
            find = 'J15'
        if sum(aDCards) == 11:
            find = 'K15'
    if sum(aPCards) == 15:
        if sum(aDCards) == 2:
            find = 'B16'
        if sum(aDCards) == 3:
            find = 'C16'
        if sum(aDCards) == 4:
            find = 'D16'
        if sum(aDCards) == 5:
            find = 'E16'
        if sum(aDCards) == 6:
            find = 'F16'
        if sum(aDCards) == 7:
            find = 'G16'
        if sum(aDCards) == 8:
            find = 'H16'
        if sum(aDCards) == 9:
            find = 'I16'
        if sum(aDCards) == 10:
            find = 'J16'
        if sum(aDCards) == 11:
            find = 'K16'
    if sum(aPCards) == 16:
        if sum(aDCards) == 2:
            find = 'B17'
        if sum(aDCards) == 3:
            find = 'C17'
        if sum(aDCards) == 4:
            find = 'D17'
        if sum(aDCards) == 5:
            find = 'E17'
        if sum(aDCards) == 6:
            find = 'F17'
        if sum(aDCards) == 7:
            find = 'G17'
        if sum(aDCards) == 8:
            find = 'H17'
        if sum(aDCards) == 9:
            find = 'I17'
        if sum(aDCards) == 10:
            find = 'J17'
        if sum(aDCards) == 11:
            find = 'K17'
    if sum(aPCards) == 17:
        if sum(aDCards) == 2:
            find = 'B18'
        if sum(aDCards) == 3:
            find = 'C18'
        if sum(aDCards) == 4:
            find = 'D18'
        if sum(aDCards) == 5:
            find = 'E18'
        if sum(aDCards) == 6:
            find = 'F18'
        if sum(aDCards) == 7:
            find = 'G18'
        if sum(aDCards) == 8:
            find = 'H18'
        if sum(aDCards) == 9:
            find = 'I18'
        if sum(aDCards) == 10:
            find = 'J18'
        if sum(aDCards) == 11:
            find = 'K18'
    if sum(aPCards) == 18:
        if sum(aDCards) == 2:
            find = 'B19'
        if sum(aDCards) == 3:
            find = 'C19'
        if sum(aDCards) == 4:
            find = 'D19'
        if sum(aDCards) == 5:
            find = 'E19'
        if sum(aDCards) == 6:
            find = 'F19'
        if sum(aDCards) == 7:
            find = 'G19'
        if sum(aDCards) == 8:
            find = 'H19'
        if sum(aDCards) == 9:
            find = 'I19'
        if sum(aDCards) == 10:
            find = 'J19'
        if sum(aDCards) == 11:
            find = 'K19'
    if sum(aPCards) == 19:
        if sum(aDCards) == 2:
            find = 'B20'
        if sum(aDCards) == 3:
            find = 'C20'
        if sum(aDCards) == 4:
            find = 'D20'
        if sum(aDCards) == 5:
            find = 'E20'
        if sum(aDCards) == 6:
            find = 'F20'
        if sum(aDCards) == 7:
            find = 'G20'
        if sum(aDCards) == 8:
            find = 'H20'
        if sum(aDCards) == 9:
            find = 'I20'
        if sum(aDCards) == 10:
            find = 'J20'
        if sum(aDCards) == 11:
            find = 'K20'
    if sum(aPCards) == 20:
        if sum(aDCards) == 2:
            find = 'B21'
        if sum(aDCards) == 3:
            find = 'C21'
        if sum(aDCards) == 4:
            find = 'D21'
        if sum(aDCards) == 5:
            find = 'E21'
        if sum(aDCards) == 6:
            find = 'F21'
        if sum(aDCards) == 7:
            find = 'G21'
        if sum(aDCards) == 8:
            find = 'H21'
        if sum(aDCards) == 9:
            find = 'I21'
        if sum(aDCards) == 10:
            find = 'J21'
        if sum(aDCards) == 11:
            find = 'K21'
    if sum(aPCards) == 21:
        if sum(aDCards) == 2:
            find = 'B22'
        if sum(aDCards) == 3:
            find = 'C22'
        if sum(aDCards) == 4:
            find = 'D22'
        if sum(aDCards) == 5:
            find = 'E22'
        if sum(aDCards) == 6:
            find = 'F22'
        if sum(aDCards) == 7:
            find = 'G22'
        if sum(aDCards) == 8:
            find = 'H22'
        if sum(aDCards) == 9:
            find = 'I22'
        if sum(aDCards) == 10:
            find = 'J22'
        if sum(aDCards) == 11:
            find = 'K22'
    x.append(wks.acell(find).value)
    dbnum = float(x[0])
    if dbnum != 0:
        wks.update(find, (dbnum + float(y))/2)
    if dbnum == 0:
        wks.update(find, float(y))

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
    db(aDCards, aPCards, y)
    print('Hit', y)
    simulationHit.clear()
        
def sim_double():
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
    db(aDCards, aPCards, y)
    print('Double', y)
    simulationDouble.clear()
 
def sim_stand():
    simulationStand.append(1)
    while len(simulationStand) < games:
            # dealer sim
        dealer_sim()
        #endgame
        sim_endgame()
    y = (sum(simulationStand) / len(simulationStand))
    db(aDCards, aPCards, y)
    print('Stand', y)
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
        db(aDCards, aPCards, y)
        y = (sum(simulationSplit) / len(simulationSplit))
        db(aDCards, aPCards, y)
    if aPCards[0] != aPCards[1]:
        y = 'Cannot split cards'
    
    print('Split', (y + b)/2)
    splitSimulationSplit.clear()

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
        print('Your main hand is, ', aPCards[0], aPCards[1],
                'Your right hand is, ', aSplitPCards[0], aSplitPCards[1])
        choice = input('What is your move for your main hand? ')
        if question == 'yes':
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
            if sum(aPCards) < 21:     
                print('Your next card for your hand is, ', aPCards[i])   
                choice = input('What is your next move? ')
                if question == 'yes':
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
                        choice = input('What is your next move? ')
                        if question == 'yes':
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
