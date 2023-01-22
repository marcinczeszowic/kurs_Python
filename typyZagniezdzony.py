imie = "Arkadiusz"
wiek = 29
plec = "facet"

imie2 = "Wioletta"
wiek2 = 23
plec2 = "Babka"

osoba1 = ('Arkadiusz', 29, "facet")
osoba2 = ('Wioletta', 29, "Babka")
osoba3 = ('Kuba', 33, "facet")

ListaGosci = [
                ['Arkadiusz', 29, "facet"],
                ['Wioletta', 29, "Babka"],
                ['Kuba', 33, "facet"]
             ]
ListaGosci[0][1] = 29

print(ListaGosci[0][0])
print(ListaGosci[0])
print(ListaGosci[1][2])
print(ListaGosci[0][1])

#krotka
ListaGosci = [
                ('Arkadiusz', 29, "facet"),
                ('Wioletta', 29, "Babka"),
                ('Kuba', 33, "facet")
             ]

ListaGosci.append(('Karol', 26, 'facet'))
print(ListaGosci)

#zbiór
ListaGosci = {
                ('Arkadiusz', 29, "facet"),
                ('Wioletta', 29, "Babka"),
                ('Kuba', 33, "facet")
            }

ListaGosci.add(('Karol', 26, 'facet'))
print(ListaGosci)
ListaGosci2 = {
                ('Arkadiusz', 29, "facet"),
                ('W', 29, "Babka"),
                ('K', 33, "facet")
            }
ListaGosci3 = ListaGosci | ListaGosci2

print(ListaGosci3)
# sprawdzanie czy dane sa w obydwóch liczbach
ListaGosci3 = ListaGosci & ListaGosci2
print(ListaGosci3)