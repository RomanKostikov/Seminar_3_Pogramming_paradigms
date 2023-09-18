# ### task002:
# ● Контекст
# Теперь, когда у вас есть абстрактный класс Shape, ваша следующая задача - получить класс Circle.
# ● Задача
# Реализовать дочерний от Shape класс Circle, включая следующие работающие методы:
# ○ конструктор класса __init__ - метод инициализации класса Circle.
# ○ get_area - метод для расчета площади круга
# ○ get_perimeter - метод для расчета периметра окружности

from math import pi


from task001 import Shape


# class Shape:
#     def __init__(self):
#         raise TypeError("Creating instance of abstract class")
#
#     def get_area(self):
#         raise TypeError("Calling abstract method")
#
#     def get_perimeter(self):
#         raise TypeError("Calling abstract method")


class Circle(Shape):
    def __int__(self, r):
        self.r = int(r)

    def get_area(self):
        return pi * self.r ** 2

    def get_perimeter(self):
        return 2 * pi * self.r
#
#
# class Square(Shape):
#     def __int__(self, r):
#         self.r = int(r)
#
#     def get_area(self):
#         return self.r * self.r
#
#     def get_perimeter(self):
#         return 4 * self.r
#
#
# def get_area(obj: Shape):
#     return obj.get_area()
#
#
# circul1 = Circle(3)
# circul2 = Square(3)
# print(get_area(circul1))
# print(get_area(circul2))
# print('Площадь: ', circle_1.get_area())
# print('Площадь: ', circle_1.get_perimeter())
