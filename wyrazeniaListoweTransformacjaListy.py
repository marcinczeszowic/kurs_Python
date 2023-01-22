liczby = [1,2,3,4,5,6]

potegiDwojki = []
for element in liczby:
    potegiDwojki.append(element ** 2)

liczbyParzyste = []
for element in liczby:
    if (element % 2 == 0):
        liczbyParzyste.append(element)

liczbyNieParzyste = []
for element in liczby:
    if (element % 2 != 0):
        liczbyNieParzyste.append(element)

potegiDwojki2 = [element**2 for element in liczby]
liczbyParzyste2 = [element for element in liczby if (element % 2 == 0)]
liczbyNieParzyste2 = [element for element in liczby if (element % 2 != 0)]

'''
[co_zrobić_na_elemencie | for element in stara_lista | warunek_oparty_na_elemencie]
'''

print(potegiDwojki)
print(potegiDwojki2)
print(liczbyParzyste)
print(liczbyParzyste2)
print(liczbyNieParzyste)
print(liczbyNieParzyste2)

