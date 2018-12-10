"""
circle hw
"""

import math
class Circle:
    def __init__(self,radius = None):
        self._radius = radius
    @property
    def radius(self):
        return self._radius
    @property
    def diameter(self):
        return self._radius*2
    @diameter.setter
    def diameter(self, value):
        self._radius = value/2
    @property
    def area(self):
        return self._radius**2 * math.pi
    @classmethod
    def from_diameter(cls, diameter):
        self = cls()
        self.diameter = diameter
        return self
    def __str__(self):
        return f"Circle with radius: {self._radius}"
    def __repr__(self):
        return f"Circle({self._radius})"
    def __add__(self, other):
        total_radius = self._radius + other._radius
        return Circle(total_radius)
    def __mul__(self, other):
        total_radius = self._radius * other
        return Circle(total_radius)
    def __rmul__(self, other):
        total_radius = other * self._radius
        return Circle(total_radius)
    def __gt__(self, other):
        return self._radius > other._radius
    def __lt__(self, other):
        return self._radius < other._radius
    def __eq__(self, other):
        return self._radius == other._radius


class Sphere(Circle):
    def __init__(self, radius):
        super().__init__(radius)
    def __str__(self):
        return f"Sphere with radius: {self._radius}"
    def __repr__(self):
        return f"Sphere({self._radius})"
    @property
    def volume(self):
        return self._radius**3 * math.pi * 4/3
    @property
    def area(self):
        return self._radius**2 * math.pi * 4


