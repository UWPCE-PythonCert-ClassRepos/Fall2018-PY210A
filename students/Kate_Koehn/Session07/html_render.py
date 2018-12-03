#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""

class Element:

    tag = "html"

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.content = []
        else:
            self.content = [content]
        self.attributes = kwargs

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, out_file):
        open_tag = ["<{}".format(self.tag)]
        print(self.attributes)
        for key, value in self.attributes.items():
            open_tag.append(' {}="{}"'.format(key, value))

        open_tag.append(">\n")
        out_file.write("".join(open_tag))
        for line in self.content:
            try:
                line.render(out_file)
            except AttributeError:
                out_file.write(line)
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


class OneLineTag(Element):

    def append(self, content):
        raise NotImplementedError

    def render(self, out_file):
        out_file.write("<{}>".format(self.tag))
        out_file.write(self.content[0])
        out_file.write("</{}>\n".format(self.tag))


class Title(OneLineTag):
    tag = "title"