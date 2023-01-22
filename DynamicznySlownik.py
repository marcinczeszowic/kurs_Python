"""
Napisz program, który pozwoli użytkownikowi:
1) Dodawać nowe definicję
2) Szukać istniejacych definicji
3) Usuwać wybrane przez niego definicję
"""
definicje = {}

while(True):
    print("1: Dodaj definicję")
    print("2: Znajdź definicję")
    print("3: Usuń definicję")
    print("4: Zakończ")

    wybor = input('Co chcesz zrobić ? ')

    if (wybor=="1"):
        klucz = input("Podaj Klucz słowo do zdefiniowania: ")
        definicja = input("Podaj definicję: ")
        definicje[klucz] = definicja
        print("Definicja dodana pomyślnie")
    elif (wybor=="2"):
        klucz = input("Czego szukasz ? ")
        if klucz in definicje:
            print(definicje[klucz])
        else:
            print('Nie znaleziono definicji o nazwie', klucz)
    elif (wybor=='3'):
        klucz = input("Jaką definicje chcesz usunąć? ")
        if klucz in definicje:
            del definicje[klucz]
            print('Usunięto definicję', klucz)
        else:
            print('Nie znaleziono definicji o nazwie', klucz)
    elif (wybor=='4'):
        print('nara')
        break
    else:
        print('podałeś cos z poza zakresu')



