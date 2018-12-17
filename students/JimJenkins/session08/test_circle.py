#!/usr/bin/env python3

from circle import Circle
from math import pi

def test_init():
    Circle(10)

def test_radius():
    c = Circle(25)

    assert c.radius == 25

def test_diameter():
    c = Circle(5)

    assert c.diameter == 10

def test_set_radius():
    c = Circle(8)
    c.diameter = 14

    assert c.radius == 7
    assert c.diameter == 14

def test_area():
    c = Circle(2)

    assert c.area == pi * 4

def test_str():
    c = Circle(10)

    assert str(c) == 'Circle with radius: 10.'