
imiona = ['Arkadiusz', 'Wiola', 'Karol', 'Kuba', 'Marcin']
liczby = [1, 54, -2, 20, 17, 2]


if ("Arkadiusz" in imiona):
    print('jest w liście')

if (2 not in liczby):
    print('nie ma takiej liczby w zbirze')
else:
    print("liczba 2 jest w zbiorze")

print('Wojtek' in imiona)

print(3 * liczby)
print([4] + liczby)