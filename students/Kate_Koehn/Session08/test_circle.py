from class_circle import Circle, Sphere
from math import pi

def test_init():
    c = Circle(10)


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


def test_string():
    c = Circle(10)

    assert str(c) == "Circle with radius: 10.000000"


def test_repr():
    c = Circle(10)

    assert repr(c) == "Circle(10)"


def test_add():
    c1 = Circle(6)
    c2 = Circle(4)

    assert (c1 + c2) == "Circle(10)"


def test_mul():
    c = Circle(10)

    assert c * 3 == "Circle(30)"


def test_rmul():
    c = Circle(10)

    assert 3 * c == "Circle(30)"


def test_eq():
    c1 = Circle(10)
    c2 = Circle(5)
    c3 = Circle(5)

    assert c1 != c2
    assert c2 == c3



def test_lt():
    c1 = Circle(2)
    c2 = Circle(4)

    assert c1 < c2


def test_gt():
    c1 = Circle(5)
    c2 = Circle(4)

    assert c1 > c2


def test_sort():
    c1 = Circle(10)
    c2 = Circle(4)
    c3 = Circle(5)

    circles = [c1, c2, c3]
    circles.sort()
    assert circles == [Circle(4), Circle(5), Circle(10)]


def test_sphere_init():
    c = Sphere(10)


def test_volume():
    c = Sphere(3)

    assert c.volume == ((4/3) * pi * (3^3))