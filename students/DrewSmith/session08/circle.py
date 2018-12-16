#!/usr/bin/env python
"""
Class that represents a circle
"""
from math import pi
import functools

@functools.total_ordering
class Circle():

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    def __init__(self, radius):
        if radius is None:
            raise TypeError("Radius cannot be none")
        self.radius = radius
    

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2
    
    @property
    def area(self):
        return pi * (self.radius ** 2)


    def __str__(self):
        return f"{self.__class__.__name__} with a radius: {self.radius:.6f}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.radius})"

    def __add__(self, other):
        val = other if not isinstance(other, Circle) else other.radius
        return Circle(self.radius + val)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        val = other if not isinstance(other, Circle) else other.radius
        self.radius += val
        return self

    def __sub__(self, other):
        val = other if not isinstance(other, Circle) else other.radius
        return Circle(self.radius - val)

    def __rsub__(self, other):
        val = other if not isinstance(other, Circle) else other.radius
        return Circle(val - self.radius)

    def __isub__(self, other):
        val = other if not isinstance(other, Circle) else other.radius
        self.radius -= val
        return self

    def __mul__(self, other):
        val = other if not isinstance(other, Circle) else other.radius
        return Circle(self.radius * val)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        val = other if not isinstance(other, Circle) else other.radius
        self.radius *= val
        return self

    def __truediv__(self, other):
        val = other if not isinstance(other, Circle) else other.radius
        return Circle(self.radius * val)

    def __rtruediv__(self, other):
        val = other if not isinstance(other, Circle) else other.radius
        return Circle(val / self.radius)

    def __itruediv__(self, other):
        val = other if not isinstance(other, Circle) else other.radius
        self.radius /= val
        return self

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius


class Sphere(Circle):
    """
    Represents a Sphere
    """

    @property
    def area(self):
        return 4 * pi * (self.radius ** 2)

    @property
    def volume(self):
        return (4 / 3) * pi * (self.radius ** 3)