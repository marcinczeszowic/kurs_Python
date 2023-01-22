import sys
evenNumbers = [element for element in range(400) if (element % 2 == 0)]

evenNumbersGemerator = (element for element in range(400) if (element % 2 == 0))
evenNumbersGemeratorPot = (element**2 for element in range(100))


print(evenNumbers)

print(sum(evenNumbersGemerator))
print(sum(evenNumbersGemeratorPot))

print(sys.getsizeof(evenNumbers))
print(sys.getsizeof(evenNumbersGemerator))

for item in evenNumbersGemeratorPot:
    print(item)



