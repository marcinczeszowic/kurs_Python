'''
funkja - to blok kodu do którego można się odwołać w każdej chwili ,
        aby otrzymać pożądany przez nas wynik
        def = definition
        def nazwa_funkcji(argumenty):
            instrukcja1
            instrukcja2

        nazwa_funkcji(argument)
'''

def wiadomoscPowitalna(imie):
    print(f"Cześć {imie}, miło mi powitać Cię w moim programie!")

"""wywołanie bez pętli"""
wiadomoscPowitalna('Marcinie')
wiadomoscPowitalna('Andrzeju')
wiadomoscPowitalna('Anno')

"""wywołanie w pętli"""
imiona = ['Marcinie', 'Andrzeju', 'Anno']

for imie in imiona:
    wiadomoscPowitalna(imie)

