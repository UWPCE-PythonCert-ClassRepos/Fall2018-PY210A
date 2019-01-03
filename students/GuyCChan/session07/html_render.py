#!/usr/bin/env python3
"""
A class-based system for rendering html.
"""

# This is the framework for the base class
class Element(object):

    tag = "html"
    indent = "    "

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.contents = []
        else:
            self.contents = [content]
        self.attributes = kwargs

    def append(self, new_content):
        self.contents.append(new_content)

    def _open_close_tags(self):
        """ Made open and close tags for all elements."""
        attrs = " ".join(["{}='{}'".format(key, value) for key, value in self.attributes.items()])
        # I really couldn't figure out comletely how to word these lines, particularly the .strip(),
        # and had to resort to plagiarising! But now I think I begin to appreciate how it's done.
        if attrs.strip():
            open_tag = "<{} {}>".format(self.tag, attrs.strip())
        else:
            open_tag = "<{}>".format(self.tag)
        close_tag = "</{}>".format(self.tag)
        return open_tag, close_tag


    def render(self, out_file, cur_ind="", **kwargs):
        open_tag, close_tag = self._open_close_tags()
        # loop through the list of contents.
        out_file.write(cur_ind)
        out_file.write(open_tag + "\n")
        for content in self.contents:
            # Replace "out_file.write(content)" with the next lines as failed test
            # shows 'AttributeError'.
            try:
                content.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write(cur_ind + self.indent)
                out_file.write(content)
                out_file.write("\n")
        out_file.write(cur_ind)
        out_file.write(close_tag)
        out_file.write("\n")

class Html(Element):
    tag = "html"

    def render(self, out_file, cur_ind="", **kwargs):
        out_file.write(cur_ind)
        out_file.write("<!DOCTYPE html>")
        out_file.write("\n")
        Element.render(self, out_file, cur_ind="", **kwargs)


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"


class OneLineTag(Element):
    pass

    def render(self, out_file, cur_ind="", **kwargs):
        open_tag, close_tag = self._open_close_tags()
        out_file.write(cur_ind)
        out_file.write(open_tag)
        out_file.write(self.contents[0])
        out_file.write(close_tag)
        out_file.write("\n")

    def append(self, content):
        """ Cannot add content to OneLineTag."""
        raise NotImplementedError


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag cannot contain any content.")
        super().__init__(content=content, **kwargs)


    def render(self, out_file, cur_ind="", **kwargs):
        # Please explain the use of the underscore in the following line. I tried and tried for hours
        # and over 2 days to get this going but failed. Is it the so called "throwaway" variable?
        # How does it work here? Without it, tests for "hr" would always come back saying "hr" has no
        # attribute 'open_tag'.
        open_tag, _ = self._open_close_tags()
        # This line didn't work for me: tag = self._open_tag()[:-1] + " />\n"
        out_file.write(cur_ind)
        out_file.write(open_tag.replace(">", " />\n"))

    def append(self, *args):
        """ Cannot add content to a SelfClosingTag."""
        raise TypeError("You cannot add content to a SelfClosingTag")

class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class A(OneLineTag):
    tag = "a"

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)


class Li(Element):
    tag = "li"


class Ul(Element):
    tag = "ul"


class H(OneLineTag):
    tag = "h"

    def __init__(self, level, *args, **kwargs):
        # Please explain why the param "content" has to be replaced with *args
        # in order to have it work. Why positional arguments?
        self.tag = "h" + str(level)
        super().__init__(*args, **kwargs)


class Meta(SelfClosingTag):
    tag = "meta"

