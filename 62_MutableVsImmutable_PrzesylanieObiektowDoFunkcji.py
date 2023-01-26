"""
obiekt to zmienna, która ma więcej mozliwości,
mozna wywałać na nim "funkcję"
może mieć więcej niż 1 wartość

obiekty immutable: bool, int, float, tuple, str
obiekty mutable: listy[],

immutable - niezmienne
mutable - zmienny
= Zmiana miejsca wskazywania na nowy adres , na inny obiekt
"""





listSample = [1,4,512,24]
print(id(listSample))

listSample2 = listSample
print(id(listSample))

listSample2.append(465)
print(id(listSample))

print(listSample)
print(listSample2)


a = 4
print(id(a))
b = a
print(id(b))
b = 7
print(id(b))
print(a.bit_length())
print(a)
print(b)

k = 4
h = 4
print(id(k)," ",  id(h))

k = 4
h = 5
print(id(k)," ",  id(h))

c = 5
print(id(c))
def add(c, amount = 1):
    print(id(c))
    c = c + amount
    print(id(c))

#add(c)

def append_element_to_list(listka, element):
    print(id(listka))
    listka.append(element)
    print(id(listka))

print(id(listSample))
append_element_to_list(listSample, 5)
