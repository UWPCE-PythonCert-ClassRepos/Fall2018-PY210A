
:orphan:

.. _notes_session08:

####################
Notes for Session 08
####################

5/3/2018

A collection of notes to go over in class, to keep things organized.

Lightning Talks (last)
======================

Jay Johnson

Tammy Do

Issues that came up during the week. (by Chris)
===============================================

What to test? And how?
----------------------

Make sure you test what matters about a function's result -- it's easiest (particularly if you wrote the code first) to simply match results, but your system will be more flexible if you test for the parts that matter, and won't change.

Ideally, your tests should be as isolated as possible. So if you, for instance, need to test that the correct letter is generated from a donor object, then create a donor object in the test, and pass that in, rather than using pulling it from the donor_db -- that way, the donor_db could be broken, and the individual tests will pass.

If the object(s) you need to create are complex, then you can use "fixtures" to set things up for you. We'll get into that in the next quarter.

This will start to make more and more sense as we do more testing -- and particularly when we do TDD and write the tests along with the code.

Example:
........

.. code-block:: python

    def test_p_tag():
        assert Para.tag == 'p'

I know I started out that way -- 'cause there wasn't anything else to test. But this is really testing an implementation detail -- the Para elements has a attribute named "tag" that is 'p'. But is that a public part of the API? do we care? -- No. What we care about is that the correct tag gets rendered, so a test for THAT makes more sense:

.. code-block:: python

    def test_render_para():
        my_stuff = 'spam, spam, spam'
        p = Para(my_stuff)
        more_stuff = 'eggs, eggs, eggs'
        p.append(more_stuff)
        contents = render_element(p).strip()
        assert contents.startswith('<p>')
        assert contents.endswith('</p>')
        assert my_stuff in contents
        assert more_stuff in contents


Do you always need an __init__?
-------------------------------

No -- you don't :-)

The ONLY thing "special" about __init__ is that it is automatically called when an instance is created.  Other than that, it's a regular method. So if you don't define one, then the superclass' __init__ will be called.

That's what inheritance is all about -- the subclass inherits ALL the superclasses methods -- including __init__.

So never write an __init__ that does nothing but call the superclass __init__

Subclasses and ``self``
-----------------------

``self`` is the first parameter in all methods. But why??

``self`` is the "current" instance of the object. This means that you don't know at code writing time what type it is -- is it the current class? some subclass?

Let's experiment with that.

html_render
-----------

Let's look at up to step 3....

And move along...

Lightning Talks
---------------

Circle class....


Hosung's Notes
==============

Announcements
-------------

Office hours: 2:30pm-4:30pm, Foster Library (Paccar Hall) Study Room #9

Online participation: https://washington.zoom.us/my/pythonxl

Grading, PR feedback
--------------------

How's it going? I've been trying to provide feedback on PRs and enter grades, but I'm finding it hard to keep track of grades from PRs, because sometimes new commits start piling up on an old PR. Your feedback welcome (if any). I personally think everyone's working very hard, so this shouldn't be a big concern. If you'd like our feedback on some specific parts, please do let us know by email separately or clearly indicate that in your PR submission comment.

Opportunity: LEAP
-----------------

Cohort 10 applications is now open just in time: http://www.industryexplorers.com/

Python classes: Special methods & protocols
-------------------------------------------

A lot of this topic is closely related to the operator overloading feature that's available in other languages like C++ and C#. A favorite example for the topic is to implement fraction (rational number) arithmetics, like making ``1/2+1/3=5/6`` possible, instead of ``1/2+1/3=0.8333333333``. Python already offers the Fraction class in the fractions module, but let's pretend it's not available and implement ourselves.

Initial Fraction class definition: ``examples/Session08/fraction.py``

Initial fraction test code:  ``examples/Session08/test_fraction.py``

Python static vs. class methods
-------------------------------

Coming from Java/C++, this was always confusing to me. Now I think I understand this better, and I may share my understanding and realization with class. Let's go over the static/class methods materials: https://uwpce-pythoncert.github.io/PythonCertDevel/modules/StaticAndClassMethods.html
