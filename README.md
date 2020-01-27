# SP_Programowanie_komputerow_lab_PP_3
Studia podyplomowe Podstawy programowania - Python, Wydział Informatyki, ZUT w Szczecinie - Laboratorium 3 - Listy, krotki, słowniki, instrukcja warunkowa, pętle - cd.

Zadanie 1:
Zwykle odliczanie wsteczne kojarzy nam się ze startem rakiety. Proszę o wygenerowanie
(przy użyciu pętli while) liczb od 10 do zera i na końcu podanie komunikatu: „Rakieta
startuje!!!”.
10
9
8
7
6
5
4
3
2
1
Rakieta startuje!!!

Zadanie 2:
Proszę napisać skrypt wypisujący tabliczkę mnożenia (zwróć uwagę na wyrównanie liczb
do prawej strony, formatowanie typu %4d w print rezerwuje 4 znaki na liczę dziesiętną):
1 2 … 10
2 4 … …
… … … …
10 … … 100

Zadanie 3:
Proszę napisać skrypt, który będzie prosił użytkownika o wciśnięcie jednej z liter: „n” lub
„c”. Jeżeli użytkownik wciśnie jedną z właściwych liter, program ma wygenerować
komunikat: „Dziękuję!”. Jeżeli użytkownik wciśnie inną literę, program ma go o tym fakcie
poinformować i dać mu kolejną szansę na wciśnięcie właściwej litery. Do skutku.

Zadanie 4:
Napisz skrypt, który będzie pobierał wartości od użytkownika tak długo, dopóki suma
wprowadzonych wartości nie przekroczy liczby 100. Program ma zakończyć się
wypisaniem uzyskanej sumy. Np.
Proszę podać wartość: 10
Proszę podać wartość: 40
Proszę podać wartość: 70
KONIEC. Suma = 120

Zadanie 5:
Proszę, używając pętli for, napisać skrypt, który poprosi o wpisanie sześciu wartości. Po
wpisaniu tych wartości program ma podsumować ile razy wprowadzona została wartość
5.
Wprowadź dowolną liczbę od 1 do 10: 2
Wprowadź dowolną liczbę od 1 do 10: 3
Wprowadź dowolną liczbę od 1 do 10: 5
Wprowadź dowolną liczbę od 1 do 10: 5
Wprowadź dowolną liczbę od 1 do 10: 5
Użytkownik wybrał 3 razy liczbę 5.

Zadanie 6:
Korzystając z pętli, napisz skrypt do generowania następującego wzoru:
*
**
***
****

Zadanie 7:
Dana jest zagnieżdżona lista: R = [ ["CA","NV","UT"], ["NJ","NY","DE"] ]. Używając pętli for,
proszę wyświetlić elementy listy zgodnie ze wzorem:
CA
NV
UT
NJ
NY
DE

Zadanie 8:
Napisz program, który wykorzysta wzór Erika Widmarka
(https://pl.wikipedia.org/wiki/Zawartość_alkoholu_we_krwi#Wz.C3.B3r_Erika_Widmar
ka) i obliczy stężenie alkoholu we krwi pewnego konsumenta napojów wyskokowych.
Program powinien zapytać o ilość wypitego czystego alkoholu oraz o wagę delikwenta w
kilogramach. Współczynnik K przyjmij taki, jaki odpowiada twojej płci. Wyprowadź na
ekran obliczone stężenie alkoholu w promilach. Sprawdź otrzymane wyniki podstawiając
przygotowane własnoręcznie dane testowe.

Zadanie 9:
Napisz program, który zapyta użytkownika o wartość zmiennej rzeczywistej x, a
następnie obliczy wartość następujących wyrażeń:
1. 3x3 - 2x2 +3x - 1, dla x = 0 wyrażenie przybiera wartość -1 , dla x = 1: 3 a dla x=-1: -9

Zadanie 10:
Obecnie obowiązująca w Polsce skala podatku PIT mówi, że podatek oblicza się
następująco:
• przy dochodzie nie przekraczającym 85528 zł: podatek = 18% dochodu minus 556
zł 02 gr
• przy dochodzie równym bądź wyższym od 85528 zł: podatek = 14 839 zł 02 gr +
32 % nadwyżki ponad 85 528 zł
Napisz program, który zapyta użytkownika o jego dochód i obliczy podatek dochodowy.
Pamiętaj, że podatek zaokrąglamy do pełnych złotych. Przetestuj swój kod używając
następujących danych: 10 000 zł (1 244 zł), 50 000 zł (8 444 zł), 100 000 zł (19 470 zł),
200 000 zł (51 470 zł). Uwaga: opisana metoda czegoś nie uwzględnia - czego? (napisz w
komentarzu do programu).

Zadanie 11:
Niemiecki matematyk Carl Friedrich Gauss opracował algorytm obliczania daty
Wielkanocy, który opisany jest poniżej. Napisz program, który zapyta użytkownika o rok
z przedziału od 1900 do 2099, a następnie poda datę Wielkanocy w tym roku.
Algorytm:
• dzielimy liczbę roku przez 19 i znajdujemy resztę a
• dzielimy liczbę roku przez 4 i znajdujemy resztę b
• dzielimy liczbę roku przez 7 i znajdujemy resztę c
• resztę a mnożymy przez 19, do iloczynu dodajemy 24, sumę dzielimy przez 30 i
znajdujemy resztę d
• dzielimy (2b + 4c + 6d + 5) przez 7 i znajdujemy resztę e
• sprawdzamy, czy d + e < 10; jeśli tak, to Wielkanoc jest (d + e + 22) marca, jeśli nie,
to (d + e – 9) kwietnia.
Przetestuj swój kod używając następujących danych: 1999 (4.IV), 2013 (31.III), 2008
(23.III), 2022 (17.IV), sprawdź też bieżący rok…
