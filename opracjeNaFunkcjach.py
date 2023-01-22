imiona = ['Arkadiusz', 'Wiola', 'Karol', 'Kuba', 'Marcin']
liczby = [1, 54, -2, 20, 17, 2]
#len - długość
print(len(imiona))
#append dodawanie do listy
liczby.append(5)
print(liczby)
#extend
liczby.extend([2, 2 ,1 , 1])
#insert(index, co) - wstaw
imiona.insert(2,'Jola')
print(imiona)
#index - indeks danego elementu
print(liczby.index(-2))
#print(liczby.index(8))
#sort(reverse=False) - sortowanie rosnąco
liczby.sort()
print(liczby)
liczby.sort(reverse=True)
print(liczby)
#max
print(max(liczby))
#min
print(min(liczby))
#count ile razy coś wystąpiło
print(liczby.count(54))
#pop usun ostatni element
liczby.pop()
liczby.pop()

print(liczby)
#remowe - usuń pierwsze wystąpienie
liczby.remove(1)
print(liczby)
#clear - wyczyść listę
liczby.clear()
print(liczby)
#reverse - zmien kolejność
liczby.reverse()
print(liczby)

numbers = [2, 5, 2, 10, 15, 6]
numbers.insert(3,11)
numbers.append(4)
print(len(numbers))


