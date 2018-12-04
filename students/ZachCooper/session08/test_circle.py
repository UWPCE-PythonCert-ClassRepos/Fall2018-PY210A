
from circle import Circle
from circle import Sphere
from math import pi

def test_init():
    Circle(10)

#Step 1
def test_radius():
    c = Circle(25)

    assert c.radius == 25

# Step 2
def test_diameter():
    c = Circle(5)

    assert c.diameter == 10

# Step 3
def test_set_radius():
    c = Circle(8)
    c.diameter = 14

    assert c.radius == 7
    assert c.diameter == 14

# Step 4
def test_area():
    c = Circle(2)

    assert c.area == pi * 4

# Step 5 Alternate Constructor???

# Step 6
def test_str():
    c = Circle(10)

    assert str(c) == 'Circle with radius: 10.000000'

def test_repr():
    c = Circle(4)
    
    assert repr(c) == 'Circle(4)'

# Step 7
def test_addition():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = c1 + c2

    assert c3.radius == 6

def test_multiply():
    c2 = Circle(4)
    c3 = c2 * 3
    assert c3.radius == 12

def test_reverse_multiply():
    c = Circle(3)

    c2 = 3 * Circle(3)

    assert c2.radius == 9.0

# Comparing Circles
# Greter than
def test_gt():
    c1 = Circle(3)
    c2 = Circle(5)
    #c3 = c1 > c2

    #assert c3
    assert c1 > c2

# Less than
def test_lt():
    c1 = Circle(3)
    c2 = Circle(5)

    assert c1 < c2 

# Equal
def test_not_eq():
    c1 = Circle(3)
    c2 = Circle(5)

    assert c1 != c2

# Equal is true
def test_eq():
    c1 = Circle(3)
    c2 = Circle(5)
    c3 = Circle(5)

    assert c2 == c3 

# # Circles sorted
"""How do I use the sorted method for this???"""
def test_sorted_circles():
    circ_list = [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4),
               Circle(5), Circle(6), Circle(7), Circle(8),
                ]
#     circ_list.sorted()


    assert circ_list[0] == Circle(0)
    assert circ_list[6] == Circle(6)
    assert [circ_list[0] < circ_list[1] < circ_list[2] < circ_list[3] < circ_list[4]
        < circ_list[5] < circ_list[6] < circ_list[7] < circ_list[8]
           ]

def test_reverse_sorted_circles():
    circ_list = [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4),
                 Circle(5), Circle(6), Circle(7), Circle(8),
                ]

    assert circ_list[0] == Circle(8)
    assert circ_list[7] == Circle(0)

# Step 8

# Step 9 Subclasing
def test_sphere_volume():
    s = Sphere(5)

    print(s.volume())

    assert s.volume() == 654.4984694978737
    

def test_sphere_area():
    s = Sphere(4)

    assert NotImplementedError

def test_str_sphere():
    s = Sphere(5)

    assert str(s) == "Sphere with radius: 5"

def test_repr_sphere():
    s = Sphere(12)

    assert repr(s) == "Sphere(12)"