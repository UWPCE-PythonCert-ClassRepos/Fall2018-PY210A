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

    def _open_tag(self):
        return "<{}>".format(self.tag)

    def _close_tag(self):
        return "</{}>".format(self.tag)

    def render(self, out_file):
        if self.attrs is None:
            out_file.write(self._open_tag())
        else:
            out_file.write(f"<{self.tag}")
            for tag, attribute in self.attrs.items():
                out_file.write(f' {tag}="{attribute}"')
            out_file.write(">")
        out_file.write("\n")

        for content in self.content:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
                out_file.write("\n")
        out_file.write(self._close_tag())
        out_file.write("\n")




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
            raise TypeError("SelfClosingTag can not contain any content.")
        self.attrs = dict(**kwargs)

    def append(self, new_content):
        if new_content:
            raise TypeError("You cannot add content to a SelfClosingTag")

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
        raise NotImplementedError("You cannot add content to a OneLineTag")


class Title(OneLineTag):
    tag = "title"


class A(OneLineTag):
    tag = "a"

    def __init__(self, link, content):
        self.kwargs = {"href": link}
        self.content = [content]
        self.attrs = dict(**self.kwargs)



class Ul(Element):
    """
    Unordered list
    """
    tag = "ul"


class Li(Element):
    tag = "li"

class H(OneLineTag):
    """
    Header
    """
    def __init__(self, num, content=None, **kwargs):
        self.number = num
        self.content = [content]
        self.tag = "h" + str(num)
        self.attrs = dict(**kwargs)







