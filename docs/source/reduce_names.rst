===============================
Reduce the Frame using Patterns
===============================

To filter the names by a given pattern or list of patterns, simply call the **.reduce_names()** method and give the patterns to use to decide which names to drop. 

Remove 
======

This example drops from the frame any element having "blank_sample" in the name, 

.. code-block:: python

    lsobject.reduce_names(remove='blank_sample')

This next example drops any element having "blank" or "zero" in the name,

.. code-block:: python

    lsobject.reduce_names(remove=['blank', 'zero'])

Keep 
====

You may also do the reverse of remove and keep only elements with a given pattern in the name using the **keep=** keyword arg. For example, keep only elements with "blank_sample" in the name, 

.. code-block:: python

    lsobject.reduce_names(keep='blank_sample')

Or keep any elements with "blank" or "zero" in the name,

.. code-block:: python

    lsobject.reduce_names(keep=['blank', 'zero'])

