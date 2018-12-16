#!/usr/bin/env python
#Tim Pauley
#Python201a,  Assignment 08
#Date: Decemeber 02 2018

#Goal: The goal is to create a class that represents a simple circle.
# Instructions: A Circle can be defined by either specifying the radius 
#or the diameter, and the user can query the circle for either its radius
# or diameter. 

from math import pi
import functools


@functools.total_ordering
class Circle(object):

    def __init__(self, radius):
        self.radius = float(radius)

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2.0)

    @property
    def diameter(self):
        return self.radius * 2.0
    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2.0

    @property
    def area(self):
        return self.radius**2 * pi

    def __repr__(self):
        return "Circle({:s})".format(repr(self.radius))

    def __str__(self):
        return "Circle with radius: {:g}".format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __iadd__(self, other):
        self.radius += other.radius
        return self

    def __mul__(self, factor):
        return Circle(self.radius * factor)

    def __imul__(self, factor):
        self.radius *= factor
        return self

    def __rmul__(self, factor):
        return Circle(self.radius * factor)
