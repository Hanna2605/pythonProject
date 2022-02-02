tuple_1 = tuple(input('Input 5 numbers: '))
tuple_2 = tuple(input('Input 3 numbers: '))
index = 0
tuple_3 = []
for num in tuple_1:
    tuple_3.append(num)
    index += 1
    if index == 2:
        for num in tuple_2:
            tuple_3.append(num)
            index += 1
        continue
print(tuple(tuple_3))


