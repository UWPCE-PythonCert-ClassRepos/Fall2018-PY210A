#!/usr/bin/env python3

from math import pi
import functools

class Circle():
    def __int__(self, radius):
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
    def __str__(self):
        return f'Circle with a radius: {self.radius:6f}'
    def __repr__(self):
        return f"Circle({self.radius})"
    @classmethod
    def from_diameter(cls, diameter):
        return cls.diameter/2

    def __add__(self, other):
        return Circle(self.radius + self.other)
    def __mul__(self, factor):
        return Circle(self.radius * factor)
    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius
    def __eq__(self, other):
        return self.radius == other.radius

class Sphere(Circle):
	@property
	def area(self):
		return 4 * pi * (self.radius ** 2)
	@property
	def volume(self):
		return (4 / 3) * pi * (self.radius ** 3)

