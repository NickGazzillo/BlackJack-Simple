try:
    dealer = int(input('What card does the dealer have? '))
    first = int(input('What is your first card? '))
    second = int(input('What is your second card? '))
    total = first + second
    if dealer <= 11 and first <= 11 and second <= 11:
        # first round of if statements are for pairs
        if first == second:
            if 2 <= first <= 3 or first == 7:
                if 2 <= dealer <= 7:
                    print('Split!')
                elif 8 <= dealer <= 11:
                    print('Hit! ')
            if first == 4:
                if 2 <= dealer <= 4 or 7 <= dealer <= 11:
                    print('Hit! ')
                elif 5 <= dealer <= 6:
                    print('Split! ')
            if first == 5:
                if 2 <= dealer <= 9:
                    print('Double! ')
                elif 10 <= dealer <= 11:
                    print('Hit! ')
            if first == 6:
                if 2 <= dealer <= 6:
                    print('Split! ')
                elif 7 <= dealer <= 11:
                    print('Hit! ')
            if first == 8:
                print('Split! ')
            if first == 9:
                if 2 <= dealer <= 6 or 8 <= dealer <= 9:
                    print('Split! ')
                elif dealer == 7 or 10 <= dealer <= 11:
                    print('Stand! ')
            if first == 10:
                print('Stand! ')
            if first == 11:
                print('Split! ')
        # second round of if statements are for Ace variants in blackjack
        elif first == 11 or second == 11:
            if dealer >= 7 and total <= 17:
                print('Hit! ')
            if 13 <= total <= 14:
                if 2 <= dealer <= 4:
                    print('Hit! ')
                elif 5 <= dealer <= 6:
                    print('Double! ')
            if 15 <= total <= 16:
                if 2 <= dealer <= 3:
                    print('Hit! ')
                elif 4 <= dealer <= 6:
                    print('Double')
            if total == 17:
                if 2 <= dealer <= 6:
                    print('Double')
            if total == 18:
                if dealer == 2:
                    print('Stand! ')
                elif 2 <= dealer <= 6:
                    print('Double!')
                elif 7 <= dealer <= 8:
                    print('Stand! ')
                elif 9 <= dealer <= 11:
                    print('Hit! ')
            if 19 <= total <= 20:
                print('Stand! ')
        # third round of if statements are normal black jack play
        elif first != 11 or second != 11 and first != second:
            if total <= 8:
                print('Hit!')
            elif total >= 17:
                print('Stand!')
            elif total == 9:
                if 3 <= dealer <= 6:
                    print('Double! ')
                elif dealer == 2 or dealer >= 7:
                    print('Hit! ')
            elif total == 10:
                if 2 <= dealer <= 9:
                    print('Double! ')
                elif dealer >= 10:
                    print('Hit! ')
            elif total == 11:
                if dealer != 11:
                    print('Double! ')
                elif dealer == 11:
                    print('Stand! ')
            elif total == 12:
                if 4 <= dealer <= 6:
                    print('Stand! ')
                elif 2 <= dealer <= 3 or dealer >= 7:
                    print('Hit! ')
            elif 13 <= total <= 16:
                if 2 <= dealer <= 6:
                    print('Stand! ')
                elif dealer >= 7:
                    print('Hit! ')
        else:
            print('Please put numbers between 1-11(Ace = 11, Face cards = 10)')
except:
    print('Please only put numerical symbols(Ace = 11, Face cards = 10)')