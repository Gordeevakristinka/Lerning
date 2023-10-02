""" 3.1 example
Дан список my_list = ['a', 'b', [1, 2, 3], 'd'].
Распечатайте значения 1, 2, 3"""

# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(my_list[2])
# # или
# print(my_list[2][0])
# print(my_list[2][1])
# print(my_list[2][2])
# # или
# new_list = my_list[2]
# print(*new_list, sep='\n')

""" 3.2 example
Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
- получите сумму всех чисел,
- распечатайте все строки, где есть буква 'a'"""

# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
"""1"""
# my_list_1 = [x for x in list_1 if isinstance(x, int)]
# print(my_list_1)
# print(sum(my_list_1))
# лучшее решение
# print(sum([x for x in list_1 if isinstance(x, int)]))
"""2"""
# print(*[x for x in list_1 if isinstance(x, str) and 'a' in x])

"""3.3 example
Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж"""
# list_2 = ['cat', 'dog', 'horse', 'cow']
# print(tuple(['cat', 'dog', 'horse', 'cow']))

""" 3.4 example
Напишите программу, которая определяет, какая семья больше.
1) Программа имеет два input() - например, family_1, family_2.
2) Членов семьи нужно перечислить через запятую.
Ожидаемый результат - программа выводит семью с бОльшим составом. 
Если состав одинаковый, print("Equal')"""

# fam1 = str(input('Введите членов семьи 1: '))
# fam2 = str(input('Введите членов семьи 2: '))
#
# if len(fam1) == len(fam2):
#     print('Equal')
# elif len(fam1) > len(fam2):
#     print('FAMILY 1')
# else:
#     print('FAMILY 2')
"""Айгуль"""
# fam1 = tuple(input('Введите членов семьи 1: ').split(','))
# fam2 = tuple(input('Введите членов семьи 2: ').split(','))
# if len(fam1) > len(fam2):
#     print(fam1)
# elif len(fam1) < len(fam2):
#     print(fam2)
# else:
#     print('Equal')

""" 3.5 example
Создайте словарь film c ключами:
title, director, year, budget, main_actor, slogan.
В значения можете передать информацию о вашем любимом фильме.
- распечатайте только ключи
- распечатайте только значения
- распечатайте пары ключ - значение"""

film = {
       'title': 'Oblivion',
       'director': 'Джозеф Косински',
       'year': 2013,
       'budget': 120000000,
       'main_actor': 'Том Круз',
       'slogan': 'Земля - это память, за которую стоит бороться.'
}
# for key in film.keys():
#     print(key)
# for value in film.values():
#     print(value)
# for key, value in film.items():
#     print(key, '-', value)
"""или"""
# print(*film.keys())
# print(*film.values())
# print(film)


""" 3.6 example
Найдите сумму всех значений в словаре"""
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 421}
# print(sum(my_dictionary.values()))

""" 3.7 example
Удалите повторяющиеся значения из списка:"""
# [1, 2, 3, 4, 5, 3, 2, 1]
# my_list = [1, 2, 3, 4, 5, 3, 2, 1]
# print(set(my_list))

""" 3.8 example
Даны два множества:
set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'},
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
- найдите значения, которые встречаются в обоих множествах
- найдите значения, которые не встречаются в обоих множествах
- проверьте являются ли эти множества подмножествами друг друга"""

# set_1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set_2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# print(set_1.intersection(set_2))
# print(set_1.symmetric_difference(set_2))
# print(set_1.issubset(set_2))
# print(set_2.issubset(set_1))

