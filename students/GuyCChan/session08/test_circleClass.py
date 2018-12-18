from circleClass import Circle, Sphere
import pytest
from math import pi

# Test for initialization of the class.
def test_init():
    Circle(4)

def test_radius():
    c = Circle(4)
    assert c.radius == 4
    assert c.radius != 6

def test_diameter():
    c = Circle(4)
    assert c.diameter == 8
    assert c.diameter != 10

def test_radius_reset():
    c = Circle(4)
    c.radius = 10
    assert c.radius == 10
    assert c.diameter == 20

def test_diameter_set():
    c = Circle(10)
    c.diameter = 8
    assert c.diameter == 8
    assert c.radius == 4
    assert c.radius != 10

def test_area():
    c = Circle(5)
    assert c.area == pi * 5 **2
    assert c.area != 80

def test_area_from_diam():
    c = Circle(5)
    assert c.area == pi * 5 ** 2

def test_area_from_diameter():
    c = Circle(7)
    assert c.area == pi * 7 ** 2

def test_str():
    """ Test for printing string, informal representation of object."""
    c = Circle(5)
    assert str(c) == "A circle with radius: 5"

def test_repr():
    """ Test for printing formal representation of object."""
    c = Circle(10.0)
    assert repr(c) == "Circle(10.0)"

def test_add_radius():
    """ Test for adding 2 radii."""
    c1 = Circle(5)
    c2 = Circle(15)
    c3 = c1 + c2
    assert c3.radius == 20
    assert c3.radius != 5

def test__add__():
    """ Test for alternative way of addition."""
    c1 = Circle(10)
    c2 = Circle(20)
    c3 = c1 + c2
    assert c3.radius == 30
    assert c3.radius != 10

def test__mul__():
    """Test for increase by a factor."""
    c1 = Circle(5)
    factor = 3
    c2 = c1 * factor
    assert c2.radius == 15

def test_incr():
    """ Test for alternative way to increase by a factor."""
    c1 = Circle(12)
    factor = 4
    c3 = c1 * factor
    assert c3.radius == 48

def test__gt__():
    """ Test for 'greater than'."""
    c1 = Circle(10)
    c2 = Circle(8)
    assert c1 > c2
    assert c1 != c2

def test__lt__():
    """ Test for 'less than'."""
    c1 = Circle(15)
    c2 = Circle(18)
    assert c1 < c2
    assert c1 != c2

def test__eq__():
    """ Test for 'equal to'."""
    c1 = Circle(5)
    c2 = Circle(5)
    assert c1 == c2

def test_circles_sort():
    """ Test sorting."""
    circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3),
    Circle(5), Circle(9), Circle(1)]
    assert Circle(6) < Circle(8)
    assert Circle(3) < Circle(5)
    assert Circle(2) > Circle(1)
    assert Circle(9) > Circle(7)

def test_volume():
    """ Test for volume of the sphere."""
    s = Sphere(1.0)
    assert s.volume == 4 / 3 * pi

def test_surf_area():
    """ Test for surface area of the sphere class."""
    s = Sphere(1.0)
    assert s.surf_area == 4 * pi

def test__str__():
    """ Test for printing informal representation of object using string."""
    s = Sphere(5.0)
    assert str(s) == "A sphere with radius: 5.0"

def test__repr__():
    """ Test for printing formal representation of object using repr."""
    s = Sphere(10.0)
    assert repr(s) == "Sphere (10.0)"

def test_volume_from_diam():
    """ Test for finding volume of sphere from diameter."""
    s = Sphere.from_diameter(2)
    assert s.radius == 1













