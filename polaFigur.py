import math

while(True):
    def pole_kwadratu(a):
        return a * a
    def pole_prostokata(a, b):
        return a * b
    def pole_kola(r):
        return math.pi * r ** 2
    def pole_trojkata(a, h):
        return 0.5 * a * h
    def pole_trapezu(a, b, h):
        return (a + b) / 2 * h

    print("1: Pole kwadratu")
    print("2: Pole prostokata")
    print("3: Pole Koła")
    print("4: Pole trójkąta")
    print("5: Pole trapezu")
    print("6: Wyjście")

    wybor = input('Co chcesz zrobić ? ')
    if (wybor == '1'):
        a = int(input('podaj a: '))
        print("Pole kwadratu: ", pole_kwadratu(a))
    elif (wybor == '2'):
        a = int(input('podaj a: '))
        b = int(input('podaj b: '))
        print('Pole prostokata: ', pole_prostokata(a, b))
    elif (wybor == '3'):
        r = int(input('podaj r: '))
        print('Pole Koła: ', pole_kola(r))
    elif (wybor == '4'):
        a = int(input('podaj a: '))
        h = int(input('podaj h: '))
        print("Pole trójkąta", pole_trojkata(a, h))
    elif (wybor == '5'):
        a = int(input('podaj a: '))
        b = int(input('podaj b: '))
        h = int(input('podaj h: '))
        print('Pole trapezu: ', pole_trapezu(a, b, h))
    elif (wybor == '6'):
        break





