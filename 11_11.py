'''
Необхідно реалізувати клас RandomVectors, який зможе створювати об'єкт, 
що ітерується, і дозволяти ітеруватися по випадковим векторам.

Формат класу:

RandomVectors(max_vectors: int, max_points: int) -> Iterable(max_vectors, max_points)
де:

max_vectors — визначає максимальну кількість елементів (примірників класу Vector) 
в ітерованій послідовності
max_points — визначає максимальне значення для координат 
x та y (в діапазоні 0...max_points)
Щоб екземпляри класу RandomVectors були об'єктами, що ітеруються, 
в класі повинен бути реалізований метод __iter__, який повертає ітератор. 
Ітератор – це будь-який об'єкт, який на кожному кроці ітерації (крок ітерації – це виклик методу 
next() для цього ітератора) повертає таке значення - і так до вичерпання 
кількості ітерацій (визначається параметром max_vectors).

У нашому випадку ітератором буде клас Iterable, у якому необхідно реалізувати метод __next__. 
Він у конструкторі отримує ті ж параметри max_vectors та max_points, що і клас RandomVectors.

Метод __next__ повинен видавати кожне наступне значення зі списку self.vectors. 
Створіть у конструкторі набір випадкових векторів self.vectors завдовжки max_vectors 
за допомогою randrange. Атрибут current_index вказівник-індекс на поточний вектор зі списку vectors, 
необхідний для ітерування.

Приклад роботи класу `RandomVectors:

vectors = RandomVectors(5, 10)

for vector in vectors:
    print(vector)
Вивід має бути схожим на цей:

Vector(7,7)
Vector(0,0)
Vector(8,9)
Vector(1,9)
Vector(6,6)
Деталізуємо наше завдання:

Клас RandomVectors повинен мати метод __iter__, який має повернути об'єкт ітератора (клас Iterable)
Об'єкт ітератора (примірник класу Iterable) повинен мати метод __next__
Метод __next__ стежить за кількістю можливих кроків ітерації, вони визначаються параметром max_vectors
Якщо ми вичерпали можливі кроки, то метод __next__ генерує виняток StopIteration
В іншому випадку метод __next__ повертає вектор з випадковими координатами 
(примірник класу Vector), розмір координат вектора визначається параметром max_points.
'''

from random import randrange


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
        x = self.coordinates.x + vector.coordinates.x
        y = self.coordinates.y + vector.coordinates.y
        return Vector(Point(x, y))

    def __sub__(self, vector):
        x = self.coordinates.x - vector.coordinates.x
        y = self.coordinates.y - vector.coordinates.y
        return Vector(Point(x, y))

    def __mul__(self, vector):
        return (
                self.coordinates.x * vector.coordinates.x
                + self.coordinates.y * vector.coordinates.y
        )

    def len(self):
        return (self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5

    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"

    def __eq__(self, vector):
        return self.len() == vector.len()

    def __ne__(self, vector):
        return self.len() != vector.len()

    def __lt__(self, vector):
        return self.len() < vector.len()

    def __gt__(self, vector):
        return self.len() > vector.len()

    def __le__(self, vector):
        return self.len() <= vector.len()

    def __ge__(self, vector):
        return self.len() >= vector.len()


class Iterable:
    def __init__(self, max_vectors, max_points):
        self.current_index = 0
        self.vectors = []
        self.max_vectors = max_vectors
        self.max_points = max_points
            

    def __next__(self):
        self.current_index += 1
        if self.current_index == (self.max_vectors + 1):
            raise StopIteration
        return Vector(Point(randrange(self.max_vectors+1), randrange(self.max_vectors+1)))


class RandomVectors:
    def __init__(self, max_vectors=10, max_points=50):
        self.max_vectors = max_vectors
        self.max_points = max_points
        

    def __iter__(self):
        return Iterable(self.max_vectors, self.max_points)


vectors = RandomVectors(5, 10)

for vector in vectors:
    print(vector)

# Vector(7,7)
# Vector(0,0)
# Vector(8,9)
# Vector(1,9)
# Vector(6,6)