lista = []
for i in range(4):
    lista.append(int(input('Wprowadź dowolną liczbę od 1 do 10: ')))
a = lista.count(5)
print('Użytkownik wybrał {} razy liczbę 5'.format(a))