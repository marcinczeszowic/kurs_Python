szukanaLiczba = 20
zgadywanaLiczba = 0


while zgadywanaLiczba !=szukanaLiczba:
    zgadywanaLiczba = int(input('Odgadnij Liczbę: '))

    if zgadywanaLiczba > szukanaLiczba:
        print('Liczba jest za duża')
    elif zgadywanaLiczba < szukanaLiczba:
        print('Liczba jest za mała')
    else:
        print("BRAWO")


