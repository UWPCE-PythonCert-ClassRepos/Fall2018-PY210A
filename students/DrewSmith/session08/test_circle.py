#!/usr/bin/env python
"""
Tests for Cirlce
"""
from circle import Circle
from circle import Sphere
import math
import pytest

def test_circle_radius():
    c = Circle(5)
    assert c.radius == 5

def test_circle_invalid_radius():
    with pytest.raises(TypeError):
        c = Circle(None)


def test_circle_diameter():
    c = Circle(5)
    assert c.diameter == 10

def test_circle_diameter_change():
    c = Circle(5)
    assert c.diameter == 10
    c.diameter = 50
    assert c.diameter == 50
    assert c.radius == 25

def test_circle_area():
    c = Circle(10)
    assert round(c.area, 2) == 314.16

def test_circle_from_diameter():
    c = Circle.from_diameter(10)
    assert c.radius == 5

def test_circle_string():
    c = Circle(15)
    assert str(c) == "Circle with a radius: 15.000000"

def test_circle_repr():
    c = Circle(15)
    assert repr(c) == "Circle(15)"

def test_circle_sum():
    c1 = Circle(10)
    c2 = Circle(15)
    c3 = c1 + c2
    assert c3.radius == 25
    c3 = c2 + 3
    assert c3.radius == 18
    assert (5 + c1).radius == 15
    c1 += 200
    assert c1.radius == 210

def test_circle_difference():
    c1 = Circle(100)
    c2 = Circle(15)
    c3 = c1 - c2
    assert c3.radius == 85
    c3 = c2 - 3
    assert c3.radius == 12
    assert (175 - c1).radius == 75
    c1 -= 50
    assert c1.radius == 50


def test_circle_product():
    c1 = Circle(5)
    c2 = Circle(10)
    c3 = c1 * c2
    assert c3.radius == 50
    c3 = c2 * 3
    assert c3.radius == 30
    assert (5 * c1).radius == 25

def test_circle_compare_eq():
    c1 = Circle(5)
    c2 = Circle(5)
    assert c1 == c2
    c3 = Circle(6)
    assert c1 != c3

def test_circle_compare_gt():
    c1 = Circle(5)
    c2 = Circle(4)
    assert c1 > c2
    c3 = Circle(6)
    assert not (c1 > c3) 
    assert not (c1 > Circle(5))

def test_circle_compare_lt():
    c1 = Circle(4)
    c2 = Circle(5)
    assert c1 < c2
    c3 = Circle(3)
    assert not (c1 < c3)
    assert not (c1 < Circle(4))

def test_circle_sort():
    circles = [Circle(10), Circle(5), Circle(30), Circle(25), Circle(15)]
    circles.sort()
    print(circles)
    assert circles == [Circle(5), Circle(10), Circle(15), Circle(25), Circle(30)]

def test_circle_reflected():
    assert Circle(10) * 3 == 3 * Circle(10)

def test_circle_increment():
    c = Circle(10)
    c += Circle(15)
    assert c.radius == 25

# Sphere
def test_sphere_string():
    c = Sphere(15)
    assert str(c) == "Sphere with a radius: 15.000000"

def test_sphere_repr():
    c = Sphere(15)
    assert repr(c) == "Sphere(15)"

def test_sphere_diameter():
    c = Sphere(5)
    assert c.diameter == 10

def test_sphere_diameter_change():
    c = Sphere(5)
    assert c.diameter == 10
    c.diameter = 50
    assert c.diameter == 50
    assert c.radius == 25

def test_sphere_area():
    c = Sphere(2)
    assert round(c.area, 2) == 50.27

# 4/3 pi r ** 3
def test_sphere_volume():
    c = Sphere(4)
    assert round(c.volume, 2) == 268.08