imiona = ['Arkadiusz', 'Wiola', 'Antek']
imie = input('Wpisz imię aby mieć dostęp: ')
imie = imie.capitalize()

if imie in imiona:
    print('Masz dostęp')
else:
    print('Brak dostępu')

if imie == "Arkadiusz" or 'Wiola': # niepoprawny zapis
    print('Masz dostęp')
else:
    print('Brak dostępu')

if imie == "Arkadiusz" or imie == 'Wiola': # poprawny zapis
    print('Masz dostęp')
else:
    print('Brak dostępu')