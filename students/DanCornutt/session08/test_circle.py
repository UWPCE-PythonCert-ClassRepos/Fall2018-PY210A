from math import pi
from circle import Circle



def test_cicle():
    c = Circle(10)
    assert c.radius == 10

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
    assert c.__str__() == "Circle with radius 10.000000"
