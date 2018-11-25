#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element:

    tag = "html"
    indent = 4
    def __init__(self, content=None, **kwargs):
        if content:
            self.content = [content]
        else:
            self.content = []
        self.attributes = kwargs.items()

    def append(self, new_content):
        self.content.append(new_content)

    def _open_tag(self):
        tag = ["<{}".format(self.tag)]
        for key, value in self.attributes:
            tag.append(' {}="{}"'.format(key, value))
        tag.append(">")
        return "".join(tag)

    def _close_tag(self):
        return "</{}>".format(self.tag)

    def render(self, outfile, cur_ind=0):
        outfile.write(" " * cur_ind)
        outfile.write(self._open_tag())
        outfile.write("\n")
        for line in self.content:
            try:
                line.render(outfile, cur_ind + self.indent)
            except AttributeError:
                outfile.write(" " * (cur_ind + self.indent) + line)
            outfile.write("\n")
        outfile.write(" " * cur_ind + self._close_tag())

class Html(Element):
    tag = "html"
    html_doctype = "<!DOCTYPE html>"

    def render(self, outfile, cur_ind=0):
        outfile.write(self.html_doctype + "\n")
        super().render(outfile, cur_ind)


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"

class OneLineTag(Element):
    def append(self, content):
        raise NotImplementedError

    def render(self, outfile, cur_ind=0):
        outfile.write(" " * cur_ind)
        outfile.write(self._open_tag())
        outfile.write(self.content[0])
        outfile.write(self._close_tag())

class title(OneLineTag):
    tag = "title"

class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def append(self, content):
        raise TypeError("You can not add content to a SelfClosingTag")

    def render(self, outfile, cur_ind=0):
        outfile.write(" " * cur_ind)
        tag = self._open_tag()[:-1] + " />"
        outfile.write(tag)

class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"

class Meta(SelfClosingTag):
    tag = "meta"


class A(OneLineTag):
    tag = "a"

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)

class Ul(Element):
    tag = "ul"

class Li(Element):
    tag = "li"

class H(OneLineTag):

    def __init__(self, level, content=None, **kwargs):
        self.tag = "h" + str(level)
        super().__init__(content, **kwargs)

class head(Element):
    tag = "head"
