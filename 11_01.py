'''
Створіть клас Point, який відповідатиме за відображення геометричної точки на площині.

Реалізуйте через конструктор __init__ ініціалізацію двох атрибутів: координати x та координати y.

Приклад:

point = Point(5, 10)

print(point.x)  # 5
print(point.y)  # 10
'''


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(10, 20)
print(p.x)
print(p.y)
        