
liczba = 0

while liczba <= 5:
    print(liczba)
    liczba +=1
liczba = 10

while liczba >= 0:
    print(liczba)
    liczba -=1

wynik = 0
i = 0

while i < 4:
    x = int(input("podaj liczbe: "))
    wynik += x
    i += 1

print(f'wynik to:{wynik}')
wynik = 0

for i in range (4):
    x = int(input("podaj liczbe: "))
    wynik += x


print(f'wynik to:{wynik}')

for i in range (40):
    if (i % 2 == 0):
        print(f"liczba {i} jest parzysta")




