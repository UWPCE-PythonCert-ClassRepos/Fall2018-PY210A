
:orphan:

.. _notes_session07:

####################
Notes for Session 07
####################

4/30/2018

A collection of notes to go over in class, to keep things organized.

Lightning Talks
===============

Adolphe Aime  Ndilingiye
Udo (Michael) Uduhiri
Zachary A Connaughton (Zach)

Issues that came up during the week.
====================================


chaining or, etc.
-----------------

this looks pretty nifty:

.. code-block:: python

    while answer != 'x' or 'r' or 't' or 'a':
        do_something()

But does that mean what you expect it to?

will it ever be ``False``?

Let's play with that...

Operator Precedence
...................

This table tells you which opertors have "Precedence" over each other -- that is, which are evaluated first:

https://docs.python.org/3/reference/expressions.html#operator-precedence

When in doubt -- add parenthesis to make it clear. Cis there a way to add parentheses that works for the above?

Comparison Chaining
...................

Another complication in all this is chaining of comparisons:

https://docs.python.org/3/reference/expressions.html#comparisons

It allows you to do nifty (and very readable) things like:

.. code-block:: python

    if a < b < c:
        do_something()

That's nice, 'cause it looks a lot like math -- simple and clear.

and that means:

.. code-block:: python

    if (a < b) and (b < c):
        do_something()


So with chaining, you can't just add parentheses to make it clear.

Also -- like with ``and`` and ``or``, chaining "shortcuts".  In the example above, if ``a`` is not less than ``b``, then ``c`` will never be evaluated. And ``b`` will only be evaluated once in any case.

So what's going on here?

.. code-block:: ipython

    In [41]: 2 < 5 in range(3)
    Out[41]: False

    In [42]: (2 < 5) in range(3)
    Out[42]: True

    In [43]: 2 < (5 in range(3))
    Out[43]: False


Turns out that ``in``, ``not``, ``not in`` are considered comparison operators too.


Mutating vs. re-assigning
-------------------------

I've seen code like this in a few trigram solutions:

``output = output + [follower]``

(``output`` is a list of strings, follower is a single string)

What it does is add a new item to a list.

But is that an efficient way to do that?

If you are adding one element to a list -- ``append()`` is the way to go.

``output_list.append(random_trigram_followers)``

Using addition works fine, but it's creating a whole new list (actually: *two* new lists) just to throw it away again.

And if you are adding another list of objects, you want to use ``extend()``.

With this code:

``output = output + [follower]``

This is what happens:

1) Create a one-element list with ``follower`` in it.
2) Create a new list with the contents of ``output`` and that just created list.
3) Re-assign the name ``output`` to that new list.
4) Throw away the original list ``output`` was bound to, and the temporary list created for ``follower``.

That's a LOT of overhead!

Be cognizant of when you are mutating (changing) an object vs. creating a new one and assigning it to the same name. When you do assignment (``=``) you are probably creating a new object -- is that what you want?


``+=`` is different -- it is the "in_place" operator, so:

``a_list += another_list``

does not create an new list -- it adds to the original list "in place" -- it is identical to:

``a_list.extend(another_list)``

And it is an efficient operation.

The trick is that the "augmented assignment" operators, like ``+=`` **do** create new object when used with an immutable:

.. code-block:: ipython

    In [4]: tup1 = tup2 = (1, 2, 3)

    In [5]: tup1 is tup2
    Out[5]: True

    In [6]: tup1 += (4, 5)

    In [7]: tup1 is tup2
    Out[7]: False

    In [9]: tup1
    Out[9]: (1, 2, 3, 4, 5)

    In [10]: tup2
    Out[10]: (1, 2, 3)

Contrast this with (mutable) lists:

.. code-block:: ipython

    In [11]: list1 = list2 = [1, 2, 3]

    In [12]: list1 += [3, 4]

    In [13]: list1 is list2
    Out[13]: True

    In [14]: list1
    Out[14]: [1, 2, 3, 3, 4]

    In [15]: list2
    Out[15]: [1, 2, 3, 3, 4]

Personally, I think it's a "wart" that augmented assignment may or may not be a mutating operation.

But at the time it was added, there were two goals:

1) Efficient in-place operations on mutables (partly to support numpy)

2) Quick and easy incrementing of values, in particular integers:

``i += 1``

And no one wanted to add **two** new sets of operators.

https://www.python.org/dev/peps/pep-0203/


A Little Code Refactoring
-------------------------

After making a few comments on a block of mailroom code, I decided it might be instructive to review and refactor it live with the class. The code can be found in the class repo in:

``/examples/Session07/refactor.py``

That code works now -- so the first thing we're going to do is make tests for it. Then we can refactor away and know it still works.

Any other questions/issue before we get into classes?

Break -- Then Lightning Talks
=============================


Classes!
========

Classes are the core of Object Oriented programming. Rather than talk about them in the abstract, we'll start doing a real problem, and talk about the pieces as we go.

html_render
-----------

So on to the the html_render assignment:

:ref:`exercise_html_renderer`



