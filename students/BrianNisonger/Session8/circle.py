import math


class circle():
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        self._radius = value / 2

    @property
    def area(self):
        return math.pi * (self._radius**2)

    @area.setter
    def area(self, value):
        self._radius = math.sqrt(value / math.pi)

    @classmethod
    def from_diameter(circle_object, value):
        return circle_object(value / 2)

    def __str__(self):
        return f'Circle with radius: {self.radius:.6f}'

    def __repr__(self):
        return f'Circle({self.radius})'

    def __add__(self, other):
        return f'Circle({self.radius+other.radius})'

    def __mul__(self, value):
        return f'Circle({self.radius*value})'

    def __rmul__(self, value):
        return f'Circle({self.radius*value})'

    def __gt__(self, other):
        return (self.radius > other.radius)

    def __lt__(self, other):
        return (self.radius < other.radius)

    def __eq__(self, other):
        return (self.radius == other.radius)


class sphere(circle):
    def __init__(self, radius):
        self._radius = radius

    def __str__(self):
        return f'Sphere with radius: {self.radius:.6f}'

    def __repr__(self):
        return f'Sphere({self.radius})'

    @property
    def volume(self):
        return (4 * math.pi * self._radius**3) / 3

    @volume.setter
    def volume(self, value):
        self._radius = (3 * (value / (4 * math.pi)))**(1. / 3)

    @property
    def area(self):
        return 4 * (math.pi * (self._radius**2))

    @area.setter
    def area(self, value):
        self._radius = (math.sqrt(value / math.pi) / 4)
