"""
Python210A Vincent Aquila  Fall2018
using Python 3.7.0
Session 07 - HTML Renderer
"""

# A class-based system for rendering html. 


# This is the framework for the base class
class Element(object):
    
    
    tag = "html"
    
    """
    We need a way to store the content: both what gets passed into the 
    __init__ and what gets added with the append method. We need a data
    structure that can hold an ordered list of things, and can be added
    to in the future - list.
    """
    def __init__(self, content=None, **kwargs):  
        # note to self - never have a default parameter be a list []
        self.contents = [content]
        #print("contents is:", self.contents)
        if content is None:
            self.content = []
        else:
            self.content = [content]
       

    """
    Note to self - def append() is a method, that can add another string 
    to the content; it is a way for the class Element to store the content 
    in a way where more can be added to it.
    """
    def append(self, new_content):
        self.contents.append(new_content)
        

    def render(self, out_file):
        # loop through the list of contents:
        for content in self.contents:
            out_file.write("<{}>\n".format(self.tag))
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)    
            #out_file.write("\n")
            out_file.write("</{}>\n".format(self.tag))
            

# 'subclassing'
class Html(Element):
	tag = "html"


class Body(Element):
	tag = "body"
    
    
class P(Element):
    tag = "paragraph"


class Head(Element):
    tag = "head"


class OneLineTag(Element):
    

    def render(self, out_file):
        """
        out_file.write("<{}>\n".format(self.tag))
        out_file.write(self.contents[0])
        out_file.write("</{}>\n".format(self.tag))
        """
        # loop through the list of contents:
        open_tag = ["<{}".format(self.tag)]
        open_tag.append(">\n")
        out_file.write("".join(open_tag))


class Title(OneLineTag):
    tag = "title"   










