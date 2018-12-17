from circle import Circle
from circle import Sphere
from math import pi

c = Circle(5)
s = Sphere(3)

def test_radius():

    assert c.radius == 5

def test_diameter():

    assert c.diameter == 10

def test_area():

    assert c.area == pi * 25

def test_str():

    assert str(c) == 'Circle with a radius: 5.000000'

def test_repr():

    assert repr(5) == "Circle(5)"

def test_add():
    c2 = Circle(6)
    cT = c + c2

    assert  cT.radius == 11

def test_mul():
    c3 = c * 3

    assert c3.radius == 15

def test_comparison():
    c5 = Circle(5)

    assert c5 == c

    c4 = Circle(4)

    assert c4 < c
    assert not (c4 > c)

    c6 = Circle(6)

    assert c6 > c
    assert not (c6 < c)

def test_circle_sort():

    circles = [Circle(10), Circle(5), Circle(30), Circle(25), Circle(15)]
    circles.sort()

    assert circles == [Circle(5), Circle(10), Circle(15), Circle(25), Circle(30)]

def test_sphere_area():

    assert s.area == 4 * pi * 9

def test_sphere_volume():

	assert s.volume == (4 / 3) * pi * 27
 