#!/usr/bin/env python
"""
Tests for Cirlce
"""
from circle import Circle
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

def test_circle_string():
    c = Circle(15)
    assert str(c) == "Circle with a radius: 15.000000"

def test_circle_repr():
    c = Circle(15)
    assert repr(c) == "Circle(15)"