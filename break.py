"""
break


continue
"""
"""
wynik = 0

for i in range(3):
    x = int(input("Podaj dodatnią liczbę: "))
    if (x>0):
        wynik += x
    else:
        print("miała byc liczba dodatnia program się zakończy")
        break
    print("aktualny wynik dodawania to:", wynik)
"""
"""
for i in range(3):
    x = int(input("Podaj dodatnią liczbę: "))
    if (x>0):
        wynik += x
    else:
        print("miała byc liczba dodatnia program się zakończy")
        continue
    print("aktualny wynik dodawania to:", wynik)
"""
"""
wynik = 0
i = 0
while i < 3:
    x = int(input("Podaj dodatnią liczbę: "))
    if (x > 0):
        wynik += x
    else:
        print("miała byc liczba dodatnia program się zakończy")
        continue

    print("aktualny wynik dodawania to:", wynik)
    i += 1
 """
wynik = 0
i = 0
while i < 3:
    x = int(input("Podaj dodatnią liczbę: "))
    if (x%2 == 0):
        wynik += x
    else:
        print("miała byc liczba dodatnia program się zakończy")
        continue

    print("aktualny wynik dodawania liczb pazystych to:", wynik)
    i += 1

    Zadanie: Dodawanie
    liczb
    parzystych
    podanych
    przez
    użytkownika