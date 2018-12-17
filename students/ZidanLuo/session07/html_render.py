#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element:
    
    tag = "html"
    indent = "    "
    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        if content is None:
            self.content = []
        else:
            self.content = [content]


    def append(self, new_content):
        self.content.append(new_content)


    def render(self, out_file, cur_ind=""):
        
        # create open tag markdown <tag_name at1: val1, at2: val2>
        out_file.write(cur_ind)
        out_file.write(self._open_tag())
        out_file.write("\n")
        # iterate over contents, and call render for each sub-element.
        # sample output should look like:
        # <tag1 at_1: val_1, at_2: val_2>
        #   <tag2 at2_1: val2_1>
        #   ........
        #   </tag2>
        for line in self.content:
            try:
                line.render(out_file,cur_ind+self.indent)
            except AttributeError:
                out_file.write(cur_ind+self.indent)
                out_file.write(line)
                out_file.write("\n")
        # close supreme tag
        out_file.write(cur_ind)
        out_file.write(self._close_tag())
        out_file.write("\n")

    def _open_tag(self):
        open_tag = ["<{}".format(self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(" "+str(key)+"="+ "\"" + str(value) + "\",")
        if(open_tag[-1][-1] == ','):
            open_tag[-1] = open_tag[-1][:-1]
        open_tag.append(">")
        return "".join(open_tag)

    def _close_tag(self):
        return "</{}>".format(self.tag)


class Html(Element):
    tag = "html"
    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + "<!DOCTYPE html>\n")
        out_file.write(self._open_tag())
        out_file.write("\n")
        for line in self.content:
            try:
                line.render(out_file, cur_ind+self.indent)
            except AttributeError:
                out_file.write(line)
                out_file.write("\n")
        # close supreme tag
        out_file.write(cur_ind)
        out_file.write(self._close_tag())
        out_file.write("\n")


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
        out_file.write(cur_ind)
        out_file.write(self._open_tag())
        out_file.write(self.content[0])
        out_file.write(self._close_tag())
        out_file.write("\n")

    def append(self, new_content):
        raise NotImplementedError

class H(OneLineTag):
    def __init__(self, level, content=None, **kwargs):
        self.tag = "h"+str(level)
        super().__init__(content, **kwargs)


class A(OneLineTag):
    tag = "a"

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):
    '''
        Selfclosing tags does not take in contents
    '''
    def render(self, out_file, ind=""):
        out_file.write(ind)
        tag=self._open_tag()[:-1]+ " />\n"
        out_file.write(tag)
    # Raise Exception when a selfclosing tags trying to take in content
    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")


    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)
    pass


class Meta(SelfClosingTag):
    tag = "meta"


class Hr(SelfClosingTag):
    tag = "hr"

    # def render(self, out_file):
    #     out_file.write(self._open_tag())
    #     out_file.write("\n")
    #     for c in self.ccontent:
    #         try

class Br(SelfClosingTag):
    tag = "br"