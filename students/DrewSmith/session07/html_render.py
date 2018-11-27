#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element:

    tag = "html"
    content_separator = "\n"
    indent_content = True
    indent = 4

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

    def render(self, out_file, curr_ind=0):
        indent_text = ' ' * curr_ind
        self.tag_open(out_file, indent_text)      
        self.tag_content(out_file, curr_ind)
        self.tag_close(out_file, indent_text)

    def attributes_text(self):
        return "".join((f' {attribute}="{value}"' for attribute, value in self.html_attributes.items()))

    def tag_open(self, out_file, indent_text=''):
        out_file.write(f"{indent_text}<{self.tag}{self.attributes_text()}>{self.content_separator}")
    
    def tag_close(self, out_file, indent_text=''):
        out_file.write(f"{indent_text}</{self.tag}>")
    
    def tag_content(self, out_file, curr_ind=0):
        for line in self.content:
            line.render(out_file, curr_ind + self.indent)
            out_file.write(self.content_separator)

class TextWrapper:
    """
    A simple wrapper that creates a class with a render method
    for simple text
    """
    def __init__(self, text):
        self.text = text

    def render(self, file_out, curr_ind=0):
        file_out.write(f"{' ' * curr_ind}{self.text}")


class Html(Element):
    """
    Top Level HTML element
    """
    tag = "html"

    def render(self, out_file, curr_ind=0):
        out_file.write(f"{' ' * curr_ind}<!DOCTYPE html>\n")
        Element.render(self, out_file, curr_ind)


class Body(Element):
    """
    Body HTML element
    """
    tag = "body"


class P(Element):
    """
    Paragraph <p> HTML element
    """
    tag = "p"


class Head(Element):
    """
    Head HTML element tag
    """
    tag = "head"


class OneLineTag(Element):
    """
    Base class for single line HTML tags
    """
    content_separator = ""
        
    def tag_close(self, out_file, indent_text=''):        
        out_file.write(f"</{self.tag}>")
    
    def tag_content(self, out_file, curr_ind=0):
        for line in self.content:
            line.render(out_file, 0)
            out_file.write(self.content_separator)

class Title(OneLineTag):
    """
    HTML Title element
    """
    tag = "title"


class SelfClosingTag(Element):
    """
    Base class for self closing tags
    """
    content_separator = ""

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("Self closing tags cannot have content")
        Element.__init__(self, **kwargs)

    def append(self, new_content):
        if new_content is not None:
           raise TypeError("Self closing tags cannot have content")

    def render(self, out_file, curr_ind=0):
        """
        Write the self closing tag with attributes
        """
        out_file.write(f"{' ' * curr_ind}<{self.tag}{self.attributes_text()} />")


class Hr(SelfClosingTag):
    """
    HTML Title element
    """
    tag = "hr"


class Br(SelfClosingTag):
    """
    HTML Title element
    """
    tag = "br"


class A(OneLineTag):
    """
    HTML Anchor (A) element
    """
    tag = "a"
    content_separator = ""
    indent_content = False

    def __init__(self, link, content=None, **kwargs):
        kwargs.setdefault("href", link)
        Element.__init__(self, content, **kwargs)


class Ul(Element):
    """
    HTML Unordered List (ul) element
    """
    tag = "ul"


class Li(Element):
    """
    HTML List Item (li) element
    """
    tag = "li"


class H(OneLineTag):
    """
    HTML Header (h1, h2, h3, h4, and h5) elements
    """
    tag = "h"

    def __init__(self, level, content=None, **kwargs):
        if 1 > level > 5:
            raise TypeError("Header must be between 1 and 5")
        self.tag = f"h{level:d}"
        Element.__init__(self, content, **kwargs)


class Meta(SelfClosingTag):
    """
    HTML Meta element
    """
    tag = "meta"


class Input(Element):
    """
    HTML Input element
    """
    tag = "input"
