
import polaFigurDef

a = polaFigurDef.pole_kwadratu(2)
print(a)

wybor = input("""Wybierz figurę , której chcesz pole obliczyć: 
1. Kwadrat
2. Prostokąt
3. Koło
4. Trójkąt
5. Trapez
""")

if (wybor == '1'):
    a = float(input('Podaj bok kwadratu: '))
    print(f"pole kwadratu wynosi: {polaFigurDef.pole_kwadratu(a)}")
elif (wybor == '2'):
    a = float(input("Podaj 1-szy bok prostokąta: "))
    b = float(input("Podaj 2-gi bok prostokąta: "))
    print("Pole prostokąta wynosi:", polaFigurDef.pole_prostokata(a, b))
elif (wybor == '3'):
    r = float(input("Podaj promień koła: "))
    print("Pole koła wynosi:", polaFigurDef.pole_kola(r))
elif (wybor == '4'):
    a = float(input("Podaj bok trójkąta: "))
    h = float(input("Podaj wysokość trójkąta: "))
    print("Pole trójkąta wynosi:", polaFigurDef.pole_trojkata(a, h))
elif (wybor == '5'):
    a = float(input("Podaj 1-szy bok prostokąta: "))
    b = float(input("Podaj 2-gi bok prostokąta: "))
    h = float(input("Podaj wysokość trapezu: "))
    print("Pole trapezu wynosi:", polaFigurDef.pole_trapezu(a, b, h))
