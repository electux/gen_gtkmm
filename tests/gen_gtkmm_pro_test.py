# -*- coding: UTF-8 -*-

'''
Module
    gen_gtkmm_pro_test.py
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
    Defines class GtkMMSetupTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of GtkMMSetup.
Execute
    python3 -m unittest -v gen_gtkmm_pro_test
'''

import sys
from typing import List
from unittest import TestCase, main

try:
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_value_error import ATSValueError
    from gen_gtkmm.pro import GtkMMSetup
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://electux.github.io/gen_gtkmm'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/electux/gen_gtkmm/blob/dev/LICENSE'
__version__ = '1.1.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GtkMMSetupTestCase(TestCase):
    '''
        Defines class GtkMMSetupTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of GtkMMSetup.
        GtkMMSetup unit tests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_default_create - Default on create is not None.
                | test_get_reader - Is reader ok.
                | test_get_writer - Is writer ok.
                | test_gen_project_empty - Create project with missing name.
                | test_gen_project_none - Create project with None name.
                | test_gen_project - Create project.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_default_create(self) -> None:
        '''Default on create is not None'''
        generator: GtkMMSetup = GtkMMSetup()
        self.assertIsNotNone(generator)

    def test_get_reader(self) -> None:
        '''Is reader ok'''
        generator: GtkMMSetup = GtkMMSetup()
        self.assertIsNotNone(generator.get_reader())

    def test_get_writer(self) -> None:
        '''Is writer ok'''
        generator: GtkMMSetup = GtkMMSetup()
        self.assertIsNotNone(generator.get_writer())

    def test_gen_project_empty(self) -> None:
        '''Create project with missing name'''
        generator: GtkMMSetup = GtkMMSetup()
        with self.assertRaises(ATSValueError):
            generator.gen_pro_setup("", "gtkmm3")

    def test_gen_project_none(self) -> None:
        '''Create project with None name'''
        generator: GtkMMSetup = GtkMMSetup()
        with self.assertRaises(ATSTypeError):
            generator.gen_pro_setup(None, "gtkmm3")

    def test_gen_project(self) -> None:
        '''Create project'''
        generator: GtkMMSetup = GtkMMSetup()
        self.assertTrue(generator.gen_pro_setup('full_simple', 'gtkmm3'))


if __name__ == '__main__':
    main()
