
from Circle_Class import Circle, Sphere

from math import pi

def test_init():
    c = Circle(4)


def test_radius():
    c = Circle(4)

    assert c.radius == 4
    
def test_diameter():
    c = Circle(4)

    assert c.diameter == 8


def test_set_diameter():
    c = Circle(7)
    c.diameter = 16

    assert c.radius == 8
    assert c.diameter == 16


def test_area():
    c = Circle(5)

    assert c.area == pi * 25


def test_str():
    c = Circle(10)

    assert str(c) == "Circle with radius: 10.000000"


def test_repr():
    c = Circle(10)
    d = eval(repr(c))

    assert repr(c) == "Circle(10)"
    assert d == c


def test_from_diameter():
    c = Circle.from_diameter(8)

    assert c.diameter == 8
    assert c.radius == 4



def test_add_two_circles():
    c1 = Circle(2)
    c2 = Circle(4)

    assert (c1 + c2) == Circle(6)


def test_mul():
    c2 = Circle(4)

    assert (c2 * 3) == Circle(12)
    assert (3 * c2) == Circle(12)


def test_compare():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(4)

    assert (c1 > c2) == False
    assert (c1 < c2) == True
    assert (c1 == c2) == False
    assert (c2 == c3) == True


def test_sort():
    circles = [Circle(6), Circle(8), Circle(5), Circle(1), Circle(0), Circle(10)]
    circles.sort()

    assert circles == [Circle(0), Circle(1), Circle(5), Circle(6), Circle(8), Circle(10)]


def test_reflected_numeric():
    c = Circle(2)

    assert (c * 3) == (3 * c)


def test_sub():
    c1 = Circle(5)
    c2 = Circle(1)

    assert (c1 - c2) == Circle(4)


def test_div():
    c1 = Circle(10)

    assert (c1 / 2) == Circle(5)


def test_sphere_str():
    s = Sphere(10)

    assert str(s) == "Sphere with radius: 10.000000"


def test_sphere_repr():
    s = Sphere(10)
    d = eval(repr(s))

    assert repr(s) == "Sphere(10)"
    assert d == s


def test_volume():
    s = Sphere(1)

    assert s.volume == (4 / 3) * pi


def test_sphere_area():
    s = Sphere(3)
    
    assert s.area == 4 * pi * 9
