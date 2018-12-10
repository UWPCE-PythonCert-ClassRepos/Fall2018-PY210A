from circle import Circle, Sphere
from math import pi
import pytest


def test_init():
    c = Circle(4)


def test_radius():
    c = Circle(25)

    assert c.radius == 25


def test_diameter():
    c = Circle(25)

    assert c.diameter == 50


def test_set_radius():
    c = Circle(8)
    c.diameter = 14

    assert c.radius == 7
    assert c.diameter == 14


def test_area():
    c = Circle(2)

    assert c.area == pi * 4


def test_str():
    c = Circle(2)

    assert str(c) == "Circle with radius: 2.000000"


def test_repr_():
    c = Circle(2)

    assert repr(c) == 'Circle(2)'

def test_add_():
    c = Circle(2)
    d = Circle(2)

    assert (c + d) == 'Circle(4)'


def test_mul_():
    c = Circle(2)
    d = Circle(2)

    assert (c + d) == 'Circle(4)'


def test_gt_():
    c = Circle(2)
    d = Circle(4)

    assert d > c


def test_eq_():
    c = Circle(2)
    d = Circle(2)

    assert c == d


def test_sorted():
    sorted_circles = [Circle(5), Circle(2), Circle(10)]
    sorted_circles.sort()

    assert sorted_circles[0] == Circle(2)
    assert sorted_circles[1] == Circle(5)
    assert sorted_circles[2] == Circle(10)


def test_sphere_init():
    s = Sphere(4)


def test_sphere_volume():
    s = Sphere(6)

    assert s.volume == 904.7786842338603


def test_sphere_area():
    s = Sphere(2)
    s2 = Sphere(3)

    assert s.area == 50.26548245743669
    assert s2.area == 113.09733552923255


def test_sphere_str():
    c = Sphere(2)

    assert str(c) == "Sphere with radius: 2.000000"


def test_sphere_repr_():
    c = Sphere(2)

    assert repr(c) == 'Sphere(2)'