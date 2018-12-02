import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __str__(self):
        return f"Circle with radius of {self.radius}"

    def __repr__(self):
        return f"Circle({self.radius})"

    def __add__(self, new):
        total = self.radius + new.radius
        return Circle(total)

    def __lt__(self, other):
        return self.radius < other.radius

    # Figure out how to make this diameter settable.
    @property
    def diameter(self):
        return self.radius*2

    @property
    def area(self):
        return round(self.radius**2*math.pi, 2)


