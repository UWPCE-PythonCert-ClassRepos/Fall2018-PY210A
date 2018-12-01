import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"Circle with radius of {self.radius}"

    def __repr__(self):
        return f"Circle({self.radius})"

    def __add__(self, new):
        total = self.radius + new.radius
        return Circle(total)

    @property
    # Figure out how to make this diameter settable.
    def diameter(self):
        return self.radius*2

    @property
    def area(self):
        return round(self.radius**2*math.pi, 2)


c = Circle(200)
c2 = Circle(500)
print(c.diameter)
print(c.area)
print(repr(c))
print(str(c))
c3 = c + c2
print(c3)
print(c3.area)
