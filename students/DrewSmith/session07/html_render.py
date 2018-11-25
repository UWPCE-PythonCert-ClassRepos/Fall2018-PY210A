#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element:

    tag = "html"
    content_separator = "\n"

    def __init__(self, content=None, **kwargs):
        self.content = []
        self.html_attributes = kwargs
        if content is not None:
            self.append(content)

    def append(self, new_content):
        if hasattr(new_content, 'render'):
            self.content.append(new_content)
        else:
            self.content.append(TextWrapper(str(new_content)))

    def render(self, out_file):
        self.tag_open(out_file)      
        self.tag_content(out_file)
        self.tag_close(out_file)
        #out_file.write(f"{self.tag_open()}{self.tag_content()}{self.tag_close()}")
        # out_file.write("{}".format(self.render_tag_open()))
        # out_file.write(self.content_separator.join())
        # for line in self.content:
        #     line.render(out_file)
        #     out_file.write("\n")
        # out_file.write(self.render_tag_close())

    def attributes_text(self):
        return "".join((f" {attribute}='{value}'" for attribute, value in self.html_attributes.items()))

    def tag_open(self, out_file):
        out_file.write(f"<{self.tag}{self.attributes_text()}>\n")
    
    def tag_close(self, out_file):
        out_file.write(f"</{self.tag}>")
    
    def tag_content(self, out_file):
        for line in self.content:
            line.render(out_file)
            out_file.write(self.content_separator)

class TextWrapper:
    """
    A simple wrapper that creates a class with a render method
    for simple text
    """
    def __init__(self, text):
        self.text = text

    def render(self, file_out):
        file_out.write(self.text)


class Html(Element):
    tag = "html"


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"


class OneLineTag(Element):
    content_separator = ""

    def tag_open(self, out_file):
        out_file.write(f"<{self.tag}{self.attributes_text()}>")

class Title(OneLineTag):
    tag = "title"

