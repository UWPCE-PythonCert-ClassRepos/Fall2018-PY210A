"""
test code for html_render.py

This is just a start -- you will need more tests!
"""

import io
import pytest
import collections

# import * is often bad form, but makes some sense for testing.
from html_render import *


# utility function for testing render methods
# needs to be used in multiple tests, so we write it once here.
def render_result(element, indent=0):
# def render_result(element):
    """
    calls the element's render method, and returns what got rendered as a
    string
    """
    # the StringIO object is a "file-like" object -- something that
    # provides the methods of a file, but keeps everything in memory
    # so it can be used to test code that writes to a file, without
    # having to actually write to disk.
    outfile = io.StringIO()
    element.render(outfile, indent=indent)
    # element.render(outfile)
    return outfile.getvalue()

########
# Step 1
########

def test_init():
    """
    This only tests that it can be initialized with and without
    some content -- but it's a start
    """
    e = Element()

    e = Element("this is some text")


def test_append():
    """
    This tests that you can append text

    It doesn't test if it works --
    that will be covered by the render test later
    """
    e = Element("this is some text")
    e.append("some more text")


def test_render_element():
    """
    Tests whether the Element can render two pieces of text
    So it is also testing that the append method works correctly.

    It is not testing whether indentation or line feeds are correct.
    """
    e = Element("this is some text")
    e.append(" and this is some more text")

    # This uses the render_results utility above
    file_contents = render_result(e).strip()
    file_contents_count = collections.Counter(file_contents.split())
    print(file_contents)

    # making sure the content got in there.
    assert("this is some text") in file_contents
    assert(" and this is some more text") in file_contents

    # make sure it's in the right order
    assert file_contents.index("this is") < file_contents.index("and this")

    # making sure the opening and closing tags are right.
    assert file_contents.startswith("<html>")
    assert file_contents.endswith("</html>")
    assert file_contents_count.get('<html>') == 1
    assert file_contents_count.get('</html>') == 1




########
# Step 2
########


