import random as r
decks = 2
aPCards = []
aDCards = []
cardBase = decks * [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
cardBaseOG =decks * [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
cardBase.insert(r.randint(7, decks * 10), 'cutCard')
question = input('play')
while question != 'no':
    while len(aPCards) != 2:
        aDCards.append(r.choice(cardBase))
        aPCards.append(r.choice(cardBase))
        i = len(aPCards) - 1     
        cardBase.remove(aPCards[i])
        cardBase.remove(aDCards[i])
        if aPCards[i] == 'cutCard' or aDCards[i] == 'cutCard':
            print('Pulled a cut card, reshuffling deck')
            cardBase = cardBaseOG.copy()
            cardBase.insert(r.randint(5, decks * 13), 'cutCard')
    aPCards.clear()
    aDCards.clear()
    print('cut', cardBase.index('cutCard'), 'len', len(cardBase))
    question = input('play?')
