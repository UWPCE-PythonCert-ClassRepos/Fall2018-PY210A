"""
Python210A Vincent Aquila  Fall2018
using Python 3.7.0
Session 08 - Circle
"""



from math import pi


class Circle():
    def __init__(self, radius):
    	self.radius = radius
    	#self.diameter = radius * 2
        
    @property
    def diameter(self):
    	return self.radius * 2
    
    @diameter.setter
    def diameter(self, value):
    	self.radius = value / 2

    @property
    def area(self, ):
    	return pi * self.radius ** 2	

    def __str__(self):
        return f"Circle with radius: {self.radius:.6f}"	







    
