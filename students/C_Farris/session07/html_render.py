#!/usr/bin/env python3

"""
A class-based system for rendering html.
Stuck on kwargs. Need to review that assignment befoer I can complete...
Problem: I am not passing the kwargs correctly. 

"""


# This is the framework for the base class
class Element(object):
    tag = 'html'

    def __init__(self, content=None, **kwargs):
        #self.kwargs = kwargs
        if not content:
            self.contents = []
        else:
            self.contents = [content]

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        #if self.kwargs:
        #    out_file.write('<{}{}>\n'.format(self.tag))
        #else:
        out_file.write('<{}>\n'.format(self.tag))
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write("\n")
        out_file.write('</{}>\n'.format(self.tag))


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
        out_file.write('<{}>'.format(self.tag))
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
        out_file.write('</{}>\n'.format(self.tag))

class Title(OneLineTag):
    tag = 'title'



page = Html()
head = Head()
head.append(Title("PythonClass = Revision 1087:"))
page.append(head)
body = Body()
#body.append(P("is this bold?", style="font-weight:bold"))
body.append(P("Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text"))
body.append(P("And here is another piece of text -- you should be able to add any number"))
page.append(body)
with open("test.html", 'w') as outfile:
    page.render(outfile)
