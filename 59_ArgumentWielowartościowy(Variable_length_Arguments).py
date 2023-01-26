import time

def function_performance(func, *arg, how_many_times = 1):
    sum = 0
    print(arg[0])
    #print(arg[1])

    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(*arg)
        end = time.perf_counter()
        sum = sum + (end-start)

    return sum

def function_performance2(func, how_many_times = 1, *arg):
    sum = 0
    print(arg[0])
    print(arg[1])
    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(*arg)
        end = time.perf_counter()
        sum = sum + (end-start)

    return sum

def function_performance3(func, how_many_times = 1, **arg):
    sum = 0
    print(arg.get("what_value"))
    print(arg.get("container"))
    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(**arg)
        end = time.perf_counter()
        sum = sum + (end-start)

    return sum

setContainer = {i for i in range(1000)}
listContainer = [i for i in range(1000)]

def is_element_in(what_value, container):
    if what_value in container:
        return True
    else:
        return False


print(function_performance(is_element_in, 500, setContainer, how_many_times=1))
print(function_performance(is_element_in, 500, listContainer, how_many_times=1))
print(function_performance2(is_element_in, 1, 500, listContainer))
print(function_performance3(is_element_in, 1, what_value=500, container=setContainer))

"""ARGUMENTY POZYCYJNE (NIENAZWANE) PRZED ARGUMENTAMI NAZWANYMI"""

