import gspread as g
import random as r 
sPCards = []
sDCards = []
sSplitPCards = []
aPCards = []
aDCards = []
aSplitPCards = []
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

# simulation loops
simulationSplit = []
splitSimulationSplit = []
simulationDouble = []
simulationSplitDouble = []
simulationHit = []
simulationSplitHit = []
simulationStand = []
simulationSplitStand = []
decks = 6
games = 10
cardBaseOG = decks * [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
cardBase = decks * [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
question = input('Would you like to pick the cards used? ')
while question != 'yes' and question !='no':
    question = str(input('Please answer \'yes\' or \'no\' '))
if question == 'yes':
    sPCards.append(int(input('What is your first card? ')))
    sPCards.append(int(input('What is your second card? ')))
    sDCards.append(int(input('What is your dealer\'s main card? ')))
    aPCards = sPCards.copy()
    dealerQuestion = input('Do we know the dealer\'s hidden card? ')
    while dealerQuestion != 'yes' and dealerQuestion != 'no':
        dealerQuestion = str(input('Please answer \'yes\' or \'no\' '))
    if dealerQuestion =='yes':
        sDCards.append(int(input('What is your dealer\'s hidden card? ')))
    if dealerQuestion == 'no':
        print('Ok')
    aDCards = sDCards.copy()
if question == 'no':
    while len(sPCards) != 2:
        sPCards.append(r.choice(cardBase))
        i = len(sPCards) - 1
        cardBase.remove(sPCards[i])
        aPCards = sPCards.copy()
    while len(sDCards) != 1:
        sDCards.append(r.choice(cardBase))
        i = len(sDCards) - 1
        cardBase.remove(sDCards[i])
        aDCards = sDCards.copy()
def db(aDCards, aPCards, y):
    if len(simulationHit) > 0 or len(simulationSplitHit) > 0:
        z = 'Hit'
    if len(simulationDouble) > 0 or len(simulationSplitDouble) > 0:
        z = "Double"
    if len(simulationStand) > 0 or len(simulationSplitStand) > 0:
        z = 'Stand'
    if len(splitSimulationSplit) > 0:
        z = 'Split'
    sa = g.service_account(filename='blackjackdatabase-eb1e681418d0.json')
    sh = sa.open('Blackjack')
    wks = sh.worksheet(str(z))
    find = str(data[sum(aPCards)][sum(aDCards)])
    x.append(wks.acell(find).value)    
    dbnum = float(x[0])
    if dbnum != 0:
        wks.update(find, (dbnum + float(y))/2)
        x.clear()
    if dbnum == 0:
        wks.update(find, float(y))
        x.clear()
    x.append(wks.acell(find).value)
    dbnum = float(x[0])
    print(z, dbnum)

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
    if len(simulationSplitHit) > 0:
        y = simulationSplitHit
    if len(simulationSplitDouble) > 0:
        y = simulationSplitDouble
    if len(simulationSplitStand) > 0:
        y = simulationSplitStand
    if len(simulationSplit) > 0:
        y = simulationSplit
    # if main deck loses
    if sum(sDCards) <= 21 and sum(sSplitPCards) < sum(sDCards):
        if y != simulationSplitDouble:
            y.append(-1)
        else: 
            y.append(-2)
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
        if y != simulationSplitDouble:
            y.append(1)
        else: 
            y.append(2)
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
        if y != simulationSplitDouble:
            y.append(-1)
        else: 
            y.append(-2)
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
        if y != simulationSplitDouble:
            y.append(1)
        else: 
            y.append(2)
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
        print('Split', (y + b)/2)
        y = (sum(simulationSplit) / len(simulationSplit))
        db(aDCards, aPCards, y)
    if aPCards[0] != aPCards[1]:
        y = 'Cannot split cards'
    splitSimulationSplit.clear()

def simsplit_hit():
    simulationSplitHit.append(.1)
    while len(simulationSplitHit) < games and aPCards[0] == aPCards[1]:
        sSplitPCards = sPCards.copy()
        sPCards.remove(sPCards[1])
        sSplitPCards.remove(sSplitPCards[1])
        sPCards.append(r.choice(cardBase))
        sSplitPCards.append(r.choice(cardBase))
        if len(sSplitPCards) == len(aSplitPCards):
            sSplitPCards.append(r.choice(cardBase))
            i = len(sSplitPCards) - 1
            cardBase.remove(sSplitPCards[i])
        # dealer sim
        dealer_sim()
        # endgame
        simsplit_endgame()
    y = (sum(simulationSplitHit) / len(simulationSplitHit))
    db(aDCards, aPCards, y)
    simulationSplitHit.clear()

def simsplit_double():
    simulationSplitDouble.append(1)
    while len(simulationSplitDouble) < games and aPCards[0] == aPCards[1]:
        sSplitPCards = sPCards.copy()
        sPCards.remove(sPCards[1])
        sSplitPCards.remove(sSplitPCards[1])
        sPCards.append(r.choice(cardBase))
        sSplitPCards.append(r.choice(cardBase))
        if len(sSplitPCards) == 2:
            sSplitPCards.append(r.choice(cardBase))
            i = len(sSplitPCards) - 1
            cardBase.remove(sSplitPCards[i])
        # dealer sim
        dealer_sim()
        # endgame
        simsplit_endgame()
    y = (sum(simulationSplitDouble) / len(simulationSplitDouble))
    db(aDCards, aPCards, y)
    simulationSplitDouble.clear()

def simsplit_stand():
    simulationSplitStand.append(1)
    while len(simulationSplitDouble) < games and aPCards[0] == aPCards[1]:
        sSplitPCards = sPCards.copy()
        sPCards.remove(sPCards[1])
        sSplitPCards.remove(sSplitPCards[1])
        sPCards.append(r.choice(cardBase))
        sSplitPCards.append(r.choice(cardBase))
            # dealer sim
        dealer_sim()
        #endgame
        simsplit_endgame()
    y = (sum(simulationSplitStand) / len(simulationSplitStand))
    db(aDCards, aPCards, y)
    simulationSplitStand.clear()

print('Your hand was', aPCards) 
print('Your dealer\'s hand was', aDCards)
sim_hit()
sim_double()
sim_stand()
'''simsplit_hit()
simsplit_double()
simsplit_stand()'''

