#!/usr/bin/env python

"""Circle HW

"""
from math import pi

class Circle:
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
        return pi * self.radius ** 2

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)


    def __str__(self):
        return "Circle with radius {:.6f}".format(self.radius)


    def __repr__(self):
        return "Circle with radius {:.6f}".format(self.radius)


    def __add__(self, other):
        new = Circle(self.radius + other.radius)
        return str(new)


    def __mul__(self, other):
        new = Circle(self.radius * other.radius)
        return str(new)
