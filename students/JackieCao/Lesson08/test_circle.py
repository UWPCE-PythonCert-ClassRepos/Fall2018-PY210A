"""
for testing
"""
import pytest
from circle import *

def test_radius():
    c = Circle(4)
    assert c.radius == 4

def test_diameter():
    c = Circle(4)
    assert c.diameter == 8
    c.diameter = 2
    assert c.diameter == 2
    assert c.radius == 1

def test_area():
    c = Circle(2)
    assert round(c.area,5) == 12.56637

def test_alternative_const():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4

def test_str():
    c = Circle(4)
    print(c)

def test_repr():
    c = Circle(4)
    assert repr(c) == "Circle(4)"
    d = eval(repr(c))
    print(d)

def test_compare():
    c1 = Circle(2)
    c2 = Circle(4)
    assert (c1 < c2) is True
    assert (c1 == c2) is False
    assert (c1 > c2) is False

def test_optional_feature():
    a_circle = Circle(2)
    another_circle = Circle(5)
    a_circle * 3 == 3 * a_circle
    a_circle += another_circle
    a_circle *= 2

def test_sphere_repr():
    c = Sphere(4)
    assert repr(c) == "Sphere(4)"

def test_sphere_volume():
    c = Sphere(5)
    assert round(c.volume, 1) == 523.6

def test_sphere_area():
    c = Sphere(5)
    assert round(c.area, 3) == 314.159
