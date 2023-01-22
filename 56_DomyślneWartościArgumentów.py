"""
Domyślne argumenty
"""

def increment(x, amount=1):
    return x + amount

#print(increment(4, 20))
#print(increment(4))

import time


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

def finish_timer(start):
    end = time.perf_counter()
    return end - start

def function_Performance(func, arg=5, how_meny_times=1):
    sum = 0
    for i in range(0, how_meny_times):
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        sum = sum + (end - start)
    return sum

def show_messsage(message):
    print(message)

print(function_Performance(sumujDo, 500, 40))
print(function_Performance(sumujDo2, 500, 50))
print(function_Performance(sumujDo3, 500))
print(function_Performance(sumujDo4, 500))
print(function_Performance(sumujDo5))