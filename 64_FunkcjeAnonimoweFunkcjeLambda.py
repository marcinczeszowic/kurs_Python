def podwoj(x):
    return x * 2

print(podwoj(4))

def funkja_dla_filtrowania(x):
    if (x % 2) == 0:
        return x


print((lambda x: x * 2)(4))

my_list = [2, 14, 22, 7, 6, 4, 1, 17]

my_filtered_list = list(filter(lambda x: x % 2 == 0, my_list))
print(my_filtered_list)

my_filtered_list2 = list(filter(funkja_dla_filtrowania, my_list))
print(my_filtered_list2)

my_filtered_list3 = [x for x in my_list if(x % 2) == 0]
print(my_filtered_list3)