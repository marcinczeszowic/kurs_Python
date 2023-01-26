"""Zasięg zmiennych"""

def add(): # zmienna lokalna jest stworzona wewnątrz funkcji i jest tylko dostepna w funkcji
    global c
    c = c + 4
    print(c)

def add2(c, amount = 1):
    c = c + amount
    print(c)

c = 1 # zmienna globalna jest dostępna dla wszyskich funkcji
#add()
add2(c)
print(c)
