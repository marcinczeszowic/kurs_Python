# dictionary - słownik KLUCZ - WARTOSC
pokoje  = {49: "Arkadiusz Włodarczyk",
           69: "Marcin Czeszowic"}

print(pokoje)
pokoje[49] = 'dupek'
print(pokoje)
pokoje[50] = 'dupek2'
print(pokoje)
print(pokoje.get(49))
pokoje.update({400: 'ciotex'})
print(pokoje)
del(pokoje[400])
print(pokoje)
print(pokoje.pop(50))
print(len(pokoje))
pokoje.clear()
print(pokoje)

