'''
Jeżeli (PRAWDA)
TO...
JEZELI CO INNEGO (PRAWDA)
TO...
A CALKOWICIE W INNYM WYPADKU
TO...
'''
if (5 > 3):
    print("lalalala")

if (5 < 3):
    print("lalalala")
    print("tralalala")

#wybor = input("1 - mnożenie, 2 - dzielenie, 3 - dodawanie, 4 - odejmowanie")    

a = int(input("podaj pierwszą liczbę: "))
b = int(input("podaj drugą liczbę: "))

if (a > b):
    print("a jest większe od b")
elif (b > a):    
    print("b jest większe od a")
else:
    print("a jest równe b")
    

wybor = int(input("1 - mnożenie, 2 - dzielenie, 3 - dodawanie, 4 - odejmowanie " ))

a = int(input("podaj pierwszą liczbę: "))
b = int(input("podaj drugą liczbę: "))

if (wybor == 1):
    print(a * b)
elif (wybor == 2):
    if (b == 0):
        print("Nie dziel cholero przez zero")
    else:   
        print(a / b)
elif (wybor == 3):
    print(a + b)
elif (wybor == 4):
    print(a - b)
else:
    print("wybierz między 1 a 4 ")



    
    
