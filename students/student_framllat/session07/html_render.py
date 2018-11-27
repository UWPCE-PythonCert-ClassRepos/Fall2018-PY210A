#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element:

    tag = "html"
    
    def __init__(self, contents=None, **kwargs):
    	if contents is None:
    		self.contents = []
    	else:
            self.contents = [contents]


    def append(self, new_content):
        self.contents.append(new_content)


    def render(self, out_file):
        # Loop thru list of contents
        for content in self.contents:
            out_file.write("<{}>\n".format(self.tag))
            # for key, value in self.attributes:
            #     open_tag = ["<{}".format(self.tag)]
            #     open_tag.append(">\n")
            #     out_file.write("".join(open_tag))

            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
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
    def render(self, out_file):
            out_file.write("<{}>".format(self.tag))
            out_file.write(self.contents[0])
            out_file.write("</{}>\n".format(self.tag))

            # open_tag = ["<{}".format(self.tag)]
            # open_tag.append(">\n")
            # out_file.write("".join(open_tag))


    def append(self, content):
        raise NotImplementedError


class Title(OneLineTag):
    tag = "title"





