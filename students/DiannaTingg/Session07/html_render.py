#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = "html"

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.content = []
        else:
            self.content = [content]
        self.attrs = dict(**kwargs)

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, out_file):
        for content in self.content:
            if self.attrs is None:
                out_file.write("<{}>\n".format(self.tag))
            else:
                out_file.write(f"<{self.tag}")
                for tag, attribute in self.attrs.items():
                    out_file.write(f' {tag}="{attribute}"')
                out_file.write(">\n")
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

class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content:
            raise TypeError
        self.attrs = dict(**kwargs)

    def append(self, new_content):
        if new_content:
            raise TypeError

    def render(self, out_file):
        if self.attrs is None:
            out_file.write("<{} />\n".format(self.tag))
        else:
            out_file.write(f"<{self.tag}")
            for tag, attribute in self.attrs.items():
                out_file.write(f' {tag}="{attribute}"')
            out_file.write(" />\n")

class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class OneLineTag(Element):
    def render(self, out_file):
        if self.attrs is None:
            out_file.write("<{}>{}</{}>\n".format(self.tag, self.content[0], self.tag))
        else:
            out_file.write(f"<{self.tag}")
            for tag, attribute in self.attrs.items():
                out_file.write(f' {tag}="{attribute}"')
            out_file.write(">{}</{}>\n".format(self.content[0], self.tag))

    def append(self, new_content):
        raise NotImplementedError


class Title(OneLineTag):
    tag = "title"
