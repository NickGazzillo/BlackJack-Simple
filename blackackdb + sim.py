from re import S
import gspread as g
import random as r 
sPCards = [10, 11]
sDCards = [2]
aPCards = [10, 11]
aDCards = [2]
aSplitCards = []
x = []
# simulation loops
simulationSplit = []
splitSimulationSplit = []
simulationDouble = []
simulationHit = []
simulationStand = []
simulationInsurance = []
decks = 6
games = 10000
cardBaseOG = decks * [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
cardBase = decks * [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
weightedCardAverage = ((2 * cardBase.count(2) + 3 * cardBase.count(3) + 4 * cardBase.count(4) + 5 * cardBase.count(
    5) + 6 * cardBase.count(6) + 7 * cardBase.count(7) + 8 * cardBase.count(8) + 9 * cardBase.count(
    9) + 10 * cardBase.count(10) + 11 * cardBase.count(11)) / (decks * 13))
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
def db(aDCards, aPCards, Hit):
    sa = g.service_account(filename='blackjackddatabase.json')
    sh = sa.open('Blackjack')
    wks = sh.worksheet('Hit')
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
    wks.update(find, (dbnum + Hit)/2)

def sim_endgame(sPCards, sDCards, aPCards, aDCards):
    if len(simulationHit) > 0:
        y = simulationHit
    if len(simulationDouble) > 0:
        y = simulationDouble
    if len(simulationStand) > 0:
        y = simulationStand
    if len(splitSimulationSplit) > 0:
        y = splitSimulationSplit
    # if main deck loses
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
    # if side deck pushes with dealer
    if sum(sPCards) == sum(sDCards):
        y.append(-1)
        while len(sPCards) != len(aPCards):
            i = len(sPCards) - 1
            cardBase.append(sPCards[i])
            sPCards.remove(sPCards[i])
        while len(sDCards) != len(aDCards):
            i = len(sDCards) - 1
            cardBase.append(sDCards[i])
            sDCards.remove(sDCards[i])
   
def dealer_sim(sDCards):
    while sum(sDCards) < 17:
        sDCards.append(r.choice(cardBase))
        i = len(sDCards) - 1
        cardBase.remove(sDCards[i])
     
def sim_hit(sPCards, sDCards, aPCards, aDCards):
    simulationHit.append(1)
    while len(simulationHit) < games:
        if len(sPCards) == len(aPCards):
            sPCards.append(r.choice(cardBase))
            i = len(sPCards) - 1
            cardBase.remove(sPCards[i])
        # dealer sim
        dealer_sim(sDCards)
        # endgame
        sim_endgame(sPCards, sDCards, aPCards, aDCards)
    Hit = (sum(simulationHit) / len(simulationHit))
    print('ad', len(aDCards), 'ap', len(aPCards))
    db(aDCards, aPCards, Hit)
    print('Hit', Hit)
    simulationHit.clear()
        
def sim_double(sPCards, sDCards, aPCards):
    simulationDouble.append(1)
    while len(simulationDouble) < games and len(aPCards) == 2:
        if len(sPCards) == 2:
            sPCards.append(r.choice(cardBase))
            i = len(sPCards) - 1
            cardBase.remove(sPCards[i])
        # dealer sim
        dealer_sim(sDCards)
        # endgame
        sim_endgame(sPCards, sDCards)
    double = (sum(simulationDouble) / len(simulationDouble))
    print('Double', double)
    simulationDouble.clear()
 
def sim_stand(sPCards, sDCards):
    simulationStand.append(1)
    while len(simulationStand) < games:
            # dealer sim
        dealer_sim(sDCards)
        #endgame
        sim_endgame(sPCards, sDCards)
    Stand = (sum(simulationStand) / len(simulationStand))
    print('Stand', Stand)
    simulationStand.clear()
            
def sim_split(sPCards, sDCards, splitSimulationSplit):
    splitSimulationSplit.append(1)
    while len(splitSimulationSplit) < games:
        if aPCards[0] == aPCards[1]:
            sSplitPCards = sPCards.copy()
            sPCards.remove(sPCards[1])
            sSplitPCards.remove(sSplitPCards[1])
            sPCards.append(r.choice(cardBase))
            sSplitPCards.append(r.choice(cardBase))
        #dealer sim
        dealer_sim(sDCards)
        #endgame
        sim_endgame(sPCards, sDCards)
    Split = (sum(splitSimulationSplit) / len(splitSimulationSplit))
    print('Split', Split)
    splitSimulationSplit.clear()

sim_hit(sPCards, sDCards, aPCards, aDCards)
