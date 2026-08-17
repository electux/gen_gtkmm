# -*- coding: UTF-8 -*-

'''
Module
    registry.py
Copyright
    Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Encapsulates core gen_gtkmm components for simplification of gen_gtkmm bundle.
'''

from __future__ import annotations

from ats_utilities.base.setup.bundle import BaseBundle

from gen_gtkmm.core.service.iservice import IService
from gen_gtkmm.core.service.isubprocessor import ISubProcessor
from gen_gtkmm.infrastructure.cli.icli import ICLI
from gen_gtkmm.setup.bundle import GenGtkmmBundle
from gen_gtkmm.setup.validator import GenGtkmmBundleValidator
from gen_gtkmm.setup.keys import GenGtkmmBundleKeys
from gen_gtkmm.setup.dependencies import GenGtkmmBundleDependencies
from gen_gtkmm.setup.dep_validator import GenGtkmmBundleDependenciesValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_gtkmm'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_gtkmm/blob/dev/LICENSE'
__version__ = '1.1.9'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenGtkmmBundleRegistry:
    '''
        Encapsulates core gen_gtkmm components for simplification of gen_gtkmm bundle.

        It defines:

            :methods:
                | create_bundle - Creates the gen_gtkmm bundle.
                | get_version - Returns the registry version.
    '''

    @classmethod
    def create_bundle(cls, dependencies: GenGtkmmBundleDependencies) -> GenGtkmmBundle:
        '''
            Creates the gen_gtkmm bundle.

            :param dependencies: The gen_gtkmm bundle dependencies.
            :return: The gen_gtkmm bundle.
            :exceptions:
                | ATSValueError: The gen_gtkmm bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The gen_gtkmm bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_gtkmm bundle must be provided and have proper values.
                | ATSTypeError:  The gen_gtkmm bundle must be an instance of GenGtkmmBundle and
                |                its attributes must be instances of their respective types.
        '''
        GenGtkmmBundleDependenciesValidator.validate(dependencies)

        base: BaseBundle | None = dependencies.get(GenGtkmmBundleKeys.DEPENDENCY_BASE) if dependencies else None
        service: IService | None = dependencies.get(GenGtkmmBundleKeys.DEPENDENCY_SERVICE) if dependencies else None
        subprocessor: ISubProcessor | None = dependencies.get(GenGtkmmBundleKeys.DEPENDENCY_SUBPROCESSOR) if dependencies else None
        cli: ICLI | None = dependencies.get(GenGtkmmBundleKeys.DEPENDENCY_CLI) if dependencies else None

        bundle: GenGtkmmBundle = GenGtkmmBundle(base=base, service=service, subprocessor=subprocessor, cli=cli)

        GenGtkmmBundleValidator.validate(bundle)

        return bundle

    @classmethod
    def get_version(cls) -> str:
        '''
            Returns the registry version.

            :return: The registry version.
            :exceptions: None.
        '''
        return __version__
