"""Napisz program który policzy sumę wszystkich liczb od 1 do podanej liczby
Dla np. 5
1+2+3+4+5
zwróci
15
"""
"""pętla z uzyciem range"""

def sumujDo(liczba):
    suma = 0
    for liczba in range(1, liczba+1):
        suma = suma + liczba
    return suma


def sumujDo2(liczba):
   return sum([liczba for liczba in range(1, liczba+1)])

def sumujDo3(liczba):
   return sum({liczba for liczba in range(1, liczba+1)})

def sumujDo4(liczba):
   return sum((liczba for liczba in range(1, liczba+1)))

def sumujDo5(liczba):
   return (1 + liczba) / 2 * liczba


print(sumujDo(5))
print(sumujDo2(5))
print(sumujDo3(5))
print(sumujDo4(5))
print(sumujDo5(5))