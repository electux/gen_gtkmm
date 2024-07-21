GTK-- project skeleton generator
--------------------------------

**gen_gtkmm** is toolset for generation GTK-- project skeleton for
developmet of desktop and embedded applications.

Developed in `python <https://www.python.org/>`_ code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|gen_gtkmm python checker| |gen_gtkmm python package| |github issues| |documentation status| |github contributors|

.. |gen_gtkmm python checker| image:: https://github.com/electux/gen_gtkmm/actions/workflows/gen_gtkmm_python_checker.yml/badge.svg
   :target: https://github.com/electux/gen_gtkmm/actions/workflows/gen_gtkmm_python_checker.yml

.. |gen_gtkmm python package| image:: https://github.com/electux/gen_gtkmm/actions/workflows/gen_gtkmm_package_checker.yml/badge.svg
   :target: https://github.com/electux/gen_gtkmm/actions/workflows/gen_gtkmm_package.yml

.. |github issues| image:: https://img.shields.io/github/issues/electux/gen_gtkmm.svg
   :target: https://github.com/electux/gen_gtkmm/issues

.. |github contributors| image:: https://img.shields.io/github/contributors/electux/gen_gtkmm.svg
   :target: https://github.com/electux/gen_gtkmm/graphs/contributors

.. |documentation status| image:: https://readthedocs.org/projects/gen-gtkmm/badge/?version=latest
   :target: https://gen-gtkmm.readthedocs.io/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents

   self
   modules

Installation
-------------

|gen_gtkmm python3 build|

.. |gen_gtkmm python3 build| image:: https://github.com/electux/gen_gtkmm/actions/workflows/gen_gtkmm_python3_build.yml/badge.svg
   :target: https://github.com/electux/gen_gtkmm/actions/workflows/gen_gtkmm_python3_build.yml

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/electux/gen_gtkmm/releases

To install **gen_gtkmm** type the following

.. code-block:: bash

    tar xvzf gen_gtkmm-x.y.z.tar.gz
    cd gen_gtkmm-x.y.z/
    # python3
    wget https://bootstrap.pypa.io/get-pip.py
    python3 get-pip.py 
    python3 -m pip install --upgrade setuptools
    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade build
    pip3 install -r requirements.txt
    python3 -m build --no-isolation --wheel
    pip3 install ./dist/gen_gtkmm-*-py3-none-any.whl
    rm -f get-pip.py
    chmod 755 /usr/local/lib/python3.10/dist-packages/usr/local/bin/gen_gtkmm_run.py
    ln -s /usr/local/lib/python3.10/dist-packages/usr/local/bin/gen_gtkmm_run.py /usr/local/bin/gen_gtkmm_run.py

You can use Docker to create image/container, or You can use pip to install

.. code-block:: bash

    #python3
    pip3 install gen_gtkmm

Dependencies
-------------

**gen_gtkmm** requires next modules and libraries

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

Tool structure
---------------

**gen_gtkmm** is based on OOP

Code structure:

.. code-block:: bash

    gen_gtkmm/
        ├── conf/
        │   ├── gen_gtkmm.cfg
        │   ├── gen_gtkmm.logo
        │   ├── gen_gtkmm_util.cfg
        │   ├── project.yaml
        │   └── template/
        │       ├── gtkmm3/
        │       │   ├── about_header.template
        │       │   ├── about_source.template
        │       │   ├── application_header.template
        │       │   ├── application_source.template
        │       │   ├── csflags.template
        │       │   ├── cxxflags.template
        │       │   ├── help_header.template
        │       │   ├── help_source.template
        │       │   ├── home_header.template
        │       │   ├── home_source.template
        │       │   ├── imodel_header.template
        │       │   ├── main_source.template
        │       │   ├── Makefile.template
        │       │   ├── model_header.template
        │       │   ├── model_source.template
        │       │   ├── objects.template
        │       │   ├── odflags.template
        │       │   ├── settings_header.template
        │       │   ├── settings_source.template
        │       │   ├── sources.template
        │       │   └── toolchain.template
        │       └── gtkmm4/
        │           ├── about_header.template
        │           ├── about_source.template
        │           ├── application_header.template
        │           ├── application_source.template
        │           ├── csflags.template
        │           ├── cxxflags.template
        │           ├── help_header.template
        │           ├── help_source.template
        │           ├── home_header.template
        │           ├── home_source.template
        │           ├── imodel_header.template
        │           ├── main_source.template
        │           ├── Makefile.template
        │           ├── model_header.template
        │           ├── model_source.template
        │           ├── objects.template
        │           ├── odflags.template
        │           ├── settings_header.template
        │           ├── settings_source.template
        │           ├── sources.template
        │           └── toolchain.template
        ├── __init__.py
        ├── log/
        │   └── gen_gtkmm.log
        ├── pro/
        │   ├── __init__.py
        │   ├── read_template.py
        │   └── write_template.py
        ├── py.typed
        └── run/
            └── gen_gtkmm_run.py

    8 directories, 53 files

Copyright and licence
----------------------

|license: gpl v3| |license: apache 2.0|

.. |license: gpl v3| image:: https://img.shields.io/badge/license-gplv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |license: apache 2.0| image:: https://img.shields.io/badge/license-apache%202.0-blue.svg
   :target: https://opensource.org/licenses/apache-2.0

Copyright (C) 2021 - 2024 by `electux.github.io/gen_gtkmm <https://electux.github.io/gen_gtkmm>`_

**gen_gtkmm** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|python software foundation|

.. |python software foundation| image:: https://raw.githubusercontent.com/electux/gen_gtkmm/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|donate|

.. |donate| image:: https://www.paypalobjects.com/en_us/i/btn/btn_donatecc_lg.gif
   :target: https://www.python.org/psf/donations/

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
