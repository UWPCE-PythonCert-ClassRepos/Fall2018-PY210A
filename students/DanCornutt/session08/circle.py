#!/usr/bin/env python

"""Circle HW, Session 07

"""
from math import pi

class Circle:
    """class for Circles with attributes and methods used by all."""
    name = "Circle"
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        """Returns diameter of circle."""
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        """Sets diameter of constructed circle.
        param1: diameter of wanted circle"""
        self.radius = value / 2

    @property
    def area(self):
        """Computes area of circle. Returns area"""
        return pi * self.radius ** 2

    @classmethod
    def from_diameter(cls, diameter):
        """Alternate constructer for from_diameter
        param1 : diameter of wanted circle"""
        return cls(diameter / 2)


    def __str__(self):
        return "{} with radius {:.6f}".format(self.name, self.radius)


    def __repr__(self):
        return "{} with radius {:.6f}".format(self.name, self.radius)


    def __add__(self, other):
        new = Circle(self.radius + other.radius)
        return str(new)


    def __mul__(self, other):
        try:
            new = Circle(self.radius * other.radius)
        except AttributeError:
            new = Circle(self.radius * other)
        return new


    def __lt__(self, other):
        return self.radius < other.radius


    def __le__(self, other):
        return self.radius <= other.radius


    def __eq__(self, other):
        return self.radius == other.radius


    def __qe__(self, other):
        return self.radius >= other.radius


    def __qt__(self, other):
        return self.radius > other.radius


    def __ne__(self, other):
        return self.radius != other.radius


class Sphere(Circle):
    """Class for Spheres, subclass of Circle. Attributes and methods for
    dealing with spheres."""
    name = "Sphere"

    @property
    def area(self):
        """Computes surface area of sphere."""
        return 4 * pi * self.radius ** 2

    @property
    def volume(self):
        """Computes volume of sphere."""
        return 4 /3 * pi * self.radius ** 3
