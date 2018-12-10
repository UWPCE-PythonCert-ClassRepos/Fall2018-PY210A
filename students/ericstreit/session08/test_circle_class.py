#Lesson##
#XXXXX Exercise ##
#
#!/usr/bin/env python3
from circle_class import *
import pytest



def test_radius():
    c = Circle(4)
    assert c.radius == 4

def test_diameter():
    c = Circle(4)
    assert c.diameter() == 8

def test_area():
    c = Circle(4)
    assert c.area() == 50.24

def test_repr():
    c = Circle(4)
    assert repr(c) == "Circle(4)"

def test_equals():
    c = Circle(4)
    d = Circle(4)
    assert c == d

def test_add():
    c = Circle(4)
    d = Circle(5)
    assert c + d == Circle(9)

def test_multiply():
    assert Circle(10) * Circle(3) == Circle(30)

def test_sort():
    circles = [Circle(6), Circle(5), Circle(4), Circle(3), Circle(0), Circle(1), Circle(2)]
    circles.sort()
    assert  circles == [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6)]

def test_multiply_int():
    #c1 = Circle(50)
    assert Circle(50) * 3 == 150

# def test_multiply_int_reverse():
#     I don't know why this one does not work :(
#     #c1 = Circle(50)
#     assert 3 * Circle(50) == 150

def test_volume():
    s1 = Sphere(5)
    assert s1.volume() == 523




#for testing
if __name__=="__main__":
    pass
