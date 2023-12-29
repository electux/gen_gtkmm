<img align="right" src="https://raw.githubusercontent.com/electux/gen_gtkmm/dev/docs/gen_gtkmm_logo.png" width="25%">

# GTK-- project skeleton generator

**gen_gtkmm** is toolset for generation GTK-- project skeleton for
developmet of desktop and embedded applications.

Developed in **[python](https://www.python.org/)** code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

[![gen_gtkmm python checker](https://github.com/electux/gen_gtkmm/actions/workflows/gen_gtkmm_python_checker.yml/badge.svg)](https://github.com/electux/gen_gtkmm/actions/workflows/gen_gtkmm_python_checker.yml) [![gen_gtkmm package checker](https://github.com/electux/gen_gtkmm/actions/workflows/gen_gtkmm_package_checker.yml/badge.svg)](https://github.com/electux/gen_gtkmm/actions/workflows/gen_gtkmm_package.yml) [![GitHub issues open](https://img.shields.io/github/issues/electux/gen_gtkmm.svg)](https://github.com/electux/gen_gtkmm/issues) [![GitHub contributors](https://img.shields.io/github/contributors/electux/gen_gtkmm.svg)](https://github.com/electux/gen_gtkmm/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
    - [Install using pip](#install-using-pip)
    - [Install using setuptools](#install-using-setuptools)
    - [Install using docker](#install-using-docker)
- [Dependencies](#dependencies)
- [Tool structure](#tool-structure)
- [Docs](#docs)
- [Copyright and licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

![debian linux os](https://raw.githubusercontent.com/electux/gen_gtkmm/dev/docs/debtux.png)

[![gen_gtkmm python3 build](https://github.com/electux/gen_gtkmm/actions/workflows/gen_gtkmm_python3_build.yml/badge.svg)](https://github.com/electux/gen_gtkmm/actions/workflows/gen_gtkmm_python3_build.yml)

Currently there are three ways to install package
* Install process based on using pip mechanism
* Install process based on build mechanism
* Install process based on setup.py mechanism
* Install process based on docker mechanism

##### Install using pip

Python package is located at **[pypi.org](https://pypi.org/project/gen_gtkmm/)**.

You can install by using pip
```
#python3
pip3 install gen_gtkmm
```

##### Install using build

Navigate to release **[page](https://github.com/electux/gen_gtkmm/releases/)** download and extract release archive.

To install **gen_gtkmm** type the following

```bash
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
```

##### Install using py setup

Navigate to **[release page](https://github.com/electux/gen_gtkmm/releases)** download and extract release archive.

To install modules, locate and run setup.py, type the following
```
tar xvzf gen_gtkmm-x.y.z.tar.gz
cd gen_gtkmm-x.y.z
#python3
pip3 install -r requirements.txt
python3 setup.py install_lib
python3 setup.py install_egg_info
python3 setup.py install_data
```

##### Install using docker

You can use Dockerfile to create image/container.

### Dependencies

**gen_gtkmm** requires next modules and libraries

* [ats-utilities - Python App/Tool/Script Utilities](https://electux.github.io/ats_utilities)

### Tool structure

**gen_gtkmm** is based on OOP

Generator structure

```
gen_gtkmm/
├── conf/
│   ├── gen_gtkmm.logo
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
```

### Docs

[![Documentation Status](https://readthedocs.org/projects/gen-esp/badge/?version=latest)](https://gen-esp.readthedocs.io/en/latest/?badge=latest)

More documentation and info at

* [gen_gtkmm.readthedocs.io](https://gen-gtkmm.readthedocs.io)
* [www.python.org](https://www.python.org/)
* [www.gtkmm.org](https://www.gtkmm.org/en/)

### Copyright and licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2021 - 2024 by [electux.github.io/gen_gtkmm](https://electux.github.io/gen_gtkmm/)

This tool is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/electux/gen_gtkmm/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.python.org/psf/donations/)
