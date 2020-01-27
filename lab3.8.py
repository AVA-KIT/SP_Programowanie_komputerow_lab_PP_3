a = int(input('Ile wypiłeś czystego alkoholu: '))
w = float(input('Podaj swoją wagę w kg: '))
k = 0.7

p = a / (k*w)
print('Stężenie alkoholu we krwi wynosi {} promila.'.format(p))

