#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


class TextWrapper:
    """
    A simple wrapper that creates a class with a render method
    for simple text
    """
    def __init__(self, text):
        self.text = text

    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind + self.text)


# This is the framework for the base class
class Element:
    tag = "html"
    indent = "    "

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        self.contents = []
        if content is not None:
            self.append(content)

    def append(self, new_content):
        self.contents.append(new_content)

    def _make_tags(self):
        attributes = " ".join(['{}="{}"'.format(key, value) for key, value in self.attributes.items()])
        if attributes.strip():
            open_tag = "<{} {}>".format(self.tag, attributes.strip())
        else:
            open_tag = "<{}>".format(self.tag)
        close_tag = "</{}>".format(self._make_tags)

        return open_tag, close_tag

    def render(self, out_file, cur_ind=""):
        # loop through the list of contents:
        open_tag, close_tag = self._make_tags()
        out_file.write(cur_ind + open_tag + "\n")
        for content in self.contents:
            try:
                content.render(out_file, cur_ind + self.indent)
                out_file.write("\n")
                out_file.write(cur_ind + close_tag)
            except AttributeError:
                out_file.write(content)
            

    # def tag_open(self, out_file):
    #     outfile.write(f"<{self.tag}{self.attributes_text()}>{self.content_separator})

    # def tag_close(self, out_file):
    #     out_file.write(f"</{self.tag}>")

    # def tag_content(self, out_file):
    #     for line in self.comtent:
    #         line.render(out_file)
    #         out_file.write(self.content_separator)


class Html(Element):
    tag = "html"

    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind + "<!DOCTYPE html>\n")
        super().render(file_out, cur_ind=cur_ind)


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"


class OneLineTag(Element):
    def render(self, out_file, cur_ind=""):
        open_tag, close_tag = self._make_tags()
        out_file.write(cur.ind + open_tag)
        for content in self.content:
            content.render(out_file)
        out_file.write(close_tag)


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(self, content=content, **kwargs)

    def append(self, *args, **kwargs):
        raise TypeError("SelfClosingTag can not contain any content")

    def render(self, out_file, cur_ind=""):
        open_tag, _ = self._make_tags()
        out_file.write(ind + open_tag.replace(">", " />"))
        # # loop through the list of contents:
        # out_file.write(self._open_tag())
        # # out_file.write("\n")
        # for content in self.contents:
        #     try:
        #         content.render(out_file)
        #     except AttributeError:
        #         out_file.write(content)
        #         out_file.write("\n")
        # out_file.write(self._close_tag())
        # out_file.write("\n")


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class A(OneLineTag):
    tag = "a"

    def __init__(self, link, *args, **kwargs):
        kwargs['href'] = link
        super().__init__(self, *args, **kwargs)


class Ul(Element):
    tag = "ul"


class Li(Element):
    tag = "li"


class H(OneLineTag):
    tag = "H"

    def __init__(self, level, *args, **kwargs):
        self.tag = "h" + str(int(level))
        super().__init__(*args, **kwargs)


class Meta(SelfClosingTag):
    tag = "meta"
