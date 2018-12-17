#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element:
    tag = "html"
    indent = "    "

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.content = []
        else:
            self.content = [content]
        self.attributes = kwargs

    def append(self, new_content):
        self.content.append(new_content)

    def what_attr(self):
        if self.attributes:
            attrs = [f'{key}="{value}"' for key, value in
                    self.attributes.items()]
            attrs_str = " ".join(attrs)
            tag = f"<{self.tag} {attrs_str}"
        else:
            tag = f"<{self.tag}"
        return tag

    def render(self, out_file, cur_ind=""):
        out_file.write(self.what_attr())
        out_file.write(">\n")

        for content in self.content:
            try:
                content.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write(cur_ind + self.indent)
                out_file.write(content)
            out_file.write("\n")
        out_file.write(cur_ind)
        out_file.write(f"</{self.tag}>\n")

class Html(Element):
    tag = "html"
    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind)
        out_file.write("<!DOCTYPE html>\n")
        super().render(out_file, cur_ind)


class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"

class OneLineTag(Element):
    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind)
        out_file.write(f"<{self.tag}> ")
        for content in self.content:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
        out_file.write(f" </{self.tag}>\n")

class Title(OneLineTag):
    tag = "title"

class SelfClosingTag(Element):
    def render(self, out_file, cur_ind=""):
        out_file.write(self.what_attr())
        try:
            self.content != []
        except TypeError:
            print("Cannot put in a content")
        out_file.write(" />")

class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"

class A(OneLineTag):
    tag = "a"
    def __init__(self, link, content=None, **kwargs):
        self.link = [f'href="{link}">']
        if content is None:
            self.content = self.link
        else:
            self.content = self.link + [content]
        self.attributes = kwargs

class Ul(Element):
    tag = "ul"

class Li(Element):
    tag = "li"

class H(OneLineTag):
    tag = "H"

    def __init__(self, n, content=None, **kwargs):
        self.tag = "h" + str(int(n))
        super().__init__(content, **kwargs)

class Meta(SelfClosingTag):
    tag = "meta"
