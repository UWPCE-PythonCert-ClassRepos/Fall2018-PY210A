#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    def __init__(self, content=None):
        print('in __init__')
        print(content)
        print(self)
        self.content = [content] # created a list with content

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, out_file):
    	for line in self.content:
        	out_file.write(line)
        	out_file.write("\n")
