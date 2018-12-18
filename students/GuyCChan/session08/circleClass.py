from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius

# Chris, if I already have the properties decorator for diameter. What extra does
# it do or what differences are there in making a classmethod for diameter?
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    @property
    def diameter(self):
        """ Add properties decorator for diameter."""
        return self.radius * 2

    @diameter.setter
    def diameter_set(self, value):
        """ Make properties setter for diameter."""
        self.radius = value/2

    @property
    def area(self):
        """ Find area using radius."""
        return pi * self.radius**2

# classmethod to find area using radius. I still haven't figured out the difference between this and the last"""
# If this is a classmethod, then the first parameter should be 'cls' instead of 'self'. Please explain."""
# This should only be necessary if the above method was not included at initialization of the class but is """
# added later. Is this correct? """
#     @classmethod
#     def area_from_rad(cls):
#         return cls(self.radius)**2 * pi

    @property
    def area_from_diam(self):
        """ Find area using diameter."""
        return pi * (self.diameter/2)**2

    @classmethod
    def area_from_diameter(cls, diameter):
        """ classmethod to find area using diameter."""
        return cls(diameter / 2)**2 * pi

    @property
    def __str__(self):
        """ print the informal representation of an object, or string."""
        return f"A circle with radius: {self.radius}"

    @property
    def __repr__(self):
        """ Print the formal representation of an object with more precise values when appropriate."""
        return f"Circle ({self.radius})"

    def add_radius(self, other):
        """ Method to add 2 radii."""
        return Circle(self.radius + other.radius)

    def __add__(self, other):
        """ Alternative Method for adding 2 radii using __add__."""
        return Circle(self.radius + other.radius)

    def __iadd__(self, other):
        """ Method for in-place adding of 2 radii."""
        self.radius += other.radius
        return self

    def __mul__(self, factor):
        """ Method to increase by a factor."""
        return Circle(self.radius * factor)

    def incr(self, factor):
        """ Alternative method to increase by a factor."""
        return Circle(self.radius * factor)

    def __gt__(self, other):
        """ Method to compare, 'greater than'."""
        return self.radius > other.radius

    def __lt__(self, other):
        """ Method to compare, 'less than'."""
        return self.radius < other.radius

    def __eq__(self, other):
        """ Method to compare, 'equal to'."""
        return self.radius == other.radius

    @staticmethod
    def circle_sort(circle):
        """ Staticmethod to sort circles."""
        return circle.radius

class Sphere(Circle):
    @property
    def volume(self):
        """ Create a subclass 'Sphere' and to calculate the volume of a sphere using V = 4/3 * pi * r ** 3."""
        return 4/3 * pi * self.radius ** 3

    @property
    def surf_area(self):
        """ Calculate the surface area of a sphere using A = 4 * pi * r ** 2."""
        return 4 * pi * self.radius ** 2

    def __str__(self):
        """ Print the object 'sphere' using the informal representation, string."""
        return f"A sphere with radius: {self.radius}"

    def __repr__(self):
        """ Print the formal representation of the object 'sphere'."""
        return f"Sphere ({self.radius})"

    @classmethod
    def volume_from_diam(cls, diameter):
        """ Find the volume of a sphere with diameter."""
        return 4/3 * pi * (self.diameter / 2) ** 3

