mas = []
mas1 = []
k = 1
tur = 0 #Cчетчик последовательности (0,1,2,3)
tur_next = 2 #Переход к следующей последовательности: (0,1) => (2,3)

# Для заполнения списка элементов необходимо использовать функцию input()
value_mas = int(input('Введите длину: '))
for i in range(value_mas):
    mas.append(input('Введите элемент: '))

print(mas)

# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
if len(mas) % 2 == 0:
    while len(mas1) < len(mas):
        mas1.append(mas[k])
        k = k - 1
        tur = tur + 1
        if tur == tur_next:
            k = k + 4
            tur_next = tur_next + 2
else:
    # При нечетном количестве элементов последний сохранить на своем месте.
    while len(mas1) < len(mas)-1:
        mas1.append(mas[k])
        k = k - 1
        tur = tur + 1
        if tur == tur_next:
            k = k + 4
            tur_next = tur_next + 2
    mas1.append(len(mas))

print(mas1)
