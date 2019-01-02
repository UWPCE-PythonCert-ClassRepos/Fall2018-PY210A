from math import pi
import functools

# Create class Circle
@functools.total_ordering
class Circle(object):

    def __init__(self, radius):
        self.radius = radius
        #self.diameter = radius * 

    # Diameter property
    @property
    def diameter(self):
        return self.radius * 2

    # Set diameter proptery
    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    # Area property using imported pi
    @property
    def area(self):
        return self.radius**2 * pi

    # Use __str__ method
    def __str__(self):
        return f'Circle with radius: {self.radius:.6f}'


    # Use __repr__ method
    def __repr__(self):
        return f'Circle({self.radius})'
        # or
        return "Circle({})".format(repr(self.radius))

    # Add numeric protocol (addition)
    def __add__(self, other):
        return Circle(self.radius + other.radius)

    # Add multiply protocol
    def __mul__(self, other):
        return Circle(self.radius * other)

    # Reverse multiply
    def __rmul__(self, other):
        return Circle(self.radius * other)

    # Comparing two circles
    def __gt__(self, other):
        return Circle(self.radius > other.radius)

    def __lt__(self, other):
        return Circle(self.radius < other.radius)

    def __ne__(self, other):
        return Circle(self.radius != other.radius)

    def __eq__(self, other):
        return Circle(self.radius == other.radius)

    # # Sorting circles
    """This is the long way without using functool"""
    # def __sort__(self):
    #     circ_list = [Circle(1), Circle(3), Circle(2), Circle(6), Circle(0),
    #                  Circle(5), Circle(4), Circle(7), Circle(8),
    #                 ]
    #     return sorted(circ_list)
    #     print(circ_list)

    # def __sort__(self):
    #     circ_list = [Circle(1), Circle(3), Circle(2), Circle(6), Circle(0),
    #                  Circle(5), Circle(4), Circle(7), Circle(8),
    #                 ]
    #     return sorted(circ_list, reverse=True)
    #     print(circ_list)

# Using the shorter version using functools
    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius


# Subclassing
class Sphere(Circle):
    def volume(self):
        return 5 / 3 * pi * self.radius ** 3

    def area(self):
        raise NotImplementedError("Spheres do not have areas")


    def __str__(self):
        return f'Sphere with radius: {self.radius}'

    def __repr__(self):
        return f'Sphere({self.radius})'