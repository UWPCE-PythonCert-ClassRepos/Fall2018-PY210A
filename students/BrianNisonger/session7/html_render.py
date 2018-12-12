"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element:
    tag = "html"
    indent = "    "

    def __init__(self, content=None, **kwargs):
        if content == None:
            self.content = []
        else:
            self.content = [content]
        self.kwargs = kwargs

    def append(self, new_content):
        self.content.append(new_content)

    def _open_tag(self, indent=indent):
        open_tag = f'<{self.tag}'
        for attributes in self.kwargs:
            open_tag = open_tag + (
                f' {attributes}="{self.kwargs[attributes]}"')
        open_tag = open_tag + (">\n")
        return open_tag

    def _close_tag(self):
        close_tag = f'</{self.tag}>'
        return close_tag

    def render(self, out_file, cur_indent=""):
        # self.indent = indent
        out_file.write(cur_indent)
        out_file.write(self._open_tag())
        for content in self.content:
            if content is not None:
                try:
                    content.render(out_file, cur_indent + self.indent)
                except AttributeError:
                    out_file.write(cur_indent + self.indent)
                    out_file.write(content.strip())
                out_file.write("\n")
        out_file.write(cur_indent)
        out_file.write(self._close_tag())


class Html(Element):
    tag = "html"

    def render(self, out_file, indent=""):
        out_file.write("<!DOCTYPE html>\n")
        super().render(out_file, indent)


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"


class OneLineTag(Element):
    indent = ""

    def append(self, new_content):
        self.content.append(f' {new_content}')

    def _open_tag(self):
        open_tag = f'<{self.tag}'
        for attributes in self.kwargs:
            open_tag = open_tag + (
                f' {attributes}="{self.kwargs[attributes]}"')
        open_tag = open_tag + (">")
        return open_tag

    def _close_tag(self):
        close_tag = f'</{self.tag}>'
        return close_tag

    def render(self, out_file, cur_indent=""):
        #self.indent = indent
        out_file.write(cur_indent)
        out_file.write(self._open_tag())
        for content in self.content:
            if content != None:
                try:
                    content.render(out_file,cur_indent+self.indent)
                except AttributeError:
                    out_file.write(content)
        out_file.write(self._close_tag())


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def _open_tag(self):
        open_tag = f'<{self.tag}'
        for attributes in self.kwargs:
            open_tag = open_tag + (
                f' {attributes}="{self.kwargs[attributes]}"')
        return open_tag

    def _close_tag(self):
        close_tag = f' />'
        return close_tag

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")

    def render(self, out_file, cur_indent=""):
        # self.indent = indent
        out_file.write(cur_indent)
        out_file.write(self._open_tag())
        for content in self.content:
            if content is not None:
                try:
                    content.render(out_file, cur_indent + self.indent)
                except AttributeError:
                    out_file.write(cur_indent + self.indent)
                    out_file.write(content.strip())
                out_file.write("\n")
        out_file.write(self._close_tag())

class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class Meta(SelfClosingTag):
    tag = "meta"
    indent = ""


class A(OneLineTag):
    tag = "a"

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)


class H(OneLineTag):
    tag = "h"

    def __init__(self, level, content=None, **kwargs):
        super().__init__(content, **kwargs)
        self.level = level

    def _open_tag(self):
        open_tag = f'<{self.tag}{self.level}'
        for attributes in self.kwargs:
            open_tag = open_tag + (
                f' {attributes}="{self.kwargs[attributes]}"')
        open_tag = open_tag + (">")
        return open_tag

    def _close_tag(self):
        close_tag = f'</{self.tag}{self.level}>'
        return close_tag


class Ul(Element):
    tag = "ul"


class Li(Element):
    tag = "li"
