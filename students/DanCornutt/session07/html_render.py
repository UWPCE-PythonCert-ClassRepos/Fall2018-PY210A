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


    def _open_tag(self):
        open_tag = ["<{}".format(self.tag)]
        for key, value in self.tag_attributes.items():
            open_tag.append(' {}="{}"'.format(key, value))
        open_tag.append(">")
        return "".join(open_tag)


    def _close_tag(self):
        return "</{}>".format(self.tag)


    def append(self, new_content):
        self.contents.append(new_content)


    def render(self, out_file):
        out_file.write(self._open_tag())
        out_file.write("\n")
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
                out_file.write("\n")

        out_file.write(self._close_tag())
        out_file.write("\n")


class Html(Element):
    tag = "html"
    doc = "<!DOCTYPE html>\n"

    def render(self,out_file):
        out_file.write(self.doc)
        super().render(out_file)

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"

class OneLineTag(Element):
    def render(self, out_file):
        out_file.write(self._open_tag())
        out_file.write(self.contents[0])
        out_file.write(self._close_tag())


    def append(self, content):
        raise NotImplementedError

class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def render(self, outfile):
        tag = self._open_tag()[:-1] + " />\n"
        outfile.write(tag)


    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class A(OneLineTag):
    tag = 'a'

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)


class H(OneLineTag):
    def __init__(self, level, content=None, **kwargs):
        self.tag = "h" + str(level)
        super().__init__(content, **kwargs)


class Ul(Element):
    tag = "ul"


class Li(Element):
    tag = "li"


class Meta(SelfClosingTag):
    tag = "meta"
