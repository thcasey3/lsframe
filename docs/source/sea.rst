===============
seaborn relplot
===============

With the **sea()** method a **relplot** is made using the **lsobject.frame**. Use the same argument names used in **seaborn.relplot()** as dictionary keys with their corresponding values being any allowed values according to the **seaborn.relplot()** docs,

.. figure:: _static/images/sea_df.png
    :width: 700
    :alt: lsframe concept
    :align: center

    **lsobject.frame**

.. code-block:: python

    lsobject.sea(options={'x': 'output1',
                          'y': 'output2',
                          'hue': 'date_delta',
                          's': 100})

.. figure:: _static/images/sea_scatter.png
    :width: 500
    :alt: lsframe concept
    :align: center

    Scatterplot from seaborn.relplot()