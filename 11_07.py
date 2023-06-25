'''
Реалізуйте для класу Vector операції додавання та віднімання векторів. 
Тобто перевизначите для нього математичні оператори __add__ та __sub__

Є два вектори: a з координатами (x1, y1) та b з координатами (x2, y2).

Тоді додавання векторів b + a - це новий вектор з координатами (x2 + x1, y2 + y1). 
Віднімання – зворотна операція, b - a - це новий вектор з координатами (x2 - x1, y2 - y1)

Приклад коду:

vector1 = Vector(Point(1, 10))
vector2 = Vector(Point(10, 10))

vector3 = vector2 + vector1
vector4 = vector2 - vector1

print(vector3)  # Vector(11,20)
print(vector4)  # Vector(9,0)
'''

class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y

    def __str__(self):
        return f"Point({self.x},{self.y})"


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        if index == 1:
            self.coordinates.y = value

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        if index == 1:
            return self.coordinates.y

    def __call__(self, value=None):
        if value:
            self.coordinates.x = self.coordinates.x * value
            self.coordinates.y = self.coordinates.y * value
        return self.coordinates.x, self.coordinates.y

    def __add__(self, vector):
        result = [0, 0]
        result[0] = self[0] + vector[0] 
        result[1] = self[1] + vector[1]
        return Vector(Point(result[0],result[1]))
        

    def __sub__(self, vector):
        result = [0, 0]
        result[0] = self[0] - vector[0] 
        result[1] = self[1] - vector[1]
        return Vector(Point(result[0],result[1]))
        
        

    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"

vector1 = Vector(Point(1, 10))
vector2 = Vector(Point(10, 10))

vector3 = vector2 + vector1
vector4 = vector2 - vector1

print(vector3)  # Vector(11,20)
print(vector4)  # Vector(9,0)