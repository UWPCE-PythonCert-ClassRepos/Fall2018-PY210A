#!/usr/bin/env python3
"""
test code for html_render.py

This is just a start -- you will need more tests!
"""
import pytest
import numpy as np
from math import pi
from circle import Circle
from circle import Sphere

#Step 1
def test_init():
    Circle(4)

def test_radius():
    c = Circle(25)
    assert c.radius == 25

#Step 2
def test_diameter():
    c = Circle(5)
    assert c.diameter == 10

#Step 3
def test_set_radius():
    c = Circle(8)
    c.diameter = 14

    assert c.radius == 7
    assert c.diameter == 14

#Step 4
def test_area():
    c = Circle(2)
    assert c.area == pi * 4

#Step 5 
def test_alter():
    c = Circle.from_diameter(8)
    assert c.diameter == 8 
    assert c.radius == 4

#Step 6 Add __str__ and __repr__ methods to your Circle class.
def test_string():
    c = Circle(10)
    assert str(c) == 'Circle with radius: 10.00000'
    assert repr(c) == 'Circle(10)'
    d = eval(repr(c))  
    assert d == Circle(10)

#Step 7 
def add_circle():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = c1 + c2
    assert c3 == Circle(6)
    c4 = c2 * 3
    assert c4 == Circle(12)

#Step 8 - ability to compare two circles:
def test_compare_circle():
    c1 = Circle(1)
    c2 = Circle(2)
    c3 = Circle(2)
    c4 = Circle(4)
    c5 = Circle(5)      
    assert (c1 > c2) == False
    assert (c1 < c2) == True
    assert (c1 == c2) == False
    assert (c2 == c3) == True
    circles = [c1, c2, c3, c4, c5]
    print (circles)
    circles.sort()
    assert circles == [Circle(1), Circle(2), Circle(2), Circle(4), Circle(5)]


#Step 8 - Optional Feature
# def test_mult__circle():
#     a_circle = Circle.__mul__(1, 3)
#     assert a_circle == 3
# See if you can make “reflected” numerics do the right thing:
# a_circle * 3 == 3 * a_circle
# What else makes sense: division? others?
# Add the “augmented assignment” operators, where they make sense:
# a_circle += another_circle
# a_circle *= 2


# Step 9: Subclassing!
# You’ve got a circle already – what if you needed a Sphere? They have a fair bit in common – 
# both defined by a radius, same relationship of radius to diameter, etc.
# Create a Sphere Class that subclasses Circle.
# Override the __str__ and __repr__ methods to be appropriate for Spheres.
# Test str and repr method from Sphere
def test_Sphere():
    s = Sphere(10)
    assert str(s) == 'Sphere with radius: 10.00000'
    assert repr(s) == 'Sphere(10)'
    d = eval(repr(s))  
    assert d == Sphere(10)

def test_Sphere_area():
    a_s = Sphere(10) #area Sphere
    area_sphere = a_s.area
    assert round (float(area_sphere), 2) == 1256.64 

def test_Sphere_clsmethod():
    s = Sphere.from_diameter(8)
    assert s.diameter == 8 
    assert s.radius == 4

def test_Volume():
    s = Sphere(5)
    v = s.volume
    assert round(float(v), 1) == 523.6

# Override the area property so that it either computes the surface area of a sphere (what’s the formula for that???), or have it raise an exception: maybe NotImplementedError.
# Make sure to write some tests – maybe ahead of time! – that confirm that all this works. And the other things like addition, and sorting…
