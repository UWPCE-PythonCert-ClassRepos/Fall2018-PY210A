#!/usr/bin/env python3

"""
A class-based system for rendering html.

On Step 5. I refactored and the code renders correctly.
I need to add the tests to the test module before I go on to 6
"""


# This is the framework for the base class
class Element(object):
    tag = 'html'

    def __init__(self, content=None, **kwargs):

        self.attributes = kwargs

        if not content:
            self.contents = []
        else:
            self.contents = [content]

    def append(self, new_content):
        self.contents.append(new_content)

    def _open_tag(self, out_file):
        open_tag = ["<{}".format(self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(' {}="{}"'.format(key, value))
        out_file.write("".join(open_tag))

    def _close_tag(self, out_file):
        out_file.write('</{}>\n'.format(self.tag))

    def render(self, out_file):
        self._open_tag(out_file)
        out_file.write(">\n")
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write("\n")
        self._close_tag(out_file)


class Html(Element):
    tag = "html"


class Body(Element):
    tag = 'body'


class P(Element):
    tag = "p"


class Head(Element):
    tag = 'head'


class OneLineTag(Element):

    def render(self, out_file):
        self._open_tag(out_file)
        out_file.write(">")
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
        self._close_tag(out_file)


class Title(OneLineTag):
    tag = 'title'


class SelfClosingTag(Element):

    def render(self, out_file):
        self._open_tag(out_file)
        out_file.write("/>")


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"



page = Html()
head = Head()
head.append(Title("PythonClass = Revision 1087:" , style="font-weight:bold"))
page.append(head)
body = Body()
body.append(Hr(style="font-weight:bold", id="intro"))
body.append(Br(style="font-weight:bold", id="intro"))
body.append(P("is this bold?", style="font-weight:bold", id="intro"))
body.append(P("Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text"))
body.append(P("And here is another piece of text -- you should be able to add any number"))
page.append(body)
with open("test.html", 'w') as outfile:
    page.render(outfile)
