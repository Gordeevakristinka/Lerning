# 1. Lists

# lst = [10, 'Hello', None, True, 25, 26.5]
# print(lst[0])
# print(lst[-6])

#*** Узнаем сколько элементов
# print(len(lst))

#*** Поставим текст в список
# text = 'Bye'
# lst.append(text)
# print(lst)
# print(id(lst))
# print(id(lst))

# *** Переназначить
# lst[-2] = 100
# print(lst)
# print(id(lst))

# *** Развернем список Reverse
# lst.reverse()
# print(lst)

# *** Найдем min всех чисел
# **** i воспринимается как элемент, т.е. 10 или Hello
# **** если есть последовательность, то можно применить цикл
# **** for i in lst (для элемента в списке)

# lst_2 = []
# for i in lst:
#     if isinstance(i, int):
#         lst_2.append(i)
# print(lst_2)
# print(sum(lst_2))
# print(min(lst_2))
# print(max(lst_2))

# *** Генерация списков
# *** Разные варианты решения 2мя разными методами

# lst = [1, 2, 3, 4, 5, 6, 7]
# lst2 = []
# for number in lst:
#     if number % 2 == 0:
#         lst2.append(number*number)
# print(lst2)

# *** Метод sort
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 11]
# lst.reverse()
# print(lst)
# print(lst.sort())
# lst.sort()
# print(lst)

# lst = ['lemon', 'cherry', 'orange', 'mango']
# lst.sort()
# print(lst)

# *** Count Посчитать конкретное значение элемента в списке

# lst5 = [10, 'Hello', None, True, 25, 26.5, True]
# print(lst5.count(True))

# *** index на каком месте в списке стоит заданное значение

# print(lst5.index(True))

# *** Посчитать сколько чисел(int) в списке
# **** т.е. элемент в списке 5 если является int
# **** True в данном случае рассматривает как 1

# lst6 = [x for x in lst5 if isinstance(x, int)]
# print(len(lst6))
# print(lst6)


# 2. TUPLES Кортежи

# *** Узнаем тип данных
# **** Если мы напишем my_tuple2 = ('lemon')
# **** print(type(my_tuple2)) то нам выведет type str
# **** только перечисление через запятую

# my_tuple = 1, 2, 3
# print(type(my_tuple))

# my_tuple2 = ('lemon', 'cherry', 'orange', 'mango')
# print(type(my_tuple2))

# *** Переведем в лист и заменили элемент нулевой (лимон) на апельсин
# lst = list(my_tuple2)
# lst[0] = 'orange'
# my_tuple2 = tuple(lst)
# print(my_tuple2)

# ***
# def sum_it(*args):
#     return sum(args)
#
# print(sum_it(2, 5, 10, 15, 13))
# print(sum_it(2, 5, 6, 11, 15, 16, 13, 18))


# 2. Dictionary. Словари

# my_dict = {
#     'name': 'Kristina',
#     'last name': 'Gordeeva',
#     'age': 31,
#     'dep': 'DEV'
# }
# print(my_dict)
# print(my_dict['name'])
#
# my_dict['dep'] = 'IT'
# print(my_dict)

# *** Методы работы со словарями
# my_dict = {
#     'name': 'Kristina',
#     'last name': 'Gordeeva',
#     'age': 31,
#     'dep': 'DEV'
}
# print(my_dict.values())
# print(my_dict.keys())
# print(my_dict.items())
# print(len(my_dict))

# my_dict['salary'] = 5000
# print(my_dict)
# print(my_dict.pop('salary'))
# print(my_dict.get('salary', 'Not found'))
#

# ***
# def keywords(**kwargs):
#     return (kwargs)
#
# print(keywords(name='Kris', last_name='Gordeeva'))


# 4. SETS. Множества
# **** Всегда только фигурные скобки.
# **** при распечатке удалит все дубликаты (например тут 8)

# my_set = {1, 2, 6, 8, 8, 8, 15, 22}
# print(my_set)

# my_list = [1, 2, True, 4, 5, 4, True, 15, 2]
# print(my_list)
# my_personal_list = list(set(my_list))
# print(my_personal_list)

# *** Методы работы сл множествами
# **** issubset является ли элемент подмножеством второго
# **** intersection где пересекаются заданные множества
# **** difference чем отличаются друг от друга
# **** set1.remove меняет местами положение элементов


# set1 = {1, 2, 5, 'hello', 'makiss'}
# set2 = {1, 2, 5, 'hello', 100, 'makiss'}
# set3 = {1, 4, 9}

# print(set1.issubset(set2))
# print(set2.issuperset(set1))
# print(set2.intersection(set1))
# print(set2.difference(set1))
# print(set1)
# set1.remove(5)
# set1.add(8)
# print(set1)

# lst = [5, ['a', 'b', 'c'], 5]
# print(lst[1][1]

# lst = [5, [1, 2, 'b'], 4]
# print(lst[1][1])

