"""1 вариант. Сдача дома"""
# class House():
#     def __init__(self, street, number):
#         self.street = street
#         self.number = number
#
#     def Congradulations(self):
#         return f'Поздравляем!'
#     def build(self):
#         return ('Дом на улице ' + self.street + ' под номером ' + str(self.number) + ' построен!')
#
# house1 = House('Новгородская,', 6)
# house2 = House('О. Кошевого,', 13)
#
# print(house1.street, house1.number)
# print(house1.Congradulations())
# print(house1.build())
# print('-'*40)
#
# print(house2.street, house2.number)
# print(house2.Congradulations())
# print(house2.build())

"""Автомобили"""
class Car:
    def __init__(self, model, color, __age):
        self.model = model
        self.color = color
        self.__age = age = 15

    def set_age(self, age):
        self.__age = age
        return 'Возраст автомобиля'
    def get_age(self):
        return self.__age
    def drive(self):
       return 'Автомобиль:'

class Driver(Car):
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


driver1 = Driver('Max', 'Logisfor', 10)
driver2 = Driver('Kris', 'Gordeeva', 3)

car1 = Car('Volvo XC40 ', 'Crystal White', 15)
car2 = Car('Mini Cooper ', 'White', 4)

print(f'Владелец:')
print(driver1.name, driver1.surname)
print(f'Стаж вождения: ', driver1.age)
print(driver1.drive())
print(car1.model, car1.color)
print(car1.set_age(15), car1.get_age())
print('-'*35)


