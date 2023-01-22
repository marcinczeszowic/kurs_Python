''' return - zwrócić '''

def poleProstokata(a, b):
    pole = a * b
    #print(f"pole prostokąta: {pole}")
    return pole

poleProstokataA = poleProstokata(2, 5)
poleProstokataB = poleProstokata(2, 6)


print(f" pole prostokata: {poleProstokataA}")
print(poleProstokataB)

def dzielenie(a, b):
    if (b == 0):
        return

    return a/b

print(dzielenie(10, 1))
print(dzielenie(10, 0))

x = dzielenie(10, 2)
if (x):
    print("ok", x)
else:
    print('podzieliłeś przez zero')