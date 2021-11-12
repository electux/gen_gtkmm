GTK-- project skeleton generator
--------------------------------

**gen_gtkmm** is toolset for generation GTK-- project skeleton for
developmet of desktop and embedded applications.

Developed in `python <https://www.python.org/>`_ code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|Python package| |GitHub issues| |Documentation Status| |GitHub contributors|

.. |Python package| image:: https://github.com/electux/gen_gtkmm/workflows/Python%20package%20gen_gtkmm/badge.svg
   :target: https://github.com/electux/gen_gtkmm/workflows/Python%20package%20gen_gtkmm/badge.svg?branch=master

.. |GitHub issues| image:: https://img.shields.io/github/issues/electux/gen_gtkmm.svg
   :target: https://github.com/electux/gen_gtkmm/issues

.. |GitHub contributors| image:: https://img.shields.io/github/contributors/electux/gen_gtkmm.svg
   :target: https://github.com/electux/gen_gtkmm/graphs/contributors

.. |Documentation Status| image:: https://readthedocs.org/projects/gen_gtkmm/badge/?version=latest
   :target: https://gen_gtkmm.readthedocs.io/projects/gen_gtkmm/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents:

   self
   modules

Installation
-------------

|Install Python2 Package| |Install Python3 Package|

.. |Install Python2 Package| image:: https://github.com/electux/gen_gtkmm/workflows/Install%20Python2%20Package%20gen_gtkmm/badge.svg
   :target: https://github.com/electux/gen_gtkmm/workflows/Install%20Python2%20Package%20gen_gtkmm/badge.svg?branch=master

.. |Install Python3 Package| image:: https://github.com/electux/gen_gtkmm/workflows/Install%20Python3%20Package%20gen_gtkmm/badge.svg
   :target: https://github.com/electux/gen_gtkmm/workflows/Install%20Python3%20Package%20gen_gtkmm/badge.svg?branch=master

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/electux/gen_gtkmm/releases

To install **gen_gtkmm** type the following:

.. code-block:: bash

    tar xvzf gen_gtkmm-x.y.z.tar.gz
    cd gen_gtkmm-x.y.z
    #python2
    pip install -r requirements.txt
    python setup.py install_lib
    python setup.py install_egg_info
    python setup.py install_data
    #python3
    pip3 install -r requirements.txt
    python3 setup.py install_lib
    python3 setup.py install_egg_info
    python3 setup.py install_data

You can use Docker to create image/container, or You can use pip to install:

.. code-block:: bash

    #python2
    pip install gen_gtkmm
    #python3
    pip3 install gen_gtkmm

|GitHub docker checker|

.. |GitHub docker checker| image:: https://github.com/electux/gen_gtkmm/workflows/gen_gtkmm%20docker%20checker/badge.svg
   :target: https://github.com/electux/gen_gtkmm/actions?query=workflow%3A%22gen_gtkmm+docker+checker%22

Dependencies
-------------

**gen_gtkmm** requires next modules and libraries:

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

Generation flow
----------------

Base flow of generation process:

.. image:: https://raw.githubusercontent.com/electux/gen_gtkmm/dev/docs/gen_gtkmm_flow.png

Tool structure
---------------

**gen_gtkmm** is based on OOP:

.. image:: https://raw.githubusercontent.com/electux/gen_gtkmm/dev/docs/gen_gtkmm.png

Code structure:

.. code-block:: bash

    gen_gtkmm/
    ├── conf/
    │   ├── gen_gtkmm.cfg
    │   ├── gen_gtkmm_util.cfg
    │   ├── project.yaml
    │   └── template/
    │       ├── ccflags.template
    │       ├── header_module.template
    │       ├── ldflags.template
    │       ├── main_module.template
    │       ├── Makefile.template
    │       ├── objects.template
    │       ├── source_module.template
    │       └── sources.template
    ├── __init__.py
    ├── log/
    │   └── gen_gtkmm.log
    ├── pro/
    │   ├── config/
    │   │   ├── __init__.py
    │   │   ├── pro_name.py
    │   │   └── template_dir.py
    │   ├── __init__.py
    │   ├── read_template.py
    │   └── write_template.py
    └── run/
        └── gen_gtkmm_run.py

Copyright and licence
----------------------

|License: GPL v3| |License: Apache 2.0|

.. |License: GPL v3| image:: https://img.shields.io/badge/License-GPLv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |License: Apache 2.0| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
   :target: https://opensource.org/licenses/Apache-2.0

Copyright (C) 2021 by `electux.github.io/gen_gtkmm <https://electux.github.io/gen_gtkmm>`_

**gen_gtkmm** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|Python Software Foundation|

.. |Python Software Foundation| image:: https://raw.githubusercontent.com/electux/gen_gtkmm/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|Donate|

.. |Donate| image:: https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif
   :target: https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`