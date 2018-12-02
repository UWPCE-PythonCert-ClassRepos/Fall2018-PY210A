from math import pi
from circle import Circle
from circle import Sphere



def test_cicle():
    """Construction of circle with radius 10"""
    c = Circle(10)
    assert c.radius == 10

def test_diameter():
    """Alternate construction with diameter 10"""
    c = Circle(5)
    assert c.diameter == 10

def test_set_radius():
    """Tests setting radius of contructed circle."""
    c = Circle(8)
    c.diameter = 14
    assert c.radius == 7
    assert c.diameter == 14

def test_area():
    """Tests area of circle"""
    c = Circle(2)
    assert c.area == pi * 4


def test_str():
    """Tests string method for circle object."""
    c = Circle(10)
    assert c.__str__() == "Circle with radius 10.000000"

def test_repr():
    """Tests string method for circle object."""
    c = Circle(8)
    assert c.__repr__() == "Circle with radius 8.000000"

def test_from_diameter():
    """Tests alternate constructor method for circle object."""
    c = Circle.from_diameter(8)
    assert c.radius == 4


def test_circle_add():
    """Tests addition of circle objects."""
    c2 = Circle(2)
    c4 = Circle(4)
    assert c2 + c4 == 'Circle with radius 6.000000'


def test_circle_mul():
    """Tests multiplication of circle objects with both objects of type
    Circle."""
    c2 = Circle(2)
    c4 = Circle(4)
    assert str(c2 * c4) == 'Circle with radius 8.000000'


def test_circle_mul2():
    """Tests multiplication of circle objects with one object of type
    Circle and the other with type int."""
    c2 = Circle(2)
    c4 = 8
    assert str(c2 * c4) == 'Circle with radius 16.000000'


def test_circle_lt():
    """Tests less than operators for circle class objects."""
    c2 = Circle(2)
    c4 = Circle(4)
    assert (c2 < c4) == True


def test_circle_le():
    """Tests less than or equpal to operators for circle class objects."""
    c2 = Circle(2)
    c4 = Circle(4)
    assert (c2 <= c4) == True


def test_circle_eq():
    """Tests equal to operators for circle class objects."""
    c2 = Circle(2)
    c2a = Circle(2)
    assert (c2 == c2a) == True

def test_sphere():
    """Tests construction of Sphere object with radius 2."""
    s2 = Sphere(2)
    assert str(s2) == 'Sphere with radius 2.000000'

def test_sphere_sa():
    """Tests computation for surface area of Sphere object."""
    s2 = Sphere(4)
    assert s2.area == (4 * pi * 4 ** 2)
