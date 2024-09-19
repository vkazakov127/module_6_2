# -*- coding: utf-8 -*-
# module_6_2.py

class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner: str, __model: str, __engine_power: int, __color: str):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:  # Если цвет в списке допустимых цветов
            old_color = self.__color   # Старый цвет
            self.__color = new_color.lower()  # В нижнем регистре символов
            print(f'Цвет был изменён. Старый: {old_color}. Новый: {self.__color}')
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):  # Наследует от класса "Vehicle"
    __PASSENGERS_LIMIT = 5

    def print_info(self):
        super().print_info()   # Наследуем метод из класса "Vehicle"
        print(f'Passenger limit: {self.__PASSENGERS_LIMIT}')


# Объекты классов
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')
# vehicle1 = Vehicle('Fedos', 'Toyota Mark II', 250, 'blue')
# Изначальные свойства
print('------ Before:')
vehicle1.print_info()
# Меняем свойства (в т.ч. вызывая методы)
print('------ Change attributes')
vehicle1.set_color('ORANGE')
vehicle1.set_color('black')
vehicle1.set_color('WHITE')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
print('------ After:')
vehicle1.print_info()
print('---------------- The End ----------------')
