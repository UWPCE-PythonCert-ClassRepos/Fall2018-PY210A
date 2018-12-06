#!/usr/bin/env Python3

##############
# Date: November 28, 2018
# Author: Carol Farris
# Goal: Gain familiarity with testing classes
##############


from math import pi


import pytest


from circle import Circle, Sphere


def test_init_circle():
    Circle(4)


def test_radius_circle():
    c = Circle(4)

    assert c.radius == 4


def test_set_radius():
    c = Circle(8)
    c.diameter = 14

    assert c.radius == 7


def test_diameter_circle():
    c = Circle(4)

    assert c.diameter == 8


def test_from_diameter():
    c = Circle.from_diameter(8)
    print(c)
    assert c.radius == 4
    assert c.diameter == 8


def test_area():
    c = Circle(2)

    assert c.area == 4 * pi

    with pytest.raises(AttributeError) as e:
        c.area = 4

    assert str(e.value) == 'can\'t set attribute'



def test_str_():
    c = Circle(4)

    assert str(c) == "Circle with a radius 4.000000"


def test_repr_():
    c = Circle(4)

    assert repr(c) == 'Circle(4)'


def test_add_():
    c = Circle(4)
    d = Circle(6)
    print(c + d)
    assert (c + d) == Circle(10)



def test_mult_():
    c = Circle(4)

    assert c * 3 == Circle(12)


def test_rmult_():
    c = Circle(4)

    assert 3 * c == Circle(12)


def test__eq__():
    a = Circle(40)
    b = Circle(1)
    c = Circle(2)
    d = Circle(2)

    circles = [a, b, c, d]
    circles.sort()
    assert c == d
    assert b != c
    assert circles == [Circle(1), Circle(2), Circle(2), Circle(40)]



###################
#Test Sphere
###################

def test_init_sphere():
    Sphere(4)


def test_volume_sphere():
    s = Sphere(3)

    assert s.volume == 113.09733552923254


def test_area_sphere():
    s = Sphere(2)
    sph = Sphere(4)

    assert s.area == 50.26548245743669
    assert sph.area == 201.06192982974676


def test_rpr_():
    s = Sphere(2)

    assert repr(s) == 'Sphere(2)'


def test_str_():
    s = Sphere(2)

    assert str(s) == "Sphere with a radius 2.000000"


def test_sphere_from_diameter():
    s = Sphere.from_diameter(8)

    assert s.radius == 4
    assert s.diameter == 8    
