#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element:

    tag = "html"

    def __init__(self, content=None, **kwargs):

        self.attributes = kwargs

        if content is None:
            self.content = []
        else:
            self.content = [content]

    def append(self, new_content):
        self.content.append(new_content)

    def _open_tag(self):
        tag = ["<{}".format(self.tag)]
        if self.attributes:
            tag.append(" ")
            for key, value in self.attributes.items():
                tag.append(key + "=" + '"' + value + '"')

        tag.append(">")
        return "".join(tag)

    def _close_tag(self):
        return f"</{self.tag}>"

    def render(self, out_file):
        out_file.write(self._open_tag())
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


class OneLineTag(Element):
    # def append(self, content):
    #     if self.content:
    #         super().append(content)

    def render(self, out_file):
        out_file.write(self._open_tag())
        out_file.write(self.content[0])
        out_file.write(self._close_tag())
        out_file.write("\n")


class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def render(self, out_file):
        out_file.write("<{}>".format(self.tag))
        out_file.write(self.content[0])
        out_file.write("</{}>".format(self.tag))

    def append(self, content):
        raise TypeError


class Title(OneLineTag):
    tag = "title"


class Br(SelfClosingTag):
    tag = "br"

    def render(self, out_file):
        open_tag = ["<{}".format(self.tag)]

        if self.attributes:
            open_tag.append(" ")
        for key, value in self.attributes.items():
            open_tag.append(key + "=" + '"' + str(value) + '"')

        open_tag.append(" />\n")

        out_file.write("".join(open_tag))


class Hr(SelfClosingTag):
    tag = "hr"

    def render(self, out_file):
        open_tag = ["<{}".format(self.tag)]

        if self.attributes:
            open_tag.append(" ")
        for key, value in self.attributes.items():
            open_tag.append(key + "=" + '"' + str(value) + '"')

        open_tag.append(" />\n")

        out_file.write("".join(open_tag))


class A(OneLineTag):
    tag = 'a'

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)