# Создать список и заполнить его элементами различных типов данных.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
a = ['a', 2, 2.02, False, None, 0b10001]

# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
for chek in a:
    print(chek, "= ", type(chek))


