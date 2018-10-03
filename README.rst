=========
sedflux3d
=========


.. image:: https://img.shields.io/pypi/v/sedflux3d.svg
        :target: https://pypi.python.org/pypi/sedflux3d

.. image:: https://img.shields.io/travis/mcflugen/sedflux3d.svg
        :target: https://travis-ci.org/mcflugen/sedflux3d

.. image:: https://readthedocs.org/projects/sedflux3d/badge/?version=latest
        :target: https://sedflux3d.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


PyMT plugin for sedflux3d


* Free software: MIT license
* Documentation: https://sedflux3d.readthedocs.io.


---------------
Installing pymt
---------------

Installing `pymt` from the `conda-forge` channel can be achieved by adding
`conda-forge` to your channels with:

.. code::

  conda config --add channels conda-forge

*Note*: Before installing `pymt`, you may want to create a separate environment
into which to install it. This can be done with,

.. code::

  conda create -n pymt python=3.6
  conda activate pymt

Once the `conda-forge` channel has been enabled, `pymt` can be installed with:

.. code::

  conda install pymt

It is possible to list all of the versions of `pymt` available on your platform with:

.. code::

  conda search pymt --channel conda-forge

-------------------------
Installing pymt_sedflux3d
-------------------------

Once `pymt` is installed, the dependencies of `pymt_sedflux3d` can
be installed with:

.. code::

  conda install sedflux

Until `pymt_sedflux3d` is available on `conda-forge`, it must
by installed from source,

.. code::

  git clone https://github.com/mcflugen/pymt_sedflux3d
  cd pymt_sedflux3d
  python setup.py install
