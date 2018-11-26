#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    indent = "    "
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

    def render(self, out_file, cur_ind=""):
        if self.attrs is None:
            out_file.write(cur_ind)
            out_file.write(self._open_tag())
        else:
            out_file.write(cur_ind)
            out_file.write(f"<{self.tag}")
            for tag, attribute in self.attrs.items():
                out_file.write(f' {tag}="{attribute}"')
            out_file.write(">")
        out_file.write("\n")

        for content in self.content:
            try:
                content.render(out_file, (cur_ind + self.indent))
            except AttributeError:
                out_file.write(cur_ind + self.indent)
                out_file.write(content)
                out_file.write("\n")
        out_file.write(cur_ind)
        out_file.write(self._close_tag())
        out_file.write("\n")


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


class Ul(Element):
    tag = "ul"


class Li(Element):
    tag = "li"


# OneLineTag
class OneLineTag(Element):
    def render(self, out_file, cur_ind=""):
        if self.attrs is None:
            out_file.write("{}<{}>{}</{}>\n".format(cur_ind, self.tag, self.content[0], self.tag))
        else:
            out_file.write(f"{cur_ind}<{self.tag}")
            for tag, attribute in self.attrs.items():
                out_file.write(f' {tag}="{attribute}"')
            out_file.write(">{}</{}>\n".format(self.content[0], self.tag))

    def append(self, new_content):
        raise NotImplementedError("You cannot add content to a OneLineTag")


class Title(OneLineTag):
    tag = "title"


class A(OneLineTag):
    tag = "a"

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)


class H(OneLineTag):
    def __init__(self, num, content=None, **kwargs):
        header_tag = "h" + str(num)

        super().__init__(content=content, **kwargs)
        self.tag = header_tag


# SelfClosingTag
class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content:
            raise TypeError("SelfClosingTag can not contain any content.")
        super().__init__(content=content, **kwargs)

    def append(self, new_content):
        if new_content:
            raise TypeError("You can not add content to a SelfClosingTag")

    def render(self, out_file, cur_ind=""):
        if self.attrs is None:
            out_file.write("{}<{} />\n".format(cur_ind, self.tag))
        else:
            out_file.write(f"{cur_ind}<{self.tag}")
            for tag, attribute in self.attrs.items():
                out_file.write(f' {tag}="{attribute}"')
            out_file.write(" />\n")


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class Meta(SelfClosingTag):
    tag = "meta"
