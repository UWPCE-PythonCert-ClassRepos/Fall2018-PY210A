#!/usr/bin/env python3

from circle import Circle, Sphere
import math
import pytest

"""
Circle Tests
"""


def test_cir_radius():
    c = Circle(5)
    assert c.radius == 5


def test_cir_radius_invalid():
    with pytest.raises(TypeError):
        c = Circle(None)


def test_cir_diameter():
    c = Circle(5)
    assert c.diameter == 10


def test_cir_diameter_change():
    c = Circle(5)
    assert c.diameter == 10
    c.diameter = 50
    assert c.diamter == 50
    assert c.radius == 25


def test_cir_area():
    c = Circle(10)
    assert round(c.area, 2) == 314.16


def test_cir_from_diameter():
    c = Circle.from_diameter(10)
    assert c.radius == 5


def test_cir_str():
    c = Circle(15)
    assert str(c) == "Circle with radius: 15"


def test_cir_sum():
    c1 = Circle(10)
    c2 = Circle(15)
    c3 = c1 + c2
    assert c3.radius == 25


def test_cir_multiply():
    c1 = Circle(5)
    c2 = Circle(10)
    c3 = c1 * c2
    assert c3.radius == 50


def test_cir_equal():
    c1 = Circle(5)
    c2 = Circle(5)
    assert c1 == c2
    assert c1 <= c2


def test_cir_greater_than():
    c1 = Circle(5)
    c2 = Circle(2)
    assert c1 > c2
    assert c2 >= c1


def test_cir_less_than():
    c1 = Circle(2)
    c2 = Circle(5)
    assert c1 < c2
    assert c1 <= c2


def test_cir_sort():
    cir_list = [Circle(10), Circle(5), Circle(25), Circle(20), Circle(15)]
    cir_list.sort(key=Circle.sort_key)
    assert circles == [Circle(5), Circle(10), Circle(15), Circle(20), Circle(25)]
    assert cir_list[0] == Circle(5)
    assert cir_list[4] == Circle(25)
    assert cir_list[4] > cir_list[0]


"""
Spheres Test
"""


def test_sph_str():
    c = Sphere(10)
    assert str(c) == "Sphere with radius 10"


def test_sph_repr():
    c = Sphere(15)
    assert repr(c) == "Sphere(15)"


def test_sph_diameter():
    c = Sphere(5)
    assert c.diameter == 10


def test_sph_diameter_change():
    c = Sphere(10)
    assert c.diameter == 20
    c.diameter = 20
    assert c.diameter == 20
    assert c.radius == 10


def test_sph_area():
    c = Sphere(2)
    assert round(c.area, 2) == 50.27


def test_sph_vol():
    c = Sphere(4)
    assert round(c.volume, 2) == 268.08
