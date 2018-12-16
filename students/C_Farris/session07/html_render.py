#!/usr/bin/env python3

"""
A class-based system for rendering html.

Last tags: tag order stored in a list, multiply those tags by the order in the list, then go by that. 
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
        if self.tag == 'html':
            out_file.write('<!DOCTYPE html>\n')
        open_tag = ["<{}".format(self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(' {}="{}"'.format(key, value))
        out_file.write("".join(open_tag))
    def _close_tag(self, out_file):
        out_file.write('</{}>\n'.format(self.tag))

    def render(self, out_file):
        if self.attributes is None:
            out_file.write(self._open_tag())
        else:    
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

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)

    def render(self, out_file):
        tag = self._open_tag(out_file)
        out_file.write("/>\n")

    def append(self, *args):
        raise TypeError("you can\'t append content to a self closing tag")


class Meta(SelfClosingTag):
    tag = 'meta'


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class A(OneLineTag):
    tag = 'a'

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link 
        super().__init__(content, **kwargs)

class UL(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'

class H(OneLineTag):
    """Header Element"""
    def __init__(self, H_level, content=None, **kwargs):
        self.tag = H_level
        self.content = [content]
        super().__init__(content, **kwargs)



