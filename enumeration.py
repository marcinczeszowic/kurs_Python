# enumeration - spis - wyliczenie
import polaFigurDef
from enum import IntEnum

Menu_Figury = IntEnum('Menu_Figury', {'Kwadrat' :1, 'Prostokat' :2, 'Kolo' :3, 'Trojkat' :4, 'Trapez' :5})


wybor = int(input("""Wybierz figurę , której chcesz pole obliczyć: 
1. Kwadrat
2. Prostokąt
3. Koło
4. Trójkąt
5. Trapez
"""))


if (wybor == Menu_Figury.Kwadrat):
    a = float(input('Podaj bok kwadratu: '))
    print(f"pole kwadratu wynosi: {polaFigurDef.pole_kwadratu(a)}")
elif (wybor == Menu_Figury.Prostokat):
    a = float(input("Podaj 1-szy bok prostokąta: "))
    b = float(input("Podaj 2-gi bok prostokąta: "))
    print("Pole prostokąta wynosi:", polaFigurDef.pole_prostokata(a, b))
elif (wybor == Menu_Figury.Kolo):
    r = float(input("Podaj promień koła: "))
    print("Pole koła wynosi:", polaFigurDef.pole_kola(r))
elif (wybor == Menu_Figury.Trojkat):
    a = float(input("Podaj bok trójkąta: "))
    h = float(input("Podaj wysokość trójkąta: "))
    print("Pole trójkąta wynosi:", polaFigurDef.pole_trojkata(a, h))
elif (wybor == Menu_Figury.Trapez):
    a = float(input("Podaj 1-szy bok prostokąta: "))
    b = float(input("Podaj 2-gi bok prostokąta: "))
    h = float(input("Podaj wysokość trapezu: "))
    print("Pole trapezu wynosi:", polaFigurDef.pole_trapezu(a, b, h))