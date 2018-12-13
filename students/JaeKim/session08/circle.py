from math import pi

class Circle:
    def __init__ (self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return pi * self.radius**2

    def __str__(self):
        return f'Circle with radius: {self.radius:.6f}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.radius})'

    def __add__(self, other):
        return f'{self.__class__.__name__}({self.radius + other.radius})'

    def __mul__(self, other):
        return f'{self.__class__.__name__}({self.radius * other.radius})'

    def __gt__(self, other):
        return {self.radius > other.radius}

    def __eq__(self, other):
        return {self.radius == other.radius}


class Sphere(Circle):
    def __str__(self):
        return f'Sphere with radius: {self.radius:.6f}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.radius})'

    @property
    def volume(self):
        radius = self.radius
        volume = 4.0 / 3.0 * pi * radius ** 3

        return volume

    @property
    def area(self):
        return 4 * pi * self.radius * self.radius

