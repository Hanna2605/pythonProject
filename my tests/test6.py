lst_1 = list(input('Input numbers: '))
lst_2 = []
i = 0
for num in lst_1:
    a = num
    j = 0
    for num in lst_1:
        if a == num and i != j:
            if a in lst_2:
                break
            else:
                lst_2.append(a)
        j += 1
    i += 1
print(lst_2)


