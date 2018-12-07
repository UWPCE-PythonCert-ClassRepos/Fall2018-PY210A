#!/usr/bin/env python3
"""
A class-based system for circle .
"""
from math import pi


# This is the framework for the base class
class Circle:
    # radius = 0

    def __init__(self, radius):
        self.radius = radius
    
    @staticmethod
    def sort_key(self):
        return self.radius

    @property
    def diameter(self):
        return self.radius * 2
    
    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2
    
    @property
    def area(self):
        return pi * self.radius**2

    @classmethod #???run c
    def from_diameter(cls, val):
        cls.diameter = val
        cls.radius = val / 2
        return cls

    def __str__(self):
        return "Circle with radius: {:0.5f}".format(self.radius)
    
    def __repr__(self): #??
        return "Circle({})".format(repr(self.radius))

    def __lt__(self, other): #less than  
        return (self.radius < other.radius)
    
    def __gt__(self, other): #greater than
        print(other)
        return (self.radius > other.radius)

    def __eq__(self, other): #equal
        return (self.radius == other.radius)

    def __mul__(self, other):
        return (self.radius * other.radius)

    @staticmethod
    # def sort_key(a_circle):
    #     return a_circle.radius

class Sphere(Circle):

    def __str__(self):
        return "Sphere with radius: {:0.5f}".format(self.radius)
    
    def __repr__(self):
        return "Sphere({})".format(repr(self.radius))
    
# Create a volume property that returns the volume (hint: volume of a sphere is: 4/3 pi r^3).
    @property 
    def volume(self):
        print ((4/3) * pi * self.radius**3)
        return (4/3) * pi * self.radius**3
    @property
    def area(self):
        # try:
        return (4 * (pi * self.radius**2))
        # return (4 * Circle.area(self.radius))
        # except:
        #     raise NotImplementedError
