import copy
"""
copy - płytka
deepcopy - głebokie kopiowanie

"""

def evil_function(toBeDestroyedList):
    print(id(toBeDestroyedList))
    toBeDestroyedList.clear()

def evil_function2(toBeDestroyedList):
    print(id(toBeDestroyedList))
    toBeDestroyedList[0][0] = 20
    print(toBeDestroyedList)

myList = [1, 4, 2, 1, 52, 3]

myList2 = [[1, 4], [2, 1], [52, 3]]
print(myList)

evil_function(myList.copy())
print(id(myList))
print(myList)

evil_function(myList)
print(id(myList))
print(myList)

evil_function2(copy.deepcopy(myList2))
print(myList2)

evil_function2(myList2.copy())
print(myList2)

evil_function(list(myList)) # to samo co copy
print(myList)

evil_function(myList[:]) # to samo co copy
print(myList)