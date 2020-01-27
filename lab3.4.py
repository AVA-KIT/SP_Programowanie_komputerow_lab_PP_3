suma = 0
while suma <= 100:
    a = int(input('Proszę podać wartość: '))
    lista = []
    lista.append(a)
    for el in lista:
        suma += el
print('Suma=',suma)
