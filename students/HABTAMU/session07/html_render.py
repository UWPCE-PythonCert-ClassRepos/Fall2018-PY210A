#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""

# This is the framework for the base class
class Element(object):

    tag = "html"
    indent = "  "
    # html_attributes = {"pid": "intro", "style": "text-align: center", "width":"400"}
    html_attributes = dict()

    def __init__(self, content=None, **kwargs):
        self.html_attributes = kwargs

        if content is None:
            self.contents = []
        else:
            self.contents = [content]
        # print("contents is:", self.contents)


    def append(self, new_content):
        self.contents.append(new_content)
        
    def render(self, out_file, ind=""):
        # loop through the list of contents
        attribute_str = "".join([f' {attribute}="{value}"' for attribute,value in self.html_attributes.items()])
        out_file.write(ind + "<{}{}>\n".format(self.tag,attribute_str))
        for content in self.contents:
            # Duck Typing on the Fly
            try:
                content.render(out_file, ind + "  ")
            except AttributeError:
                out_file.write(ind + "  " + str(content))
            out_file.write('\n')
        out_file.write(ind + "</{}>".format(self.tag))


class Html(Element):
    tag = 'html'

    def render(self, out_file, ind=""):
        out_file.write(ind + "<!DOCTYPE html>\n")
        super(Html,self).render(out_file, ind)

class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'

class SelfClosingTag(Element):
    # tag = 'hr'
    
    def render(self, out_file, ind=""):
        # render self closing tags with attributes to out_file
        attribute_str = "".join([f' {attribute}="{value}"' for attribute, value in self.html_attributes.items()])
        out_file.write(ind + "<{}{} />".format(self.tag, attribute_str))


class Hr(SelfClosingTag):
    tag = 'hr'


class Br(SelfClosingTag):
    tag = 'br'

class Meta(SelfClosingTag):
    tag = 'meta'

class OneLineTag(Element):

    # def append(self, content):
    #     if isinstance(content, OneLineTag) or type(content) is str:
    #         self.contents.append(content)
    #     else:
    #         raise ValueError(f"You can only append an instance of OneLineTag or a string to tag '{self.tag}'.")

    def append(self, content):
        raise NotImplementedError

    def render(self, out_file, ind=""):
        attribute_str = "".join([f' {attribute}="{value}"' for attribute, value in self.html_attributes.items()])
        out_file.write(ind + "<{}{}>".format(self.tag, attribute_str))
        for content in self.contents:
            # determine type of an object if it is Element?
            if isinstance(content, OneLineTag):
                content.render(out_file)
            else:
                out_file.write(content)
                # out_file.write('\n')
        out_file.write("</{}>".format(self.tag))

class A(OneLineTag):
    tag = 'a'
    def __init__(self, link, content):
        super(A, self).__init__(content, href=link)


class H(Element):
    tag = 'h'
    def __init__(self, level, content=None, **kwargs):
        self.tag = self.tag + str(level)
        super(H,self).__init__(content,**kwargs)

class Ul(Element):
    tag = 'UL'

class Li(OneLineTag):
    tag = 'li'
    def append(self, content):
        if isinstance(content, OneLineTag) or type(content) is str:
            self.contents.append(content)
        else:
            raise ValueError(
                f"You can only append an instance of OneLineTag or a string to tag '{self.tag}'.")

class Title(OneLineTag):
    tag = 'title'
