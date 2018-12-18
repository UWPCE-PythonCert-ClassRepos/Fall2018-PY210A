#!/usr/bin/env python3

"""
Class that represents a circle
"""
from math import pi
import functools


@functools.total_ordering
class Circle(object):

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    def __init__(self, radius):
        self.radius = float(radius)

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, val):
        self.radius = val/2

    @property
    def area(self):
        return pi * (self.radius ** 2)

    def __repr__(self):
        return f'Circle({self.radius!r}'

    def __str__(self):
        return f'Circle with raidus: {self.radius:.6f}'

    @staticmethod
    def sort_key(a_circle):
        return a_circle.radius

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __iadd__(self, other):
        self.radius += other.radius
        return self

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __rmul__(self, other):
        return Circle(self.radius * other)

    def __imul__(self, other):
        self.radius *= other
        return self

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __notequal__(self, other):
        return self.radius != other.radius


class Sphere(Circle):

    def volume(self):
        return (4 / 3) * pi * (self.radius ** 3)

    @property
    def area(self):
        return 4 * pi * (self.radius ** 2)
