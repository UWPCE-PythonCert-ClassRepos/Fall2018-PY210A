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













# The goal is to create a class that represents a simple circle.

# A Circle can be defined by either specifying the radius or the diameter, and
#the user can query the circle for either its radius or diameter.

# Other abilities of a Circle instance:

# Compute the circle’s area.
# Print the circle and get something nice.
# Be able to add two circles together.
# Be able to compare two circles to see which is bigger.
# Be able to compare to see if they are are equal.
# (follows from above) be able to put them in a list and sort them.
# You will use:

# properties.
# a bunch of “magic methods”.
# a classmethod (after you’ve learned about them…).
# General Instructions:
# For each step, write a couple of unit tests that test the new features.
# Run these tests (and they will fail the first time)
# Add the code required for your tests to pass.
# Step 1:
# Create class called Circle – it’s signature should look like:

# c = Circle(the_radius)
# The radius is a required parameter (can’t have a circle without one!)

# The resulting circle should have an attribute for the radius:

# c.radius
# So you can do:

# >> c = Circle(4)
# >> print(c.radius)
# 4
# Remember: tests first!

# Step 2:
# Add a “diameter” property, so the user can get the diameter of the circle:

# >> c = Circle(4)
# >> print(c.diameter)
# 8
# Step 3:
# Set up the diameter property so that the user can set the diameter of the circle:

# >> c = Circle(4)
# >> c.diameter = 2
# >> print c.diameter
# 2
# >> print c.radius
# 1
# NOTE that the radius has changed!

# Important: Do not store both the radius and the diameter as attributes! If you
#do that, they could get out of sync. So store only one (the radius), and have
#the other calculated “on the fly” by the property.

# Step 4:
# Add an area property so the user can get the area of the circle:

# >> c = Circle(2)
# >> print(c.area)
# 12.566370
# (pi can be found in the math module).

# The user should not be able to set the area:

# >> c = Circle(2)
# >> c.area = 42
# AttributeError
# Step 5:
# NOTE: wait on this one ‘till we learn about class methods..

# Add an “alternate constructor” that lets the user create a Circle directly
#with the diameter:

# >> c = Circle.from_diameter(8)
# >> print(c.diameter)
# 8
# >> print(c.radius)
# 4
# Step 6:
# Every class should have a nice way to print it out…

# Add __str__ and __repr__ methods to your Circle class.

# Now you can print it:

# In [2]: c = Circle(4)

# In [3]: print(c)
# Circle with radius: 4.000000

# In [4]: repr(c)
# Out[4]: 'Circle(4)'

# In [5]: d = eval(repr(c))

# In [6]: d
# Out[6]: Circle(4)
# Step 7:
# Add some of the numeric protocol to your Circle:

# You should be able to add two circles:

# In [7]: c1 = Circle(2)

# In [8]: c2 = Circle(4)

# In [9]: c1 + c2
# Out[9]: Circle(6)
# and multiply one by a number:

# In [16]: c2 * 3
# Out[16]: Circle(12)
# (what happens with 3 * c2 ? – can you fix that?)

# Step 8:
# Add the ability to compare two circles:

# In [10]: c1 > c2
# Out[10]: False

# In [11]: c1 < c2
# Out[11]: True

# In [12]: c1 == c2
# Out[12]: False

# In [13]: c3 = Circle(4)

# In [14]: c2 == c3
# Out[14]: True
# Once the comparing is done, you should be able to sort a list of circles:

# In [18]: print circles
# [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3),
#Circle(5), Circle(9), Circle(1)]

# In [19]: circles.sort()

# In [20]: print circles
# [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6),
#Circle(7), Circle(8), Circle(9)]
# NOTE: make sure to write unit tests for all of this! Ideally before writing
#the code.

# Step 8: Optional Features:
# See if you can make “reflected” numerics do the right thing:
# a_circle * 3 == 3 * a_circle
# What else makes sense: division? others?
# Add the “augmented assignment” operators, where they make sense:
# a_circle += another_circle

# a_circle *= 2
# Look through all the “magic methods” and see what makes sense for circles.
# Step 9: Subclassing!
# You’ve got a circle already – what if you needed a Sphere? They have a fair
#bit in common – both defined by a radius, same relationship of radius to diameter,
#etc.

# So we can get a pretty useful Sphere class by simply subclassing Circle, and
#adding and changing a couple things.

# Create a Sphere Class that subclasses Circle.
# Override the __str__ and __repr__ methods to be appropriate for Spheres.
# Create a volume property that returns the volume (hint: volume of a sphere is:
#4/3 pi r^3).
# Override the area property so that it either computes the surface area of a
#sphere (what’s the formula for that???), or have it raise an exception: maybe
#NotImplementedError.
# Make sure to write some tests – maybe ahead of time! – that confirm that all
#this works. And the other things like addition, and sorting…

# Check that the Sphere.from_diameter() alternate constructor actually creates
#a Sphere! (you DO NOT have to write a new classmethod for that!) – pretty cool, eh?


