#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element:

    def __init__(self, content=None):
        self.content = [content]

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, out_file):
        out_file.write('<html>\n')
        for line in self.content:
            out_file.write(line)
            out_file.write('\n')
        out_file.write('</html>')
        # out_file.write('<html>{}</html>'.format(''.join(self.content)))
