import pytest
from circle import circle
from circle import sphere
import math


def test_Circle():
    c = circle(10)
    assert c.radius == 10


def test_diameter():
    c = circle(10)
    assert c.diameter == 20


def test_set_diameter():
    c = circle(10)
    assert c.diameter == 20
    c.diameter = 10
    assert c.diameter == 10


def test_change_radius_diameter():
    c = circle(10)
    c.diameter = 100
    assert c.radius == 50


def test_set_area():
    c = circle(10)
    assert math.isclose(c.area, (math.pi * 10**2), rel_tol=.01)
    c.area = 5
    assert math.isclose(c.area, 5, rel_tol=.01)


def test_change_values_area():
    c = circle(10)
    c.area = 5
    assert math.isclose(c.radius, 1.26, rel_tol=.01)
    assert math.isclose(c.diameter, c.radius * 2, rel_tol=.01)


def test_from_diameter():
    c = circle.from_diameter(10)
    assert c.diameter == 10
    assert c.radius == 5


def test_str():
    c = circle(10)
    assert str(c) == 'Circle with radius: 10.000000'
    assert repr(c) == "Circle(10)"


def test_math():
    c1 = circle(10)
    c2 = circle(10)
    assert c1 + c2 == 'Circle(20)'
    assert c1 * 2 == 'Circle(20)'
    assert 2 * c1 == 'Circle(20)'


def test_relationships():
    c1 = circle(10)
    c2 = circle(20)
    assert (c1 > c2) is False
    assert c1 < c2
    assert (c1 == c2) is False
    c2 = circle(25)
    assert c1 < c2
    c2 = circle(10)
    assert c1 == c2


def test_sort():
    circle_list = [
        circle(10),
        circle(1),
        circle(4),
        circle(5),
        circle(2),
        circle(7),
        circle(3),
        circle(6),
        circle(9),
        circle(8)
    ]
    circle_list.sort()
    assert circle_list == [
        circle(1),
        circle(2),
        circle(3),
        circle(4),
        circle(5),
        circle(6),
        circle(7),
        circle(8),
        circle(9),
        circle(10)
    ]


def test_sphere():
    s1 = sphere(10)
    assert str(s1) == 'Sphere with radius: 10.000000'
    assert repr(s1) == 'Sphere(10)'
    assert math.isclose(s1.volume, 4188.79, rel_tol=.01)
    assert math.isclose(s1.area, 1256.64, rel_tol=.01)
    s1.volume = 10
    assert math.isclose(s1.volume, 10, rel_tol=.01)
    assert math.isclose(s1.radius, 1.34, rel_tol=.01)
    s2 = sphere.from_diameter(20)
    assert s2.radius == 10
