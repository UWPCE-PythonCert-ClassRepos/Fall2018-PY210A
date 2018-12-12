from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return pi * (self.radius ** 2)


    def __str__(self):
        return "Circle with radius: {0:.6f}".format(self.radius)


    def __repr__(self):
        return f"Circle({self.radius})"


    @classmethod
    def from_diameter(Circle, value):
        return Circle(value / 2)


    def __add__(self, other):
        r = self.radius + other.radius
        return Circle(r)


    def __rmul__(self, value):
        return Circle(self.radius * value)


    def __mul__(self, value):
        return Circle(self.radius * value)


    def __lt__(self, other):
        return self.radius < other.radius


    def __eq__(self, other):
        return self.radius == other.radius


    def __gt__(self, other):
        return self.radius > other.radius


    def __sub__(self, other):
        return Circle(self.radius - other.radius)


    def __truediv__(self, value):
        return Circle(self.radius / value)


    def __cmp__(self,other):
        return cmp(self.radius, other.radius)

class Sphere(Circle):
    """
    There are several ways to initialize the subclass Sphere
    """

    def __init__(self, radius):
        super(Sphere, self).__init__(radius)

    
    def __str__(self):
        return "Sphere with radius: {0:.6f}".format(self.radius)


    def __repr__(self):
        return f"Sphere({self.radius})"


    @property
    def volume(self):
        return (4 / 3) * (pi * self.radius ** 3)

    @property
    def area(self):
        return 4 * pi * (self.radius ** 2)
    
