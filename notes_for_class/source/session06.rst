
:orphan:

.. _notes_session06:

####################
Notes for Session 06
####################

4/26/2018

A collection of notes to go over in class, to keep things organized.

Lightning Talks
===============

Ryan Drovdahl

Meet Shah



Issues that came up during the week.
====================================


Getting an arbitrary key from a dict
------------------------------------

See ``arbitrary_key.py`` in `examples/session05`


dict as switch -- how do you leave the loop?
--------------------------------------------

Let's look at a particularly nifty solution:

``solutions/Lesson05/mailroom_dict_as_switch``


globals??
---------

a number of folks have been putting code in the global (module) namespace:

.. code-block:: python

   the_dict = {}

   def fun():
       ...
       the_dict = something()

What's wrong with this?

Any Questions about the homework -- or anything?
------------------------------------------------

Break and Lightning talks:


Ryan Drovdahl

Meet Shah


Testing?
--------

Did you'all do the testing exercise with a coding bat example?

We could do one now.

Or...

Advanced Argument Passing
-------------------------

All this ``*arg``, ``**kwargs`` stuff a bit confusing?

Let's explore it a bit.

AND -- we'll use TDD to do it.

Exercise here:

https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/args_kwargs_lab.html








