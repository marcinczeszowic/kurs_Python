A = {1, 4, 20, 24, 5, 20, 5}
B = {2, 1, 25, 40, 20}
print(A)
A.add(7)
print(A)
print(set(A))

# wspólne elementy zbioru a i b
print(A & B)

# wszyskie elementy zbioru a i b
print(A | B)

# odejmowanie zbiorów
print(A)
print(B)
print(A - B)
print(B - A)
# alternatywa wykluczająca ( wyklucza wspólne wartości )
print(A^B)

# usuwanie elemenrtów
A.discard(1)
print(A)
# sprawdzanie podzbiorów
print(A.issubset(B))

