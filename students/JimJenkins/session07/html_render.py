#!/usr/bin/env python3


class Element:
    """
    class to provide html elements
    """

    def __init__(self, content=None):
        """
        init for element
        :param content: self
        :param content with default none
        """
        if content is None:
            self.content = []
        else:
            self.content = [content]


    def append(self, new_content):
        """
        append method for element
        :param new_content: new content to be added
        :return: appends new content
        """
        self.content.append(new_content)


    def render(self, out_file):
        """
        render the content
        :param out_file: render to an external file
        :return: pipes content to a file

        out_file.write('<{}>\n'.format(self.tag))
        for line in self.content:
            out_file.write(line)
            out_file.write('\n')
        out_file.write('</{}>\n'.format(self.tag))
        """



class Html(Element):
    """
    subclass for html tag for content
    """
    tag = 'html'
    def render(self, file_out, indent=""):
        file_out.write('<!DOCTYPE html>\n')
        Element.render(self, file_out, indent)


class Body(Element):
    """
    subclass for body elements from element
    """
    tag = 'body'


class P(Element):
    """
    subclass for paragraph value from element
    """
    tag = 'p'


class Head(Element):
    """
    subclass for head value from element
    """
    tag = 'head'


class OneLineTag(Element):
    """
    subclass for one line tag value from element
    :return output as a single line
    """
    tag = ''
    def render(self, file_out, indent=""):
        file_out.write('{}<{}{}>{}</{}>\n'.format(indent, self.tag, self.attributes, self.contents[0], self.tag))


class Title(OneLineTag):
    """
    subclass for title from one line tag
    """
    tag = 'title'


class A(OneLineTag):
    """
    subclass for tag a from one line tag
    """
    tag = 'a'
    def __init__(self, html_address, text):
        OneLineTag.__init__(self, text, a=html_address)


class Ul(Element):
    """
    subclass for underline element under element
    """
    tag = 'u1'


class Li(Element):
    """
    subclass for bullets under element
    """
    tag = 'li'


class H(OneLineTag):
    """
    subclass for H tag from one line tag
    """
    def __init__(self, h_counter, header):
        self.tag = u'h' + str(h_counter)
        Element.__init__(self, header)


class SelfClosingTag(Element):
    """
    subclass for closing tag from element
    """
    def render(self, file_out, indent=""):
        file_out.write('{}<{}{} />\n'.format(indent, self.tag, self.attributes))


class Hr(SelfClosingTag):
    """
    subclass for hr closing from self closing tag
    """
    tag = 'hr'


class Br(SelfClosingTag):
    """
    subclass for break from self closing tag
    """
    tag = 'br'


class Meta(SelfClosingTag):
    """
    subclass for meta from self closing tag
    """
    tag = 'meta'


"""
Creating classes
"""

e = Element()
e = Element('hello')
print(e)
