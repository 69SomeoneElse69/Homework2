# Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]


continue_enter = 'Y'
i = 0
my_list = []

while continue_enter == "Y":
    i = i + 1
    name = input('Введите название: ')
    cost = input('Введите цену: ')
    count = input('Количество: ')
    tipe = input('Ед. измерения: ')
    continue_enter = str(input('Перейти к следующей строке? \nY - Да \nN - Нет\n: ')).upper()
    if continue_enter == "Y":
        my_direct = {'Название': name, 'Цена': cost, 'ед.': tipe}
        my_cortej = (i, my_direct)
        my_list.append(my_cortej)
        print('\n'.join(map(str, my_list)))
    else:
        my_direct = {'Название': name, 'Цена': cost, 'ед.': tipe}
        my_cortej = (i, my_direct)
        my_list.append(my_cortej)
        print('\n'.join(map(str, my_list)))
        break

# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

analitic_name = []
analitic_cost = []
analitic_tipe = []
analitic_dict = {}

for i in range(len(my_list)):
    unrar_name = my_list[i]
    unrar_name = unrar_name[1]
    unrar_name = unrar_name.get('Название')
    analitic_name.append(unrar_name)

    unrar_cost = my_list[i]
    unrar_cost = unrar_cost[1]
    unrar_cost = unrar_cost.get('Цена')
    analitic_cost.append(unrar_cost)

    unrar_tipe = my_list[i]
    unrar_tipe = unrar_tipe[1]
    unrar_tipe = unrar_tipe.get('ед.')
    analitic_tipe.append(unrar_tipe)

analitic_dict['Название'] = analitic_name
analitic_dict['Цена'] = analitic_cost
analitic_dict['ед.'] = analitic_tipe

import pprint
pprint.pprint(analitic_dict)
