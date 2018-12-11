# Lesson 08 Assignment: Circle Class
# Create a class that represents a simple circle

from math import pi


class Circle(object):
    def __init__(self, radius):
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

    @classmethod
    def from_diameter(cls, value):
        return cls(value/2)

    def __str__(self):
        return f"{self.__class__.__name__} with radius: {self.radius}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.radius})"

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __rmul__(self, value):
        return Circle(self.radius * value)

    def __mul__(self, value):
        try:
            return Circle(self.radius * value)
        except TypeError:
            rmul(self, value)

    def __lt__(self, other):
        if self.radius < other.radius:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.radius > other.radius:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.radius == other.radius:
            return True
        else:
            return False

    def sort_key(self):
        return self.radius

    @staticmethod
    def __sort__(circle_list):
        return circle_list.sort(key=Circle.sort_key)

    def __iadd__(self, other):
        new_radius = self.radius + other.radius
        return Circle(new_radius)

    def __imult__(self, other):
        new_radius = self.radius * other
        return Circle(new_radius)


class Sphere(Circle):

    @property
    def volume(self):
        return 4 / 3 * pi * self.radius ** 3

    @property
    def area(self):
        try:
            return 4 * pi * self.radius ** 2
        except NotImplementedError:
            print("Error")
