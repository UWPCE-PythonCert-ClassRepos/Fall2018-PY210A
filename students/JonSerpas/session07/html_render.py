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
            self.contents = [content]  # created a list with content
        print("contents is :", self.contents)
        self.attributes = kwargs

    def append(self, new_content):
        self.contents.append(new_content)

    def _open_tag(self):
        open_tag = [("<{}".format(self.tag))]
        for key, value in self.attributes.items():
            open_tag.append(' {}="{}"'.format(key, value))
        open_tag.append(">")
        return "".join(open_tag)

    def render(self, out_file):
        # loop through the list of contents:
        # open_tag = [("<{}".format(self.tag))]
        # for key, value in self.attributes.items():
        #     open_tag.append(' {}="{}"'.format(key, value))
        # open_tag.append(">\n")
        open_tag = self._open_tag()
        out_file.write(open_tag + '\n')
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write("\n")
        out_file.write("</{}>\n".format(self.tag))


class Html(Element):
    tag = 'html'


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):
    def render(self, out_file):
        out_file.write("<{}>".format(self.tag))
        out_file.write(self.contents[0])
        out_file.write("</{}>\n".format(self.tag))
        

    def append(self, new_content):
        raise NotImplementedError
        self.contents.append(new_content)


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def render(self, out_file):
        # loop through the list of contents:
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

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")


class Hr(SelfClosingTag):
    tag = 'hr'

    def render(self, out_file):
        tag = self._open_tag()[:-1] + " />\n"
        out_file.write(tag)


class Br(SelfClosingTag):
    tag = 'br'

    def render(self, out_file):
        tag = self._open_tag()[:-1] + " />\n"
        out_file.write(tag)


class A(OneLineTag):

    tag = 'a'

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)















