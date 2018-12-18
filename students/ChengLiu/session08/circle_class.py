#!/usr/bin/env python3

import math


class Circle(object):
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        # print("Property: radius =", self._radius)
        return self._radius

    @radius.setter
    def radius(self, value):
        # print("Setter: setting radius to ", value)
        self._radius = value

    @property
    def diameter(self):
        # print("Getter: get the radius value", self.radius * 2)
        return self._radius * 2.0

    @diameter.setter
    def from_diameter(self, value):
        # print("Setter: setting diameter to ", value)
        self._diameter = value
        self._radius = value / 2.0

    @property
    def area(self):
        return math.pi * self._radius ** 2.0

    def __repr__(self):
        return "Radius: {:f}\nDiameter: {:f}\nArea: {:f}\n".format(self.radius, self.diameter, self.area)

    def __add__(self, other):
        return "Circle({:d})".format(self.radius + other.radius)

    def __mul__(self, factor):
        return "Circle({:d})".format(self.radius * factor)

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius


if __name__ == "__main__":
    radius = float(input("Enter a new for the radius: "))
    c = Circle(radius)
    print(c)

    c.from_diameter = float(input("Enter a new value for the diameter: "))
    print(c)
