'''
У класу Point через конструктор __init__ оголошено два атрибути: координати x та y. 
Приховати доступ до них з допомогою подвійного підкреслення: __x та __y

Реалізуйте для класу Point механізми setter та getter до атрибутів __x та __y за допомогою декораторів property та setter.

Приклад:

point = Point(5, 10)

print(point.x)  # 5
print(point.y)  # 10
'''
class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.x = x
        self.y = y

    @property
    def value(self):
        return self.__x, self.__y

    @value.setter
    def value(self, new_x, new_y):
        self.__x = new_x
        self.__y = new_y


point = Point(5, 10)

print(point._Point__x)  # 5
print(point._Point__y)  # 10
print(point.x)  # 5
print(point.y) 