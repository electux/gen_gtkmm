# -*- coding: UTF-8 -*-

'''
Module
    factory.py
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
    Factory for creating the gen_gtkmm bundle.
'''

from __future__ import annotations

from ats_utilities.base.setup.factory import BaseBundleFactory
from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.base.setup.options import BaseBundleOptions
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.factory import ContextBundleFactory

from gen_gtkmm.setup.bundle import GenGtkmmBundle
from gen_gtkmm.setup.options import GenGtkmmBundleOptions
from gen_gtkmm.setup.registry import GenGtkmmBundleRegistry
from gen_gtkmm.setup.dependencies import GenGtkmmBundleDependencies
from gen_gtkmm.setup.opt_validator import GenGtkmmBundleOptionsValidator
from gen_gtkmm.setup.keys import GenGtkmmBundleKeys
from gen_gtkmm.core.service.engine import Service
from gen_gtkmm.infrastructure.subprocessor import SubProcessor
from gen_gtkmm.infrastructure.cli.engine import CLI
from gen_gtkmm.infrastructure.cli.setup.bundle import CLIBundle
from gen_gtkmm.infrastructure.cli.setup.dependencies import CLIBundleDependencies
from gen_gtkmm.infrastructure.cli.setup.registry import CLIBundleRegistry
from gen_gtkmm.infrastructure.command.command import CommandBundle
from gen_gtkmm.infrastructure.command.gen_gtkmm_command_definition import GenGtkmmCommandDefinition
from gen_gtkmm.infrastructure.command.gen_gtkmm_command_executor import GenGtkmmCommandExecutor

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_gtkmm'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_gtkmm/blob/dev/LICENSE'
__version__ = '1.0.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenGtkmmBundleFactory:
    '''
        Factory for creating the gen_gtkmm bundle.

        It defines:

            :attributes:
                | _info_file - Path to the gen_gtkmm info file.
            :methods:
                | create_bundle - Creates the gen_gtkmm bundle with optional pre-configured options.
    '''

    _info_file: str = 'gen_gtkmm/infrastructure/config/gen_gtkmm.cfg'

    @classmethod
    def create_bundle(cls, options: GenGtkmmBundleOptions | None = None) -> GenGtkmmBundle:
        '''
            Creates the gen_gtkmm bundle with optional pre-configured options.

            :param options: The pre-configured options for the gen_gtkmm bundle.
            :return: The gen_gtkmm bundle.
            :exceptions:
                | ATSValueError: The gen_gtkmm bundle options must be provided and have proper values.
                | ATSTypeError:  The gen_gtkmm bundle options must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_gtkmm bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The gen_gtkmm bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_gtkmm bundle must be provided and have proper values.
                | ATSTypeError:  The gen_gtkmm bundle must be an instance of GenGtkmmBundle and
                |                its attributes must be instances of their respective types.
        '''
        if options is not None:
            GenGtkmmBundleOptionsValidator.validate(options)

        info_file = options.get(GenGtkmmBundleKeys.OPTION_INFO_FILE) if options else cls._info_file

        context_bundle: ContextBundle = ContextBundleFactory.create_bundle()

        base_bundle: BaseBundle = BaseBundleFactory.create_bundle(
            options=BaseBundleOptions(
                info_file=info_file,
                use_generator=True,
                context_bundle=context_bundle
            )
        )

        subprocessor: SubProcessor = SubProcessor(generator=base_bundle.generation_manager)

        service: Service = Service(subprocessor=subprocessor)

        gen_gtkmm_definition: GenGtkmmCommandDefinition = GenGtkmmCommandDefinition()

        gen_gtkmm_bundle: CommandBundle = CommandBundle(
            definition=gen_gtkmm_definition,
            executor=GenGtkmmCommandExecutor(gen_gtkmm_definition)
        )

        cli_bundle: CLIBundle = CLIBundleRegistry.create_bundle(
            dependencies=CLIBundleDependencies(
                service=service,
                parser=base_bundle.option_manager,
                commands=[gen_gtkmm_bundle]
            )
        )

        cli: CLI = CLI(cli_bundle)

        return GenGtkmmBundleRegistry.create_bundle(
            dependencies=GenGtkmmBundleDependencies(
                base=base_bundle,
                service=service,
                subprocessor=subprocessor,
                cli=cli
            )
        )
