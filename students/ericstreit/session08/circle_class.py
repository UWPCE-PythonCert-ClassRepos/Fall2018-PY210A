#Lesson08
#Circle Class Exercise ##
#
#!/usr/bin/env python3
import math
#define class
class Circle(object):
    """
    Description of class

    :param arg1: The first very important parameter. And a bit about
                 what it means.
    :param arg2: The second very important parameter. And now some
                 description of how this is used
    etc
    """
    def __init__(self, rad):
        self.radius = rad

    def diameter(self):
        return self.radius * 2

    def area(self):
        return 3.14 * (self.radius * self.radius)

### make an alternate constructor!

    def __repr__(self):
        return "Circle({})".format(self.radius)

    def __str__(self):
        return "Circle with a radius of: {}".format(self.radius)

    def __eq__(self, other):
        if type(other) == int:
            return (self.radius == other)
        else:
            return (self.radius == other.radius)

    def __lt__(self, other):
        return (self.radius < other.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        if type(other) == int:
            return Circle(self.radius * other)
        else:
            return Circle(self.radius * other.radius)

class Sphere(Circle):

    def volume(self):
        return int((4 / 3) * 3.14 * (self.radius ** 3))

    def __repr__(self):
        return "Sphere({})".format(self.radius)

    def __str__(self):
        return "Sphere with a volume of: {}".format(self.volume())

    def area(self):
        raise NotImplementedError('Please run the surface_area function instead')

#for testing
if __name__=="__main__":
    pass
