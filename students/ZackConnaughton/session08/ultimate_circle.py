

import math

class circle:

    def __init__(self, rad=0):
        self.radius = rad


    def __str__(self):
        return "Circle with radius: {:.6f}".format(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)

    def __add__(self, other):
        return circle(self.radius + other.radius)

    def __mul__(self, value):
        return circle(self.radius * value)

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return self.radius ** 2 * math.pi

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

class Sphere(circle):

    def __str__(self):
        return "Sphere with radius: {:.6f}".format(self.radius)

    def __repr__(self):
        return "Sphere({})".format(self.radius)

    @property
    def volume(self):
        return (4/3) * math.pi * (self.radius ** 3)

    @property
    def area(self):
        return 4 * super().area
