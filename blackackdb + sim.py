import gspread as g
sPCards = []
sDCards = []
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
def db(sDCards, sPCards, aDCards, aPCards):
    sa = g.service_account(filename='blackjackddatabase.json')
    sh = sa.open('Blackjack')
    wks = sh.worksheet('Hit')
    if sum(sPCards) == 2:
        if sum(sDCards) == 2:
            find = 'B3'
        if sum(sDCards) == 3:
            find = 'C3'
        if sum(sDCards) == 4:
            find = 'D3'
        if sum(sDCards) == 5:
            find = 'E3'
        if sum(sDCards) == 6:
            find = 'F3'
        if sum(sDCards) == 7:
            find = 'G3'
        if sum(sDCards) == 8:
            find = 'H3'
        if sum(sDCards) == 9:
            find = 'I3'
        if sum(sDCards) == 10:
            find = 'J3'
        if sum(sDCards) == 11:
            find = 'K3'
    if sum(sPCards) == 3:
        if sum(sDCards) == 2:
            find = 'B4'
        if sum(sDCards) == 3:
            find = 'C4'
        if sum(sDCards) == 4:
            find = 'D4'
        if sum(sDCards) == 5:
            find = 'E4'
        if sum(sDCards) == 6:
            find = 'F4'
        if sum(sDCards) == 7:
            find = 'G4'
        if sum(sDCards) == 8:
            find = 'H4'
        if sum(sDCards) == 9:
            find = 'I4'
        if sum(sDCards) == 10:
            find = 'J4'
        if sum(sDCards) == 11:
            find = 'K4'
    if sum(sPCards) == 4:
        if sum(sDCards) == 2:
            find = 'B5'
        if sum(sDCards) == 3:
            find = 'C5'
        if sum(sDCards) == 4:
            find = 'D5'
        if sum(sDCards) == 5:
            find = 'E5'
        if sum(sDCards) == 6:
            find = 'F5'
        if sum(sDCards) == 7:
            find = 'G5'
        if sum(sDCards) == 8:
            find = 'H5'
        if sum(sDCards) == 9:
            find = 'I5'
        if sum(sDCards) == 10:
            find = 'J5'
        if sum(sDCards) == 11:
            find = 'K5'
    if sum(sPCards) == 5:
        if sum(sDCards) == 2:
            find = 'B6'
        if sum(sDCards) == 3:
            find = 'C6'
        if sum(sDCards) == 4:
            find = 'D6'
        if sum(sDCards) == 5:
            find = 'E6'
        if sum(sDCards) == 6:
            find = 'F6'
        if sum(sDCards) == 7:
            find = 'G6'
        if sum(sDCards) == 8:
            find = 'H6'
        if sum(sDCards) == 9:
            find = 'I6'
        if sum(sDCards) == 10:
            find = 'J6'
        if sum(sDCards) == 11:
            find = 'K6'
    if sum(sPCards) == 6:
        if sum(sDCards) == 2:
            find = 'B7'
        if sum(sDCards) == 3:
            find = 'C7'
        if sum(sDCards) == 4:
            find = 'D7'
        if sum(sDCards) == 5:
            find = 'E7'
        if sum(sDCards) == 6:
            find = 'F7'
        if sum(sDCards) == 7:
            find = 'G7'
        if sum(sDCards) == 8:
            find = 'H7'
        if sum(sDCards) == 9:
            find = 'I7'
        if sum(sDCards) == 10:
            find = 'J7'
        if sum(sDCards) == 11:
            find = 'K7'
    if sum(sPCards) == 7:
        if sum(sDCards) == 2:
            find = 'B8'
        if sum(sDCards) == 3:
            find = 'C8'
        if sum(sDCards) == 4:
            find = 'D8'
        if sum(sDCards) == 5:
            find = 'E8'
        if sum(sDCards) == 6:
            find = 'F8'
        if sum(sDCards) == 7:
            find = 'G8'
        if sum(sDCards) == 8:
            find = 'H8'
        if sum(sDCards) == 9:
            find = 'I8'
        if sum(sDCards) == 10:
            find = 'J8'
        if sum(sDCards) == 11:
            find = 'K8'
    if sum(sPCards) == 8:
        if sum(sDCards) == 2:
            find = 'B9'
        if sum(sDCards) == 3:
            find = 'C9'
        if sum(sDCards) == 4:
            find = 'D9'
        if sum(sDCards) == 5:
            find = 'E9'
        if sum(sDCards) == 6:
            find = 'F9'
        if sum(sDCards) == 7:
            find = 'G9'
        if sum(sDCards) == 8:
            find = 'H9'
        if sum(sDCards) == 9:
            find = 'I9'
        if sum(sDCards) == 10:
            find = 'J9'
        if sum(sDCards) == 11:
            find = 'K9'
    if sum(sPCards) == 9:
        if sum(sDCards) == 2:
            find = 'B10'
        if sum(sDCards) == 3:
            find = 'C10'
        if sum(sDCards) == 4:
            find = 'D10'
        if sum(sDCards) == 5:
            find = 'E10'
        if sum(sDCards) == 6:
            find = 'F10'
        if sum(sDCards) == 7:
            find = 'G10'
        if sum(sDCards) == 8:
            find = 'H10'
        if sum(sDCards) == 9:
            find = 'I10'
        if sum(sDCards) == 10:
            find = 'J10'
        if sum(sDCards) == 11:
            find = 'K10'
    if sum(sPCards) == 10:
        if sum(sDCards) == 2:
            find = 'B11'
        if sum(sDCards) == 3:
            find = 'C11'
        if sum(sDCards) == 4:
            find = 'D11'
        if sum(sDCards) == 5:
            find = 'E11'
        if sum(sDCards) == 6:
            find = 'F11'
        if sum(sDCards) == 7:
            find = 'G11'
        if sum(sDCards) == 8:
            find = 'H11'
        if sum(sDCards) == 9:
            find = 'I11'
        if sum(sDCards) == 10:
            find = 'J11'
        if sum(sDCards) == 11:
            find = 'K11'
    if sum(sPCards) == 11:
        if sum(sDCards) == 2:
            find = 'B12'
        if sum(sDCards) == 3:
            find = 'C12'
        if sum(sDCards) == 4:
            find = 'D12'
        if sum(sDCards) == 5:
            find = 'E12'
        if sum(sDCards) == 6:
            find = 'F12'
        if sum(sDCards) == 7:
            find = 'G12'
        if sum(sDCards) == 8:
            find = 'H12'
        if sum(sDCards) == 9:
            find = 'I12'
        if sum(sDCards) == 10:
            find = 'J12'
        if sum(sDCards) == 11:
            find = 'K12'
    if sum(sPCards) == 12:
        if sum(sDCards) == 2:
            find = 'B13'
        if sum(sDCards) == 3:
            find = 'C13'
        if sum(sDCards) == 4:
            find = 'D13'
        if sum(sDCards) == 5:
            find = 'E13'
        if sum(sDCards) == 6:
            find = 'F13'
        if sum(sDCards) == 7:
            find = 'G13'
        if sum(sDCards) == 8:
            find = 'H13'
        if sum(sDCards) == 9:
            find = 'I13'
        if sum(sDCards) == 10:
            find = 'J13'
        if sum(sDCards) == 11:
            find = 'K13'   
    if sum(sPCards) == 13:
        if sum(sDCards) == 2:
            find = 'B14'
        if sum(sDCards) == 3:
            find = 'C14'
        if sum(sDCards) == 4:
            find = 'D14'
        if sum(sDCards) == 5:
            find = 'E14'
        if sum(sDCards) == 6:
            find = 'F14'
        if sum(sDCards) == 7:
            find = 'G14'
        if sum(sDCards) == 8:
            find = 'H14'
        if sum(sDCards) == 9:
            find = 'I14'
        if sum(sDCards) == 10:
            find = 'J14'
        if sum(sDCards) == 11:
            find = 'K14'
    if sum(sPCards) == 14:
        if sum(sDCards) == 2:
            find = 'B15'
        if sum(sDCards) == 3:
            find = 'C15'
        if sum(sDCards) == 4:
            find = 'D15'
        if sum(sDCards) == 5:
            find = 'E15'
        if sum(sDCards) == 6:
            find = 'F15'
        if sum(sDCards) == 7:
            find = 'G15'
        if sum(sDCards) == 8:
            find = 'H15'
        if sum(sDCards) == 9:
            find = 'I15'
        if sum(sDCards) == 10:
            find = 'J15'
        if sum(sDCards) == 11:
            find = 'K15'
    if sum(sPCards) == 15:
        if sum(sDCards) == 2:
            find = 'B16'
        if sum(sDCards) == 3:
            find = 'C16'
        if sum(sDCards) == 4:
            find = 'D16'
        if sum(sDCards) == 5:
            find = 'E16'
        if sum(sDCards) == 6:
            find = 'F16'
        if sum(sDCards) == 7:
            find = 'G16'
        if sum(sDCards) == 8:
            find = 'H16'
        if sum(sDCards) == 9:
            find = 'I16'
        if sum(sDCards) == 10:
            find = 'J16'
        if sum(sDCards) == 11:
            find = 'K16'
    if sum(sPCards) == 16:
        if sum(sDCards) == 2:
            find = 'B17'
        if sum(sDCards) == 3:
            find = 'C17'
        if sum(sDCards) == 4:
            find = 'D17'
        if sum(sDCards) == 5:
            find = 'E17'
        if sum(sDCards) == 6:
            find = 'F17'
        if sum(sDCards) == 7:
            find = 'G17'
        if sum(sDCards) == 8:
            find = 'H17'
        if sum(sDCards) == 9:
            find = 'I17'
        if sum(sDCards) == 10:
            find = 'J17'
        if sum(sDCards) == 11:
            find = 'K17'
    if sum(sPCards) == 17:
        if sum(sDCards) == 2:
            find = 'B18'
        if sum(sDCards) == 3:
            find = 'C18'
        if sum(sDCards) == 4:
            find = 'D18'
        if sum(sDCards) == 5:
            find = 'E18'
        if sum(sDCards) == 6:
            find = 'F18'
        if sum(sDCards) == 7:
            find = 'G18'
        if sum(sDCards) == 8:
            find = 'H18'
        if sum(sDCards) == 9:
            find = 'I18'
        if sum(sDCards) == 10:
            find = 'J18'
        if sum(sDCards) == 11:
            find = 'K18'
    if sum(sPCards) == 18:
        if sum(sDCards) == 2:
            find = 'B19'
        if sum(sDCards) == 3:
            find = 'C19'
        if sum(sDCards) == 4:
            find = 'D19'
        if sum(sDCards) == 5:
            find = 'E19'
        if sum(sDCards) == 6:
            find = 'F19'
        if sum(sDCards) == 7:
            find = 'G19'
        if sum(sDCards) == 8:
            find = 'H19'
        if sum(sDCards) == 9:
            find = 'I19'
        if sum(sDCards) == 10:
            find = 'J19'
        if sum(sDCards) == 11:
            find = 'K19'
    if sum(sPCards) == 19:
        if sum(sDCards) == 2:
            find = 'B20'
        if sum(sDCards) == 3:
            find = 'C20'
        if sum(sDCards) == 4:
            find = 'D20'
        if sum(sDCards) == 5:
            find = 'E20'
        if sum(sDCards) == 6:
            find = 'F20'
        if sum(sDCards) == 7:
            find = 'G20'
        if sum(sDCards) == 8:
            find = 'H20'
        if sum(sDCards) == 9:
            find = 'I20'
        if sum(sDCards) == 10:
            find = 'J20'
        if sum(sDCards) == 11:
            find = 'K20'
    if sum(sPCards) == 20:
        if sum(sDCards) == 2:
            find = 'B21'
        if sum(sDCards) == 3:
            find = 'C21'
        if sum(sDCards) == 4:
            find = 'D21'
        if sum(sDCards) == 5:
            find = 'E21'
        if sum(sDCards) == 6:
            find = 'F21'
        if sum(sDCards) == 7:
            find = 'G21'
        if sum(sDCards) == 8:
            find = 'H21'
        if sum(sDCards) == 9:
            find = 'I21'
        if sum(sDCards) == 10:
            find = 'J21'
        if sum(sDCards) == 11:
            find = 'K21'
    if sum(sPCards) == 21:
        if sum(sDCards) == 2:
            find = 'B22'
        if sum(sDCards) == 3:
            find = 'C22'
        if sum(sDCards) == 4:
            find = 'D22'
        if sum(sDCards) == 5:
            find = 'E22'
        if sum(sDCards) == 6:
            find = 'F22'
        if sum(sDCards) == 7:
            find = 'G22'
        if sum(sDCards) == 8:
            find = 'H22'
        if sum(sDCards) == 9:
            find = 'I22'
        if sum(sDCards) == 10:
            find = 'J22'
        if sum(sDCards) == 11:
            find = 'K22'
    wks.update(find, 2)
