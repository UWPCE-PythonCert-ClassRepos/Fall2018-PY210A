
:orphan:

.. _notes_session10:

####################
Notes for Session 10
####################

12/11/2018

A collection of notes to go over in class, to keep things organized.

Lightning Talks
===============

Kanahn Sethunarayanan

Tim Pauley

Zidan Luo

Issues that came up during the week.
====================================

``classmethod``
---------------

I didn't get a chance to go over this last week, so I will now.

One Circle solution had this:

.. code-block:: python

    @classmethod #???run c
    def from_diameter(cls, val):
        cls.diameter = val
        cls.radius = val / 2
        return cls

What is wrong with this code? What is actually happening here??

When to make a method or property?
-----------------------------------

It is a good idea to make a property to access information in your class that requires "inside information", For example, in a Donor class:

.. code-block:: python

  @property
  def maxdonation(self):
      return max(self.donations)

This way, client code can get the maximum donation without knowing, or caring, how the donations are stored in the class.

However, there is no need to create a property to "hide" something that is already part of the public API:

.. code-block:: python

  @property
  def namelength(self):
      return(len(self.name))

There is no point to this -- ``a_donor.name`` is expected to be a string -- so if you want to know how long it is, you can simply do:  ``len(a_donor.name)``

You *do* want to use properties to "hide" implementation details -- but the name attribute being a string is part of the API, not an implementation detail.


Anything else from OO mailroom?
-------------------------------

Does anyone volunteer for a code review?or

Or should we review mine?

The Next Class
==============

Next quarter, you'll finish up the core of the Python language, then go into depth on some of the more advanced features of the language. Finally, you'll do a bit with using Python with other tools, such as databases.


End of Quarter:
===============

We will review PRs through Sunday.






