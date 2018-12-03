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
        out_file.write(f"<{self.tag}>\n")
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
        out_file.write(f"\n</{self.tag}>\n")


class Body(Element):

    tag = "body"


class Paragraph(Element):

    tag = "p"


class Head(Element):

    tag = "head"


class OneLineTag(Element):
    def render(self, out_file):
        for content in self.contents:
            out_file.write(f"<{self.tag}>")
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
        out_file.write(f"</{self.tag}>\n")


class Title(OneLineTag):

    tag = "title"


class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)


class Hr(SelfClosingTag):

    tag = "hr"

    def render(self, out_file):
        out_file.write(f"<{self.tag}>")


class Anchor(OneLineTag):

    tag = "a"

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)

