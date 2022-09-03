import random as r
simulationHit = []
simulationDouble = []
simulationStand = []
splitSimulationSplit = []
decks = 6
games = 10001
sPCards = [2, 2]
sDCards = [2]
aPCards = [2, 2]
aDCards = [2]
sSplitPCards = []
cardBase = 6 * [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
weightedCardAverage = ((2 * cardBase.count(2) + 3 * cardBase.count(3) + 4 * cardBase.count(4) + 5 * cardBase.count(
    5) + 6 * cardBase.count(6) + 7 * cardBase.count(7) + 8 * cardBase.count(8) + 9 * cardBase.count(
    9) + 10 * cardBase.count(10) + 11 * cardBase.count(11)) / (decks * 13))

def sim_endgame(sPCards, sDCards):
    if len(simulationHit) > 0:
        x = simulationHit
    if len(simulationDouble) > 0:
        x = simulationDouble
    if len(simulationStand) > 0:
        x = simulationStand
    if len(splitSimulationSplit) > 0:
        x = splitSimulationSplit
    # if main deck wins
    if sum(sPCards) <= 21 and sum(sPCards) > sum(sDCards) or sum(sDCards) > 21:
        if x != simulationDouble:
            x.append(1)
        else:
            x.append(2)
        while len(sPCards) != len(aPCards):
            i = len(sPCards) - 1
            cardBase.append(sPCards[i])
            sPCards.remove(sPCards[i])
        while len(sDCards) != len(aPCards):
            i = len(sDCards) - 1
            cardBase.append(sDCards[i])
            sDCards.remove(sDCards[i])
    # if main deck loses
    if sum(sPCards) <= 21 and sum(sPCards) < sum(sDCards) or sum(sPCards) > 21:
        if x != simulationDouble:
            x.append(-1)
        else: 
            x.append(-2)
        while len(sPCards) != len(aPCards):
            i = len(sPCards) - 1
            cardBase.append(sPCards[i])
            sPCards.remove(sPCards[i])
        while len(sDCards) != len(aPCards):
            i = len(sDCards) - 1
            cardBase.append(sDCards[i])
            sDCards.remove(sDCards[i])
    # if side deck pushes with dealer
    if sum(sPCards) == sum(sDCards):
        x.append(0)
        while len(sPCards) != len(aPCards):
            i = len(sPCards) - 1
            cardBase.append(sPCards[i])
            sPCards.remove(sPCards[i])
        while len(sDCards) != 2:
            i = len(sDCards) - 1
            cardBase.append(sDCards[i])
            sDCards.remove(sDCards[i])
   
def dealer_sim(sDCards):
    while sum(sDCards) < 17:
        sDCards.append(r.choice(cardBase))
        i = len(sDCards) - 1
        cardBase.remove(sDCards[i])
     
def sim_hit(sPCards, sDCards, aPCards):
    simulationHit.append(1)
    while len(simulationHit) < games:
        if len(sPCards) == len(aPCards):
            sPCards.append(r.choice(cardBase))
            i = len(sPCards) - 1
            cardBase.remove(sPCards[i])
        # dealer sim
        dealer_sim(sDCards)
        # endgame
        sim_endgame(sPCards, sDCards)
    Hit = (sum(simulationHit) / len(simulationHit))
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
        
sim_hit(sPCards, sDCards, aPCards)
sim_double(sPCards, sDCards, aPCards)
sim_stand(sPCards, sDCards)
sim_split(sPCards, sDCards, splitSimulationSplit)
