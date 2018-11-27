#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element:
    tag = "html"

    def __init__(self, content=None, **kwags):
        if content:
            self.contents = [content]
        else: self.contents = []
        self.tag_attributes = kwags

    def append(self, new_content):
        self.contents.append(new_content)


    def render(self, out_file):
        open_tag = ["<{}".format(self.tag)]
        # print(self.tag_attributes.keys(), self.tag_attributes.values())
        for key, value in self.tag_attributes.items():
            open_tag.append(' {}="{}"'.format(key, value))
        open_tag.append(">\n")
        out_file.write("".join(open_tag))
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write("\n")
        out_file.write("</{}>".format(self.tag))



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
        out_file.write("<{}>".format(self.tag))
        out_file.write(self.contents[0])
        out_file.write("</{}>\n".format(self.tag))

    def append(self, content):
        raise NotImplementedError

class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):
    pass


class Hr(SelfClosingTag):
    tag = "hr"
