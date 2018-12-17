#!/usr/bin/env python3

class Circle():
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius


c = Circle(5)
print(c.radius)

c.radius = 7
print(c.diameter)
