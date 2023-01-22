"""
funkcja jako zmienna
"""
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

def function_Performance(func, arg):
    start = time.perf_counter()
    func(arg)
    end = time.perf_counter()
    return end - start

def show_messsage(message):
    print(message)

print(function_Performance(sumujDo, 500))
print(function_Performance(sumujDo2, 500))
print(function_Performance(sumujDo3, 500))
print(function_Performance(sumujDo4, 500))
print(function_Performance(sumujDo5, 500))

"""
start = time.perf_counter()
print(sumujDo(5))
print(finish_timer(start))

start = time.perf_counter()
print(sumujDo2(5))
print(finish_timer(start))

start = time.perf_counter()
print(sumujDo3(5))
print(finish_timer(start))

start = time.perf_counter()
print(sumujDo4(5))
print(finish_timer(start))

start = time.perf_counter()
print(sumujDo5(5))
print(finish_timer(start))
"""