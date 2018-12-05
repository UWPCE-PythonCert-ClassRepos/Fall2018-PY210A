class Circle():


    def __init__(self, radius):
        from math import pi
        self.pi = pi
        self.radius = radius


    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return self.pi * self.radius**2

    def __str__(self):
        return f'Circle with radius: {self.radius:.6f}'

    def __repr__(self):
        return "Circle({})".format(self.radius)