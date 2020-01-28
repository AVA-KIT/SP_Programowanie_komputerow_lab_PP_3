d = float(input('Podaj swój dochód w zł: '))

if d >= 85528:
    p = 14839.02 + (d - 85528) * 0.32
    print('Podatek wynosi: ',int(round(p,0)),' zł')
else:
    p = d * 0.18 - 556.02
    print('Podatek wynosi: ',int(round(p,0)), ' zł')


# powyższ metoda nie uwzględnia kwoty minimalnej wolnej od podatku.