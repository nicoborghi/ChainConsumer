"""
========================
Gaussian KDE and Extents
========================

Smooth marginalised distributions with a Gaussian KDE, and pick custom extents.


Note that invoking the KDE on large data sets will significantly increase rendering time when
you have a large number of points.

Also note that if you pass a floating point number to bins, it multiplies the default bin size
(which is a function of number of steps in the chain) by that amount. If you give it an integer,
it will use that many bins.
"""

import numpy as np
from chainconsumer import ChainConsumer

if __name__ == "__main__":
    data = np.random.multivariate_normal([0.0, 4.0], [[1.0, 0.7], [0.7, 1.5]], size=50000)

    c = ChainConsumer()
    c.add_chain(data)
    c.configure(bins=0.9, kde=True)
    fig = c.plotter.plot(extents=[(-2, 4), (0, 10)])

    fig.set_size_inches(4.5 + fig.get_size_inches())  # Resize fig for doco. You don't need this.
