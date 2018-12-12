# Tests for Circle Class

import pytest
from math import pi
from circle_class import Circle, Sphere


# Step 1
def test_empty_circle():
    with pytest.raises(TypeError):
        Circle()


def test_new_circle():
    Circle(1)


def test_radius():
    c = Circle(2)

    assert c.radius == 2


# Step 2
def test_diameter():
    c = Circle(3)

    assert c.diameter == 6


# Step 3
def test_set_diameter():
    c = Circle(4)
    c.diameter = 5

    assert c.diameter == 5
    assert c.radius == 2.5


# Step 4
def test_area():
    c = Circle(6)

    assert c.area == pi * 36


def test_set_area():
    c = Circle(7)

    with pytest.raises(AttributeError):
        c.area = 10


# Step 5
def test_alt_constructor():
    c = Circle.from_diameter(8)

    assert c.diameter == 8
    assert c.radius == 4


# Step 6
def test_string():
    c = Circle(9)

    assert str(c) == "Circle with radius: 9"


def test_repr():
    c = Circle(10)

    assert repr(c) == "Circle(10)"


# Step 7
def test_add_circles():
    c1 = Circle(2)
    c2 = Circle(3)

    assert c1 + c2 == Circle(5)


def test_multiply_circle():
    c4 = Circle(4)

    assert c4 * 2 == Circle(8)


def test_reverse_multiply_circle():
    c1 = Circle(5)

    assert 3 * c1 == Circle(15)


# Step 8
def test_greater_than():
    c1 = Circle(1)
    c2 = Circle(2)

    assert (c1 > c2) is False


def test_less_than():
    c3 = Circle(3)
    c4 = Circle(4)

    assert (c3 < c4) is True


def test_equal_to():
    c1 = Circle(5)
    c2 = Circle(5)

    assert (c1 == c2) is True


def test_sort():
    circles = [Circle(6), Circle(1), Circle(3), Circle(5), Circle(10)]
    circles.sort()

    assert circles == [Circle(1), Circle(3), Circle(5), Circle(6), Circle(10)]


# Step 8 Optional Features
def test_reflected_mult():
    assert Circle(5) * 3 == 3 * Circle(5)


def test_plus_equals():
    c1 = Circle(4)
    c2 = Circle(5)
    c1 += c2

    assert c1 == Circle(9)


def test_mult_equals():
    c3 = Circle(3)
    c3 *= 5

    assert c3 == Circle(15)


# Step 9
def test_new_sphere():
    Sphere(4)


def test_str_sphere():
    s = Sphere(10)
    assert str(s) == "Sphere with radius: 10"


def test_repr_sphere():
    s = Sphere(5)

    assert repr(s) == "Sphere(5)"


def test_volume():
    s = Sphere(2)

    assert s.volume == 4/3 * pi * 2**3


def test_sphere_area():
    s = Sphere(3)

    assert s.area == 4 * pi * 3**2


def test_alt_constructor_sphere():
    s = Sphere.from_diameter(10)

    assert s.diameter == 10
    assert s.radius == 5
