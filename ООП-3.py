import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self):
        return f"Point(x={self.x}, y={self.y})"

class Circle(Point):
    radius = 0

    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        radius_diff = self.radius - other.radius

        if radius_diff < 0:
            return Point(x, y)

        return Circle(radius_diff, x, y)

    def __str__(self):
        return super().__str__()[:-1] + f', radius={self.radius})'

circle_1 = Circle(6, 2, 4)
circle_2 = Circle(3)
print('circle_1: ', circle_1)
print('circle_2: ', circle_2)
circle_3 = circle_1 - circle_2
print('circle_3: ', circle_3)
print(str(type(circle_3)))
circle_4 = circle_3 - circle_2
print('circle_4: ', circle_4)
print(str(type(circle_4)))