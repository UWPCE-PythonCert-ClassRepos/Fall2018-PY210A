:orphan:

.. _notes_session04:

####################
Notes for Session 04
####################

Instructor: Chris

4/19/2018

A collection of notes to go over in class, to keep things organized.

Lightning Talks
===============

Brianna Dean

Aarthi Ravichander

Issues that came up during the week.
====================================

Mutable default parameters
--------------------------

There was a video on this -- any questions about it?

If not then we'll move on...

This is a real "gotcha" in Python. One of you wrote a non-recursive solution to the sum_series problem. It worked great -- EXCEPT if it got called more than once! Any idea what the problem is?

.. code-block:: python

    def sum_series(nth=1, sequence=[0,1]):
        """
        Generate a list of sums given a seed and return the Nth number.
        """
        for i in range(2, nth):
            sequence.append(sequence[i-2] + sequence[i-1])
        return sequence[nth-1]

So this uses the logic of starting out with the first two values in the series, and then looping to build up the series from there.

And [0, 1] is set as a default to start the series off -- the start of the Fibonacci series.  So if you pass in only one argument, you should get the Fibonacci number:

Remember that the start of the Fibonacci series is::

  0, 1, 1, 2, 3, 5, 8, 13, ...

What happens when you run this code:

.. code-block:: python

    In [21]: sum_series(5)
    Out[21]: 3

All good.

    In [22]: sum_series(6)
    Out[22]: 1
    # WTF???

The issue is that:

Default Arguments get evaluated **when the function is defined**. So every time the function is called, it will use the *same* list! Each time adding more and more to the list.

Let's explore that some more, and some solutions....


Recursion in an interactive loop
--------------------------------

not a great idea!

you can do something like:

.. code-block:: python

    def mainloop():
        while True:
            ans = input("A question > ")
            ....
            if ans == "again"
                mainloop()

Let's look at this:

``examples/session04/recursive_mainloop.py``

(do a ``git pull upstream master`` if you don't see it.)

Slicing and List labs
---------------------

Any questions?

Let's look at my solutions quickly.

mailroom
--------

Anyone get it done?

Should we look at my solution -- or wait??

Lightning Talks:
----------------

Brianna Dean

Aarthi Ravichander

New Material
============

Any questions on dictionaries, set or files?

This gets fun now!

mailroom part 2
---------------

How might you use dictionaries in mailroom? If you haven't finished it without dicts, whynot add them now?

trigrams
--------

This is a really fun one -- but challenging.

Let's get a start on it!


