"""
Użyj funkcji any(), aby określić, czy lista zawiera liczby parzyste
"""
# any = jakikolwiek - funkcja ta sprawdza czy jaka kolwiek wartość zwraca True
# all - wszystkie


numbers1 = [1, 3, 5, 6, 7]
numbers2 = [1, 3, 5, 7, 9]

#numbers1 = [nr % 2 == 0 for nr in numbers1]
#numbers2 = [nr % 2 == 0 for nr in numbers2]

def any_even(lista):
    #return ([nr % 2 == 0 for nr in lista])
    return any([nr % 2 == 0 for nr in lista])

def all_even(lista):
    #return ([nr % 2 == 0 for nr in lista])
    return all([nr % 2 == 0 for nr in lista])

print(any_even(numbers1))
print(any_even(numbers2))

print(all_even(numbers1))
print(all_even(numbers2))

if (any_even(numbers1)):
    print("tak jest parzysta")
else:
    print("nie jest parzysta")

if (any_even(numbers2)):
    print("tak jest parzysta")
else:
    print("nie jest parzysta")

john = {
    'name': 'John Doe',
    'age': 30,
    'skills': ['Python', 'JavaScript', 'C++']
        }
jane = {
    'name': 'Jane Smith',
    'age': 25,
    'skills': ['Python', 'Java']
        }





