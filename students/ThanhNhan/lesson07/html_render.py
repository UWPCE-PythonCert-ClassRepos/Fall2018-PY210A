#!/usr/bin/env python3
import pytest
"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element:
    tag = "html"
    indent = "    "
    def __init__(self, content=None, **kwargs):
       
        if content is None:
            self.contents = []
        else:
            self.contents = [content]
        self.attributes = kwargs
        print("contents is", self.contents)
        print("kwargs ", self.attributes)


    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file, cur_ind=""):   
       # self.indent = cur_ind
        out_file.write(cur_ind + self._open_tag())        
       # out_file.write("<{}>\n".format(self.tag))
        for line in self.contents:
            try:
                line.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write(cur_ind + self.indent + line)
                out_file.write("\n")
        out_file.write(cur_ind + self._close_tag())

    def _open_tag(self):
        open_tag = []
        if (self.attributes is None):
            open_tag.append("<{}>".format(self.tag))
        else:
            open_tag.append("<{}".format(self.tag))
            for key, value in self.attributes.items():       
                open_tag.append(' {}="{}"'.format(key,value))
            open_tag.append(">\n")
        
        return "".join(open_tag)

    def _close_tag(self):
        return "</{}>\n".format(self.tag)
        # out_file.write("just something as a place holder...")

class Html(Element):
    tag = "html"
    
    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + "<!DOCTYPE html>\n")
        super().render(out_file, cur_ind=cur_ind)


class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"

class Ul(Element):
    tag = "ul"

class Li(Element):
    tag = "li"

class OneLineTag(Element):

    def render(self, out_file, cur_ind=""):

        if self.attributes is None:
            out_file.write(cur_ind + "<{}>".format(self.tag))
            out_file.write(self.contents[0])
            out_file.write("</{}>\n".format(self.tag))
        else:
            out_file.write(cur_ind + "<{}".format(self.tag))
            for key, value in self.attributes.items():       
                out_file.write(' {}="{}"'.format(key,value))
            out_file.write(">")
            out_file.write(self.contents[0])
            out_file.write("</{}>\n".format(self.tag))


    def append(self, content):      
        raise NotImplementedError("Cannot add content to OneLineTag")

class Title(OneLineTag):
    tag = "title"

class H(OneLineTag):
    tag = "h"

    def __init__(self, level, content=None, **kwargs):
        self.tag = "h" + str(level)
        super().__init__(content, **kwargs)

class SelfClosingTag(Element):  

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content, **kwargs)
        #Element.__init__(self, content=content, **kwargs)

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")

    # loop through the list of contents:
    def render(self, outfile, cur_ind=""):
        tag = [cur_ind + self._open_tag()]
        for key, value in self.attributes.items():       
            tag.append(' {}="{}"'.format(key,value))
        tag.append(self._close_tag())
        outfile.write("".join(tag))

    def _open_tag(self):
        return "<{}".format(self.tag)
        
    def _close_tag(self):
        return " />\n"

class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"

class Meta(SelfClosingTag):
    tag = "meta"

class A(OneLineTag):
    tag = "a"

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)




