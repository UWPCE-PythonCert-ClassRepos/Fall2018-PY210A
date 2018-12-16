#!/usr/bin/env python3

""" Session 8 """

from math import pi
import functools

@functools.total_ordering
class Circle(object):


    def __init__(self, radius):
        self.pi = pi
        self.radius = float(radius)

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2.0)

    @property
    def diameter(self):
        return self.radius * 2
    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2


    @property
    def area(self):
        return self.pi * self.radius**2

    # def __imul__(self, factor):
    #     """see __iadd__"""
    #     self.radius *= factor
    #     return self

    def __str__(self):
        return f'Circle with radius: {self.radius:.6f}'

    def __repr__(self):
        return "Circle({})".format(self.radius)

    def __add__(self, other):
        return (Circle(self.radius + other.radius))

    def __mul__(self, value):
        return Circle(self.radius * value)

    # def __eq__(self, other):
    #     return self.radius == other.radius
    # def __ne__(self, other):
    #     return self.radius != other.radius
    # def __gt__(self, other):
    #     return self.radius > other.radius
    # def __ge__(self, other):
    #     return self.radius >= other.radius
    # def __lt__(self, other):
    #     return self.radius < other.radius
    # def __le__(self, other):
    #     return self.radius <= other.radius

    # Or you can put the @total_ordering decorator on the class definition
    # and do only these:
    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

class Sphere(Circle):
    """
    Doing the Spere Creation Dance
    """
    def volume(self):
        return 4 / 3 * pi * self.radius ** 3

    @property
    def area(self):
        return 4 * pi * self.radius ** 2

    def __repr__(self):
        return "Sphere({:g})".format(self.radius)

    def __str__(self):
        return "Sphere with radius: {:g}".format(self.radius)

