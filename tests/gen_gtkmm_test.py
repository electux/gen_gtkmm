# -*- coding: UTF-8 -*-

'''
Module
    gen_gtkmm_test.py
Copyright
    Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines class GenGtkMMTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of GenGtkMM.
Execute
    python3 -m unittest -v gen_gtkmm_test
'''

import sys
from typing import List
from os import makedirs, rmdir
from unittest import TestCase, main

try:
    from gen_gtkmm import GenGtkMM
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://electux.github.io/gen_gtkmm'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/electux/gen_gtkmm/blob/dev/LICENSE'
__version__: str = '1.1.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class GenGtkMMTestCase(TestCase):
    '''
        Defines class GenGtkMMTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of GenGtkMM.
        GenGtkMM unit tests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_default_create - Default on create is not None.
                | test_missing_args - Missing args.
                | test_process3 - Generate project gtkmm3.
                | test_process4 - Generate project gtkmm4.
                | test_pro_already_exists - Generate already existing project.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_default_create(self) -> None:
        '''Default on create is not None'''
        generator: GenGtkMM = GenGtkMM()
        self.assertIsNotNone(generator)

    def test_missing_args(self) -> None:
        '''Missing args'''
        sys.argv.clear()
        generator: GenGtkMM = GenGtkMM()
        self.assertFalse(generator.process())

    def test_wrong_arg(self) -> None:
        '''Generate project'''
        sys.argv.clear()
        sys.argv.insert(0, '-d')
        sys.argv.insert(1, 'wrong')
        sys.argv.insert(2, '-t')
        sys.argv.insert(3, 'gtkmm3')
        generator: GenGtkMM = GenGtkMM()
        self.assertFalse(generator.process())

    def test_process3(self) -> None:
        '''Generate project'''
        sys.argv.clear()
        sys.argv.insert(0, '-n')
        sys.argv.insert(1, 'latest3')
        sys.argv.insert(2, '-t')
        sys.argv.insert(3, 'gtkmm3')
        generator: GenGtkMM = GenGtkMM()
        self.assertTrue(generator.process())

    def test_process4(self) -> None:
        '''Generate project'''
        sys.argv.clear()
        sys.argv.insert(0, '-n')
        sys.argv.insert(1, 'latest4')
        sys.argv.insert(2, '-t')
        sys.argv.insert(3, 'gtkmm4')
        generator: GenGtkMM = GenGtkMM()
        self.assertTrue(generator.process())

    def test_pro_already_exists(self) -> None:
        '''Generate already existing project'''
        sys.argv.clear()
        sys.argv.insert(0, '-n')
        sys.argv.insert(1, 'fresh_new')
        sys.argv.insert(2, '-t')
        sys.argv.insert(3, 'gtkmm3')
        generator: GenGtkMM = GenGtkMM()
        makedirs('fresh_new')
        self.assertFalse(generator.process())
        rmdir('fresh_new')


if __name__ == '__main__':
    main()
