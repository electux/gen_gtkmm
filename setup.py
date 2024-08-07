#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Module
    setup.py
Copyright
    Copyright (C) 2021 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
    gen_gtkmm is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    gen_gtkmm is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines setup for tool gen_gtkmm.
'''

from __future__ import print_function
from typing import List, Optional
from os.path import abspath, dirname, join
from setuptools import setup

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://electux.github.io/gen_gtkmm'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/electux/gen_gtkmm/blob/dev/LICENSE'
__version__ = '1.1.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'

TOOL_DIR: str = 'gen_gtkmm/'
CONF: str = 'conf'
TEMPLATE: str = 'conf/template'
LOG: str = 'log'
THIS_DIR: str = abspath(dirname(__file__))
long_description: Optional[str] = None
with open(join(THIS_DIR, 'README.md'), encoding='utf-8') as readme:
    long_description = readme.read()
PROGRAMMING_LANG: str = 'Programming Language :: Python ::'
VERSIONS: List[str] = ['3.10', '3.11']
SUPPORTED_PY_VERSIONS: List[str] = [
    f'{PROGRAMMING_LANG} {VERSION}' for VERSION in VERSIONS
]
LICENSE_PREFIX: str = 'License :: OSI Approved ::'
LICENSES: List[str] = [
    'GNU Lesser General Public License v2 (LGPLv2)',
    'GNU Lesser General Public License v2 or later (LGPLv2+)',
    'GNU Lesser General Public License v3 (LGPLv3)',
    'GNU Lesser General Public License v3 or later (LGPLv3+)',
    'GNU Library or Lesser General Public License (LGPL)'
]
APPROVED_LICENSES: List[str] = [
    f'{LICENSE_PREFIX} {LICENSE}' for LICENSE in LICENSES
]
PYP_CLASSIFIERS: List[str] = SUPPORTED_PY_VERSIONS + APPROVED_LICENSES
setup(
    name='gen_gtkmm',
    version='1.1.6',
    description='GTK-- project skeleton generator',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://electux.github.io/gen_gtkmm/',
    license='GPL 2024 Free software to use and distributed it.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='GTK--, Project, C++, Gtk, Unix, Linux',
    platforms='POSIX',
    classifiers=PYP_CLASSIFIERS,
    packages=['gen_gtkmm', 'gen_gtkmm.pro'],
    install_requires=['ats-utilities'],
    package_data={
        'gen_gtkmm': [
            'py.typed',
            f'{CONF}/gen_gtkmm.logo',
            f'{CONF}/gen_gtkmm.cfg',
            f'{CONF}/gen_gtkmm_util.cfg',
            f'{CONF}/project.yaml',
            f'{TEMPLATE}/gtkmm3/about_header.template',
            f'{TEMPLATE}/gtkmm3/about_source.template',
            f'{TEMPLATE}/gtkmm3/application_header.template',
            f'{TEMPLATE}/gtkmm3/application_source.template',
            f'{TEMPLATE}/gtkmm3/csflags.template',
            f'{TEMPLATE}/gtkmm3/cxxflags.template',
            f'{TEMPLATE}/gtkmm3/help_header.template',
            f'{TEMPLATE}/gtkmm3/help_source.template',
            f'{TEMPLATE}/gtkmm3/home_header.template',
            f'{TEMPLATE}/gtkmm3/home_source.template',
            f'{TEMPLATE}/gtkmm3/imodel_header.template',
            f'{TEMPLATE}/gtkmm3/model_header.template',
            f'{TEMPLATE}/gtkmm3/model_source.template',
            f'{TEMPLATE}/gtkmm3/main_source.template',
            f'{TEMPLATE}/gtkmm3/Makefile.template',
            f'{TEMPLATE}/gtkmm3/objects.template',
            f'{TEMPLATE}/gtkmm3/odflags.template',
            f'{TEMPLATE}/gtkmm3/settings_header.template',
            f'{TEMPLATE}/gtkmm3/settings_source.template',
            f'{TEMPLATE}/gtkmm3/sources.template',
            f'{TEMPLATE}/gtkmm3/toolchain.template',
            f'{TEMPLATE}/gtkmm4/about_header.template',
            f'{TEMPLATE}/gtkmm4/about_source.template',
            f'{TEMPLATE}/gtkmm4/application_header.template',
            f'{TEMPLATE}/gtkmm4/application_source.template',
            f'{TEMPLATE}/gtkmm4/csflags.template',
            f'{TEMPLATE}/gtkmm4/cxxflags.template',
            f'{TEMPLATE}/gtkmm4/help_header.template',
            f'{TEMPLATE}/gtkmm4/help_source.template',
            f'{TEMPLATE}/gtkmm4/home_header.template',
            f'{TEMPLATE}/gtkmm4/home_source.template',
            f'{TEMPLATE}/gtkmm4/imodel_header.template',
            f'{TEMPLATE}/gtkmm4/model_header.template',
            f'{TEMPLATE}/gtkmm4/model_source.template',
            f'{TEMPLATE}/gtkmm4/main_source.template',
            f'{TEMPLATE}/gtkmm4/Makefile.template',
            f'{TEMPLATE}/gtkmm4/objects.template',
            f'{TEMPLATE}/gtkmm4/odflags.template',
            f'{TEMPLATE}/gtkmm4/settings_header.template',
            f'{TEMPLATE}/gtkmm4/settings_source.template',
            f'{TEMPLATE}/gtkmm4/sources.template',
            f'{TEMPLATE}/gtkmm4/toolchain.template',
            f'{LOG}/gen_gtkmm.log'
        ]
    },
    data_files=[(
        '/usr/local/bin/', [
            f'{TOOL_DIR}run/gen_gtkmm_run.py'
        ]
    )]
)
