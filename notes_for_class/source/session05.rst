
:orphan:

.. _notes_session05:

####################
Notes for Session 05
####################

A collection of notes to go over in class, to keep things organized.

Lightning Talks
===============

Ornob Siddiquee

Andrew Wall


Issues that came up during the week.
====================================

git and generated files
-----------------------

In general, you don't want to put generated files in git.

In this case, the letters your mailroom program created.

**Caution:** be very careful with ``git add .`` or ``git add *`` -- generally better to specifically add the files you now you need.

Style
-----

Use PEP8 style -- really!

https://www.python.org/dev/peps/pep-0008/

The ONLY exception is if you work in an organization that has a different style guide. It can make sense for your python code to match other code in an organization. But otherwise, use a style consistent with the rest of the Python world.

And don't use "Hungarian Notation" -- it is really non-pythonic, and sometimes actually wrong -- and a string called ``intSomething`` just adds confusion!

The best way to do this is with a linter in your editor -- like the Anaconda package in Sublime. A number of you are getting really annoyed by all the "noise" that the linter creates. But if you keep your code in PEP8 style, it won't be there!

sorting
-------

``.sort()`` vs ``sorted()``

What is the "key" thing? how do you make one?


Minor Issues
------------

Remember that:

``something in a_dict`` checks if ``this`` is a key

similarly:

``for k in dict:``

loops through the keys. So no need for:

``for k in dict.keys():``


Getting an arbitrary key from a dict
------------------------------------

See ``arbitrary_key.py`` in `examples/session05`

Review of last week's assignments
=================================

Mailroom review
---------------

Anyone up for a review?

Trigrams review
---------------

Anyone want to look at theirs?


Lightning Talks
===============

Ornob Siddiquee

Andrew Wall

New Assignments
===============

Comprehensions
--------------

It turns out the Comprehensions lab was not in Canvas!

It is now. But let's take a few mintues to go through it in class:

https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/comprehensions_lab.html

Exceptions
----------

Exceptions take a little while to "wrap your head around".

Shall we do the Excercise together?

https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/except_exercise.html