# tests for the new tags
def test_html():
    e = Html("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e).strip()

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents
    assert file_contents.endswith("</html>")


def test_body():
    e = Body("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e).strip()

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents

    assert file_contents.startswith("<body>")
    assert file_contents.endswith("</body>")


def test_p():
    e = P("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e).strip()

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents

    assert file_contents.startswith("<p>")
    assert file_contents.endswith("</p>")


def test_sub_element():
    """
    tests that you can add another element and still render properly
    """
    page = Html()
    page.append("some plain text.")
    page.append("some 2 plain text.")
    page_body = Body()
    page_body.append(P("A simple paragraph of text"))
    page_body.append(P("Another simple paragraph of text"))
    page.append(page_body)
    page.append("Some more plain text.")
    file_contents = render_result(page)
    print(file_contents) # so we can see it if the test fails

    # note: The previous tests should make sure that the tags are getting
    #       properly rendered, so we don't need to test that here.
    assert "some plain text" in file_contents
    assert "A simple paragraph of text" in file_contents
    assert "Some more plain text." in file_contents
    assert "some plain text" in file_contents
    # but make sure the embedded element's tags get rendered!
    assert "<p>" in file_contents
    assert "</p>" in file_contents
    assert "<body>" in file_contents
    assert "</body>" in file_contents
    #assert False


# #####################
# # indentation testing
# #####################


def test_indent():
    """
    Tests that the indentation gets passed through to the renderer
    """
    html = Html("some content")
    file_contents = render_result(html, indent=3)

    print(file_contents)
    lines = file_contents.split("\n")
    assert lines[1].startswith("   <")
    assert lines[-2].startswith("   <")


def test_indent_contents():
    """
    The contents in a element should be indented more than the tag
    by the amount in the indent class attribute
    """
    html = Element("some content")
    file_contents = render_result(html, indent=0)

    print(file_contents)
    lines = file_contents.split("\n")
    assert lines[1].startswith(f'{" "*Element.ind}')


# def test_multiple_indent():
#     """
#     make sure multiple levels get indented fully
#     """
#     body = Body()
#     body.append(P("some text"))
#     html = Html(body)
#
#     file_contents = render_result(html)
#
#     print(file_contents)
#     lines = file_contents.split("\n")
#     print(lines)
#     for i in range(3):  # this needed to be adapted to the <DOCTYPE> tag
#         assert lines[i + 1].startswith(i * f'{" "*Element.ind}' + "<")
#
#     assert lines[4].startswith(3 * f'{" "*Element.ind}' + "some")

# this is for testing indenting -- we'll wait 'till we get to that
def test_element_indent1():
    """
    Tests whether the Element indents at least simple content

    we are expecting to to look like this:

    <html>
        this is some text
    <\html>

    More complex indentation should be tested later.
    """
    e = Element("this is some text")

    # This uses the render_results utility above
    file_contents = render_result(e).strip()

    # making sure the content got in there.
    assert("this is some text") in file_contents

    # break into lines to check indentation
    lines = file_contents.split('\n')
    # making sure the opening and closing tags are right.
    assert lines[0] == "<html>"
    # this line should be indented by the amount specified
    # by the class attribute: "indent"
    assert lines[1].startswith(f'{" "*(Element.ind+4)}' + "thi")
    assert lines[2] == "</html>"
    assert file_contents.endswith("</html>")


########
# Step 3
########

def test_sub_element_more():
    """
    tests that you can add another element and still render properly
    """
    page = Html()
    page.append("some plain text.")
    page.append("some 2 plain text.")
    page_head = Head()
    page_title = Title(" PythonClass - Session 7 example ")
    #page_title.append("PythonClass - Session 7 example")
    page_head.append(page_title)
    page.append(page_head)

    file_contents = render_result(page)
    print(file_contents) # so we can see it if the test fails

    # note: The previous tests should make sure that the tags are getting
    #       properly rendered, so we don't need to test that here.
    assert "<title> PythonClass - Session 7 example </title>" in file_contents
    # assert "A simple paragraph of text" in file_contents
    # assert "Some more plain text." in file_contents
    # assert "some plain text" in file_contents
    # but make sure the embedded element's tags get rendered!
    assert "<head>" in file_contents
    assert "</head>" in file_contents
    assert "<title>" in file_contents
    assert "</title>" in file_contents
    #assert False

########
# Step 4
########

def test_sub_element_attrs():
    """
    tests that you can add another element and still render properly
    """
    page = Html()
    page.append("some plain text.")
    page.append("some 2 plain text.")
    page_body = Body()
    page_body.append(P("A simple paragraph of text", \
    style="text-align: center; font-style: oblique;"))
    page_body.append(P("Another simple paragraph of text"))
    page.append(page_body)
    page.append("Some more plain text.")
    file_contents = render_result(page)
    print(file_contents) # so we can see it if the test fails

    # note: The previous tests should make sure that the tags are getting
    #       properly rendered, so we don't need to test that here.
    assert "some plain text" in file_contents
    assert "A simple paragraph of text" in file_contents
    assert "Some more plain text." in file_contents
    assert "some plain text" in file_contents
    # but make sure the embedded element's tags get rendered!
    assert '<p style="text-align: center; font-style: oblique;">' in file_contents
    assert "</p>" in file_contents
    #assert False

########
# Step 5
########

def test_self_closing_attrs():
    """
    tests that you can add self closing tag and still render properly
    """
    page = Html()
    page.append("some plain text.")
    page.append("some 2 plain text.")
    page_body = Body()
    page_body.append(P("A simple paragraph of text", \
    style="text-align: center; font-style: oblique;"))
    page_body.append(P("Another simple paragraph of text"))
    page_hr = Hr()
    page_body.append(page_hr)
    page.append(page_body)
    page.append("Some more plain text.")
    file_contents = render_result(page)
    print(file_contents) # so we can see it if the test fails

    # note: The previous tests should make sure that the tags are getting
    #       properly rendered, so we don't need to test that here.
    assert "some plain text" in file_contents
    assert "A simple paragraph of text" in file_contents
    assert "Some more plain text." in file_contents
    assert "some plain text" in file_contents
    # but make sure the embedded element's tags get rendered!
    assert '<p style="text-align: center; font-style: oblique;">' in file_contents
    assert "</p>" in file_contents
    assert "<hr />" in file_contents
    #assert False

########
# Step 7
########

def test_list_headers():
    """
    tests that you can add one-line tag with content and keywords (attrs)
    """
    page = Html()
    page.append("some plain text.")
    page.append("some 2 plain text.")
    page_body = Body()
    page_body.append(P("A simple paragraph of text", \
    style="text-align: center; font-style: oblique;"))
    page_body.append(P("Another simple paragraph of text"))
    page_hr = Hr()
    page_body.append(page_hr)
    page.append(page_body)
    page.append("Some more plain text.")
    page_a = A("http://google.com", "link to google")
    page_u_list = Ul(id="TheList", style="line-height:200%")
    page_list_item = Li('The first item in a list')
    page_list_item_2 = Li('This is the second item', style="color: red")
    page_header = H(2, "PythonClass - Class 6 example")
    page_u_list.append(page_list_item)
    page_u_list.append(page_list_item_2)
    page_body.append(page_u_list)
    page_body.append(page_header)
    file_contents = render_result(page)
    print(page.content)
    print(file_contents) # so we can see it if the test fails

    # note: The previous tests should make sure that the tags are getting
    #       properly rendered, so we don't need to test that here.
    assert "some plain text" in file_contents
    assert "A simple paragraph of text" in file_contents
    assert "Some more plain text." in file_contents
    assert "some plain text" in file_contents
    # but make sure the embedded element's tags get rendered!
    assert '<p style="text-align: center; font-style: oblique;">' in file_contents
    assert "</p>" in file_contents
    assert "<hr />" in file_contents
    # assert '''
    #         <hr />
    #         <ul id="TheList" style="line-height:200%">
    #             <li>
    #             The first item in a list
    #             </li>
    #             <li style="color: red">
    #             This is the second item
    #             </li>
    #         </ul>''' in file_contents
    assert '<h2>PythonClass - Class 6 example</h2>' in file_contents
    #assert False

########
# Step 8
########

def test_doctype_meta():
    """
    tests that you can add one-line tag with content and keywords (attrs)
    """
    page = Html()
    page_head = Head()
    page_meta = Meta(charset="UTF-8")
    page_head.append(page_meta)
    page.append(page_head)
    page_body = Body()
    # page_body.append(P("A simple paragraph of text", \
    # style="text-align: center; font-style: oblique;"))
    page_body.append(P("Another simple paragraph of text"))
    # page_hr = Hr()
    # page_body.append(page_hr)
    page.append(page_body)
    page.append("Some more plain text.")
    file_contents = render_result(page)
    print(file_contents) # so we can see it if the test fails
    # note: The previous tests should make sure that the tags are getting
    #       properly rendered, so we don't need to test that here.
    assert '<meta charset="UTF-8" />' in file_contents
    assert file_contents.index('<meta charset="UTF-8" />') > file_contents.index('<head>')
    assert '\n\n' not in file_contents