"""
test code for html_render.py

This is just a start -- you will need more tests!
"""

import io
import pytest

# import * is often bad form, but makes it easier to test everything in a module.
from html_render import *


# utility function for testing render methods
# needs to be used in multiple tests, so we write it once here.
def render_result(element, ind=0):
    """
    calls the element's render method, and returns what got rendered as a
    string
    """
    # the StringIO object is a "file-like" object -- something that
    # provides the methods of a file, but keeps everything in memory
    # so it can be used to test code that writes to a file, without
    # having to actually write to disk.
    outfile = io.StringIO()
    # this so the tests will work before we tackle indentation
    if ind:
        element.render(outfile, ind)
    else:
        element.render(outfile)
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
    e.append("and this is some more text")

    # This uses the render_results utility above
    file_contents = render_result(e).strip()

    # making sure the content got in there.
    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents

    # make sure it's in the right order
    assert file_contents.index("this is") < file_contents.index("and this")

    # making sure the opening and closing tags are right.
    assert file_contents.startswith("<html>")
    assert file_contents.endswith("</html>")

# # Uncomment this one after you get the one above to pass
# # Does it pass right away?
def test_render_element2():
    """
    Tests whether the Element can render two pieces of text
    So it is also testing that the append method works correctly.

    It is not testing whether indentation or line feeds are correct.
    """
    e = Element()
    e.append("this is some text")
    e.append("and this is some more text")

    # This uses the render_results utility above
    file_contents = render_result(e).strip()

    # making sure the content got in there.
    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents

    # make sure it's in the right order
    assert file_contents.index("this is") < file_contents.index("and this")

    # making sure the opening and closing tags are right.
    assert file_contents.startswith("<html>")
    assert file_contents.endswith("</html>")



# # ########
# # # Step 2
# # ########

# # tests for the new tags
def test_html():
    e = Html("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e).strip()

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents
    print(file_contents)
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
    page.append(P("A simple paragraph of text"))
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




########
# Step 3
########

def test_element_OneLineTag():
    """
    Tests that creating a one line Title tag renders appropriately
    """
    page = Html()
    title = Title("some title text")
    title_contents = render_result(title)
    # Verify standard rendered text
    assert title_contents.startswith("<title>")
    assert title_contents.endswith("</title>")
    assert "some title text" in title_contents
    # Make sure there are no new lines
    assert "\n" not in title_contents

    page.append(title)
    assert title_contents in render_result(page)

########
# Step 4
########

def test_attributes():
    """
    Tests that HTML attributes are rendered correctly
    """
    attributes = {'id':'p_test', 'class':'cssClass'}
    p = P("some text", **attributes)
    p_contents = render_result(p)
    for attribute in attributes.items():
        assert f'{attribute[0]}="{attribute[1]}"' in p_contents

########
# Step 5
########
def test_self_closing_tag_hr():
    """
    Tests Hr self closing tag
    """
    hr = Hr()
    contents = render_result(hr)
    assert contents == "<hr />"

    hr = Hr(width=50)
    contents = render_result(hr)
    assert contents == '<hr width="50" />'
    

def test_self_closing_tag_hr_content_error():
    """
    Tests Hr self closing tag Type error for content
    """
    hr = Hr()
    with pytest.raises(TypeError):
        hr.append("Some Text")

    with pytest.raises(TypeError):
        hr = Hr("some text text")


def test_self_closing_tag_br():
    """
    Tests Br self closing tag
    """
    br = Br()
    contents = render_result(br)
    assert contents == "<br />"

    br = Br(width=50)
    contents = render_result(br)
    assert contents == '<br width="50" />'
    

def test_self_closing_tag_br_content_error():
    """
    Tests Br self closing tag Type error for content
    """
    br = Br()
    with pytest.raises(TypeError):
        br.append("Some Text")

    with pytest.raises(TypeError):
        br = Br("some text text")

########
# Step 6
########
def test_anchor_tag():
    """
    Test Anchor (A) tag functions
    """
    a = A("https://www.duckduckgo.com", "Fav Search Site")
    a_text = render_result(a)

    assert 'href="https://www.duckduckgo.com"' in a_text
    assert ">Fav Search Site<" in a_text
    assert a_text.endswith("</a>")

########
# Step 7
########
def test_ul_tag():
    """
    Test Unordered List (ul) and list item (li) tag functions
    """
    ul = Ul()
    ul.append(Li("Some Text"))
    ul.append(Li("More Text", width='25px'))
    text = render_result(ul)

    assert text.startswith("<ul>")
    assert text.endswith("</ul>")
    assert "Some Text" in text
    assert '<li width="25px">' in text


def text_header_tags():
    """
    Test Header tags (h1, h2, etc)
    """
    header = H(1, "Medium Large Text")
    text = render_result(header)
    assert text.startswith("<h1>")
    assert "Medium Large Text" in text

    header = H(5, "Small Text")
    text = render_result(header)
    assert text.startswith("<h5>")
    assert "Small Text" in text

def text_header_tags_error():
    """
    Test exception condition of out of bounds header level
    """
    with pytest.raises(TypeError):
        H(0, "Text goes here")

    with pytest.raises(TypeError):
        H(6, "Text goes here")


########
# Step 8
########
def test_html_doctype():
    """
    Test Doctype for HTML
    """
    html = Html()
    text = render_result(html)
    assert text.startswith("<!DOCTYPE html>")

def test_meta_tag():
    """
    Test Meta tag
    """
    meta = Meta(charset="UTF-8")
    text = render_result(meta)
    assert text.startswith("<meta")
    assert 'charset="UTF-8"' in text
    assert text.endswith("/>")

# #####################
# # indentation testing
# #  Uncomment for Step 9 -- adding indentation
# #####################


def test_indent():
    """
    Tests that the indentation gets passed through to the renderer
    """
    html = Html("some content")
    file_contents = render_result(html, ind=3).rstrip()  #remove the end newline

    print(file_contents)
    lines = file_contents.split("\n")
    assert lines[0].startswith("   <")
    print(repr(lines[-1]))
    assert lines[-1].startswith("   <")


def test_indent_contents():
    """
    The contents in a element should be indented more than the tag
    by the amount in the indent class attribute
    """
    html = Element("some content")
    file_contents = render_result(html, ind="")

    print(file_contents)
    lines = file_contents.split("\n")
    assert lines[1].startswith(' ' * Element.indent)


def test_multiple_indent():
    """
    make sure multiple levels get indented fully
    """
    body = Body()
    body.append(P("some text"))
    html = Html(body)

    file_contents = render_result(html)

    print(file_contents)
    lines = file_contents.split("\n")
    for i in range(3):  # this needed to be adapted to the <DOCTYPE> tag
        assert lines[i + 1].startswith((' ' * (i * Element.indent)) + "<")

    assert lines[4].startswith((' ' * (3 * Element.indent)) + "some")


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
    assert lines[1].startswith(' ' * Element.indent + "thi")
    assert lines[2] == "</html>"
    assert file_contents.endswith("</html>")
