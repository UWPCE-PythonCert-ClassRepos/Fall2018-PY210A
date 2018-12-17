#!/usr/bin/env python3
import math
'Create a circle using classes'

class Circle:
    def __init__(self, radius):
        self.radius = radius
    _diameter = None
    @property
    def diameter(self):
        self._diameter = self.radius * 2
        return self._diameter
    @diameter.setter
    def diameter(self, diameter):
        self._diameter = diameter
        self.radius = int(self._diameter / 2)
        return self._diameter
    _area = None
    @property
    def area(self):
        self._area = math.pi * (self.radius**2)
        return self._area
    @classmethod
    def from_diameter(cls, diameter_value):
        'Create circle using diameter'
        self = cls(int(diameter_value/2))
        return self
    def __str__(self):
        return f'Circle with radius: {self.radius}'
    def __repr__(self):
        return f'Circle({self.radius})'
    def __add__(self, other):
        return Circle(self.radius + other.radius)
    def __mul__(self, other):
        return Circle(self.radius * other.radius)
    def __lt__(self, other):
        return self.radius < other.radius
    def __gt__(self, other):
        return self.radius > other.radius
    def __eq__(self, other):
        return self.radius == other.radius