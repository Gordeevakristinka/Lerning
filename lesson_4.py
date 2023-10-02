# 1. Функция (functions)
# *** минимальное значение
# import datetime
#
# min_item = min(20, 15, 77, 100)
# print(min_item)

# *** функция имени
# def person(age, first_name, last_name):
#     return f'Hello, my name is {first_name} {last_name}. I am {age} years old'
# print(person(31, first_name= 'Kristina', last_name= 'Gordeeva'))

# *** рисунок, принимает 3 аргумента(1 опозиц, 2,3 имен)
# def pattern(lenght, char1='', char2='*'):
#     return (char1 + char2) * lenght + char1
# print(pattern(4, '+*+', '7'))

#******************************************************************
# 2. Декораторы
# ***
# def decorator_function(func):
#     def wrapper(*args):
#         print('Wrapper function')
#         print(f'Calling function: {func.__name__}')
#         print(f'With arguments: {args}')
#         print('Wrapped function in process')
#         print(func(*args))
#         print('Exiting wrapper')
#     return wrapper
# @decorator_function
# def hello(item):
#     return f'{item} is wrapped!'
#
# hello('Candy')

# ********************************************************************
# 3. Пространство имен (Namespace)
# ***
# x = 15
# y = 25
# def sum_it(x, y):
#     print(f'locals: {locals()}')
#     return x + y
# print(f'Inside the function: {sum_it(10, 18)}')
# print(f'Outside the function: {x + y}')
# print(f'Globals: {globals()}')

# ***
# name = 'Alice'
#
# def outer_function():
#     # name = 'Albert'
#     def inner_function():
#         # name = 'Alex'
#         return name
#     return inner_function
#
# closure = outer_function()
# result = closure()
#
# print(result)

# ***********************************************************
# 4. Область видимости (SCOPE)
# *** Лямбда
# result = lambda n: n*n
# print(result(5))

# *** Пример из прошлого ДЗ
# list_1 = ['Hi', "ananas", 2, None, 75, 36, 'groove', 100]
# def filter_and_sum(lst):
#     new_lst = []
#     for x in lst:
#         if isinstance(x, int):
#             new_lst.append(x)
#     print(new_lst)
#     return sum(new_lst)
#
# print(filter_and_sum(list_1))

# *** тоже само решение, но с лямбдой:
# print(sum(filter(lambda x: isinstance(x, int), list_1)))
# *** тоже решение как отфильтровать только числа из заданного списка:
# print(list(filter(lambda x: isinstance(x, int), list_1)))
# *** отфильтровать только слова
# print(list(filter(lambda x: isinstance(x, str), list_1)))
# ***
# filtered = list(filter(lambda x: isinstance(x, str) and 'a' in x, list_1))
# print(filtered)
# print(list(filter(lambda i: 'a' in i, filtered)))

# *** функция reduce
# перемножение всех чисел
# 1*5=5, 5*5=25, 25*8=...

# from functools import reduce
# result = reduce(lambda x, y: x*y, [1, 5, 8, 11, 13])
# print(result)

# *** функция map
# для каждого элемента в списке совершаем действие

# result = list(map(lambda x: x**2, [1, 5, 8, 11, 13]))
# print(result)

# ****************************************************
# 5. модули

# from math import prod
# import math
# from math import *

# from my_module import sum_it
# result = sum_it(7, 8)
# print(result)

# l = [1, 2, 5, 7]
# print(math.prod(l))
# print(prod(l))

# *******************************************
# 6. TEST
# from my_module import *
# def tests():
#     assert sum_it(5, 8) == 13, f'Wrong number, actual result is {sum_it(5, 8)}'
#     assert sum_it(10, 8) == 23, f'Wrong number, actual result is {sum_it(10, 8)}'
# tests()

# ***************************************************
# *** Метод datetime

# *** текущая дата
# birth_year = 1992
# current_date = datetime.date.today()
# print(current_date)
#
# # *** сколько лет на данный момент
# current_age = current_date.year - birth_year
# print(current_age)




