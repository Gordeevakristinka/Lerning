# print('1.' + ' Hello, World!')
#
# name = input('Hello,')
# print('2.' + ' Hello,' + name)

# a = int(input('Enter the first number: '))
# b = int(input('Enter the second number: '))
# result = a + b
# print(f'3.' + f' Результат = {result}')

# print('*********')
# print('*       *')
# print('*       *')
# print('*********')
#
# print('*********\n*       *\n*       *\n*********')
#
# print(
# """*********
# *       *
# *       *
# *********
# """)

num = int(input('Please input 4-digit number: '))
num1 = num//1000
num2 = num%1000//100
num3 = num%100//10
num4 = num%10

print(f'Тысячи - {num1}')
print(f'Сотни - {num2}')
print(f'Десятки - {num3}')
print(f'Единицы - {num4}')
