"""
Napisz funkcję która dla przykładu po wywołaniu:
print(count(2,4,1,2,4,5, 10))
pokaże jako wynik:
28
czyli sumę wszystkich argumentów.
"""

def count(*arg):
    suma = sum(arg)
    return suma

print(count(2, 4, 1, 2, 4, 5, 10))