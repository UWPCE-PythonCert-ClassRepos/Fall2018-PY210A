#!/usr/bin/env python3
####stopped at step 4
"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = "html"

    def __init__(self, content=None, **kwargs):
        self.contents = [content]
        # print("contents is:", self.contents)

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        # Loop through the list of contents:
        out_file.write("<{}>\n".format(self.tag))
        for content in self.contents:
            if content is not None:
                try:
                    content.render(out_file)
                except AttributeError:
                    out_file.write(content)
                out_file.write("\n")
        out_file.write("</{}>\n".format(self.tag))

class Html(Element):

    tag = "html"

class Body(Element):

    tag = "body"

class P(Element):

    tag = "p"

class Head(Element):

    tag = "head"

class OneLineTag(Element):

    def render(self, out_file):
        # One line render:
        #removing my way and implementing the tutorial way
        #out_file.write("<{}> {} </{}>\n".format(self.tag, self.contents, self.tag))
        out_file.write("<{}>".format(self.tag))
        out_file.write(self.contents[0])
        out_file.write("</{}>\n".format(self.tag))

    def append(self, content):
        raise NotImplementedError

class Title(OneLineTag):

    tag = "title"
