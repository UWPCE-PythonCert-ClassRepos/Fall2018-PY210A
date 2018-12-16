

from ultimate_circle import circle
from ultimate_circle import Sphere
import pytest

def test_circle_class():
    circle()
    circle(4)


def test_circle_radius():
    c = circle(4)
    assert c.radius == 4

def test_circle_diameter():
    c = circle(4)
    assert c.diameter == 8

def test_circle_change_diameter():
    c = circle(4)
    assert c.radius == 4
    c.diameter = 2
    assert c.radius == 1
    assert c.diameter == 2

def test_area():
    c = circle(4)
    assert "{:.2f}".format(c.area) == '50.27'
    with pytest.raises(AttributeError):
        c.area = 50

def test_circle_by_diameter():
    c = circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4

def test_string():
    c = circle(4)
    assert c.__str__() == "Circle with radius: 4.000000"

def test_repr():
    c = circle(4)
    assert (repr(c)) == "Circle(4)"

def test_circle_add():
    c1 = circle(2)
    c2 = circle(4)
    assert repr(c1 + c2) == "Circle(6)"

def test_circle_multiply_by_number():
    c = circle(4)
    assert repr(c * 3) == "Circle(12)"

def test_circle_compare():
    c1 = circle(2)
    c2 = circle(4)
    assert (c1 > c2) == False
    assert (c1 < c2) is True
    assert (c1 == c2) is False
    c3 = circle(4)
    assert c2 == c3

def test_circle_sort():
    circles = [circle(6), circle(7), circle(8), circle(4), circle(0), circle(2), circle(3), circle(5), circle(9), circle(1)]
    circles.sort()
    assert circles == [circle(0), circle(1), circle(2), circle(3), circle(4), circle(5), circle(6), circle(7), circle(8), circle(9)]


def test_sphere_init():
    Sphere()
    Sphere(4)

def test_sphere_string():
    s = Sphere(4)
    assert s.__str__() == "Sphere with radius: 4.000000"

def test_sphere_repr():
    s = Sphere(4)
    assert (repr(s)) == "Sphere(4)"

def test_sphere_volume():
    s = Sphere(4)
    print(s)
    print(s.volume)
    assert "{:.2f}".format(s.volume) == '268.08'

def test_sphere_area():
    s = Sphere(4)
    print(s.area)
    assert "{:.2f}".format(s.area) == '201.06'

def test_sphere_from_diameter():
    s = Sphere.from_diameter(8)
    assert s.radius == 4

def test_sphere_adding():
    s1 = Sphere(2)
    s2 = Sphere(3)
    assert s1 + s2 == Sphere(5)
