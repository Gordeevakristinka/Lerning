"""1. Классы. Метод __init__"""
class Person:

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.__age__ = age

    def hello(self):
        return f'Hello, my name is {self.name} {self.surname}'

    def walk(self):
        return 'I can walk'
#
person_1 = Person('Kristina', 'Gordeeva', 31)
# print(person_1.name, person_1.surname)
# print(person_1.surname)
print(f'Atributes: {person_1.__dict__}')
# print(person_1.hello())
# print(person_1.walk())
# print(Person.__dict__)
"""меняем имя"""
# person_1.name = 'Kris'
# print(f'New name is {person_1.name}')
#
# person_2 = Person('Max', 'Loginov')
# # print(person_2.name, person_2.surname)
# print(person_2.hello())
# print(person_2.walk())

"""2. Наследование"""
# class Tester(Person):
#
#     def __init__(self, name, surname, framework):
#         super().__init__(name, surname)
#         self.framework = framework
#
#     def test(self):
#         return 'I love testing'
#
# tester_1 = Tester('Max', 'Loginov', 'pytest')
# print(tester_1.hello())
# print(tester_1.name)
# print('I am',tester_1.framework)

"""3. Гит. Гитхаб"""
