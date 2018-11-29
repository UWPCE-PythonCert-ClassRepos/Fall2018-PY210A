#!/usr/bin/env python
"""
Classes that represent circles
"""
from math import pi

class Circle():

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
        return f"Circle with a radius: {self.radius:.6f}"

    def __repr__(self):
        return f"Circle({self.radius})"