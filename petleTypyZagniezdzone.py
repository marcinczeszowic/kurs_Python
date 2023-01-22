imie = "Arkadiusz"
wiek = 29
plec = "facet"

imie2 = "Wioletta"
wiek2 = 23
plec2 = "Babka"

osoba1 = ('Arkadiusz', 29, "facet")
osoba2 = ('Wioletta', 29, "Babka")
osoba3 = ('Kuba', 33, "facet")



listaGosci = {
                ('Arkadiusz', 29, "facet"),
                ('Wioletta', 29, "Babka"),
                ('Kuba', 33, "facet")
             }

listaGosci2 = {
                ('Arkadiusz', 29, "facet"),
                ('W', 29, "Babka"),
                ('K', 33, "facet")
              }
listaGosci3 = listaGosci & listaGosci2

for imie, wiek, plec in listaGosci:
    print(f"{imie},{wiek},{plec}")
    print()