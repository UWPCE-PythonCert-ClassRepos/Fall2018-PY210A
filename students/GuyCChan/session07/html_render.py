#!/usr/bin/env python3
"""
A class-based system for rendering html.
"""

# This is the framework for the base class
class Element(object):

    tag = "html"

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.contents = []
        else:
            self.contents = [content]
        self.attributes = kwargs

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        # loop through the list of contents (see func above)
        out_file.write("<{}>\n".format(self.tag))
        for content in self.contents:
            # Replace "out_file.write(content)" with the next lines as failed test
            # shows 'AttributeError'.
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
    pass

    def render(self, out_file, **attributes):
        open_tag.write("<{} ".format(self.tag))
        for key, value in self.attributes.items():
            open_tag.write("{}='{}'".format(key, value))
        open_tag.append(">\n")
        out_file.write(self.contents[0])
        out_file.write("</{}>\n".format(self.tag))

    def append(self, content):
        raise NotImplementedError


class Title(OneLineTag):
    tag = "title"



