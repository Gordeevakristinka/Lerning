"""4.1 example
Напишите функцию square, принимающую 1 аргумент — сторону квадрата,
и возвращающую 3 значения (с помощью кортежа):
периметр квадрата, площадь квадрата, диагональ квадрата."""

"""Мое решение"""
# def squaer(a):
#     return a * 4, a * a, ((a ** 2) / 2) ** 0,5
# print(squaer(6))
"""Рената"""
# def square(a):
#     p = 4 * a
#     s = a * a
#     d = (a ** 2) / 2
#     d = d ** 0.5
#     k = (p, s, d)
#     return k
# print(square(16))

"""4.2 example
Напишите фукнцию, которая принимает
произвольное количество именнованных аргументов построчно
в формате аргумент: значение.
Например:
name: John
last_name: Smith
age: 35
position: web developer"""

"""мое решение"""
# def person(name, last_name, age, position):
# # в скобках можно указать *kwargs
#     print(f'name:', name)
#     print(f'last_name:', last_name)
#     print(f'age:', age)
#     print(f'position:', position)
# person(name='Kristina', last_name='Gordeeva', age=31, position='QA')
"""Айгуль"""
# def person(**kwargs):
#     print(*kwargs.items(), sep='\n')
# person(name='Kris', last_name='Gordeeva', age=31, position='QA')
"""Рената"""
# def person(name, last_name, age, position):
#     return (['name:', name],['last_name:', last_name],['age:', age], ['position:', position])
#
# print('Kris', 'Gordeeva', 31, 'QA')

"""4.3 example
Используя лямбда-выражение,
из списка my_list = [20, -3, 15, 2, -1, -21]
создайте новый список, содержащий только
положительные числа"""

"""мое решение"""
# my_list = [20, -3, 15, 2, -1, -21]
# positive_list = list(filter(lambda x: x > 0, my_list))
# print(positive_list)
"""Рената"""
# number = [20, -3, 15, 2, -1, -21]
# lst_number = [x for x in number if x > 0]
# print(lst_number)

""" 4.4 example
Используя лямбда выражение,
получите результат перемножения значений в предыдущем списке"""

"""мое решение"""
# my_list = [20, -3, 15, 2, -1, -21]
# print(functools.reduce(lambda a, b: a * b, my_list))
"""Рената"""
# my_list = [20, -3, 15, 2, -1, -21]
# result = list(lambda x, y: x*y [20, -3, 15, 2, -1, -21])
# print(result)

""" 4.5 example
Напишите декоратор, который высчитывает
время работы функции, которую он принимает
в качестве параметра"""

"""мое решение"""
# import time
# def timer(func):
#     def wrapper():
#         start = time.perf_counter()
#         print(start)
#         func()
#         end = time.perf_counter()
#         print(end)
#         result = end - start
#         print(result)
#     return wrapper
#
#
# @timer
# def hello():
#     time.sleep(5)
#     print('Hello, World!')
# hello()

"""Рената"""
# def timeMometr(func):
#     from time import time
#     def wrapper(*args):
#         start_time = time()
#         value = func(*args)
#         end_time = time()
#         print(f'Время выполнения функции {end_time-start_time} сек.')
#         return value
#     return wrapper
# @timeMometr
# def delenn(a, b):
#     from time import sleep
#     sleep(5)
#     return a % b
# print(delenn(10, 3))


""" 4.6 example
Создайте файл my_calc.py
и пропишите в нем минимум 4 функции,
выполняющие базовые арифметические вычисления.
Примените эти функции в качестве методов в другом файле."""

"""мое решение"""
# from my_calc import sum
# print(sum(4, 6))
"""Рената"""
# import importFile
# print(importFile.delen(6, 2))
# print(importFile.sum(6, 2))
# print(importFile.proiz(6, 2))
# print(importFile.delenn(6, 2))


