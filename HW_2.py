# 1 example
# Здоровье персонажа в игре. Если оно равно или меньше нуля, выведите на экран False, в противном случае True.

# health = int (input('Введите показатели: '))
# if health <= 0:
#     print('False')
# else:
#     print('True')


# 2 example
# Четное или нет?. Если да, выведите на экран текст “Четное”, а иначе - “Нечетное”

# num = int (input('Введите число: '))
# if num % 2 == 0:
#     print('Четное число')
# else:
#     print('Нечетное число')

# 3 example
# Определение високосного года

# year = int (input('Введите год: '))
# if year % 4 == 0 and year % 100 != 0:
#     print('Високосный год!')
# elif year % 400 == 0:
#     print('Високосный год!')
# else:
#     print('Не високосный(')


# 4 example
# Печать текста заданное количество раз, построчно.

# num = int(input('Введи количество повторений: '))
# text = input("Введите текст: ")
# # print(text * num)
# #
# for i in range(num):
#     print(text)

# 5 example
# программа-калькулятор, принимающая 2 числа и оператор (в формате str), про6изводит заданное арифметическое действие и печатает результат в формате: {num1} {operator) {num2) = {result}

num1 = int(input("Введите число 1: "))
num2 = int(input("Введите число 2: "))
c = input("Введите оператор: ")
if c == '+':
    print(num1 + num2)
elif c == '*':
    print(num1 * num2)
elif c == '-':
    print(num1 - num2)
elif c == '/':
    print(num1 / num2)
else:
    print('Ошибка!!!')


