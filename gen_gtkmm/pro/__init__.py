# -*- coding: UTF-8 -*-

'''
 Module
     __init__.py
 Copyright
     Copyright (C) 2021 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Defined class GtkMMSetup with attribute(s) and method(s).
     Created API for generating GTK+ project skeleton.
'''

import sys

try:
    from pathlib import Path
    from gen_gtkmm.pro.config import ProConfig
    from gen_gtkmm.pro.config.pro_name import ProName
    from gen_gtkmm.pro.read_template import ReadTemplate
    from gen_gtkmm.pro.write_template import WriteTemplate
    from ats_utilities.checker import ATSChecker
    from ats_utilities.config_io.base_check import FileChecking
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config_io.yaml.yaml2object import Yaml2Object
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2021, https://electux.github.io/gen_gtkmm'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/electux/gen_gtkmm/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GtkMMSetup(FileChecking, ProConfig, ProName):
    '''
        Defined class GtkMMSetup with attribute(s) and method(s).
        Created API for generating GTK+ project skeleton.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
                | PRO_STRUCTURE - project setup (templates, modules).
                | __reader - reader API.
                | __writer - writer API.
            :methods:
                | __init__ - initial constructor.
                | get_reader - getter for template reader.
                | get_writer - getter for template writer.
                | gen_pro_setup - generate project skeleton.
                | __str__ - dunder method for GtkMMSetup.
    '''

    GEN_VERBOSE = 'GEN_GTKMM::PRO::GTKMM_SETUP'
    PRO_STRUCTURE = '/../conf/project.yaml'

    def __init__(self, project_name, verbose=False):
        '''
            Initial constructor.

            :param project_name: project name.
            :type project_name: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('str:project_name', project_name)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        FileChecking.__init__(self, verbose=verbose)
        ProConfig.__init__(self, verbose=verbose)
        ProName.__init__(self, verbose=verbose)
        verbose_message(GtkMMSetup.GEN_VERBOSE, verbose, 'init generator')
        self.__reader = ReadTemplate(verbose=verbose)
        self.__writer = WriteTemplate(verbose=verbose)
        project_structure = '{0}{1}'.format(
            Path(__file__).parent, GtkMMSetup.PRO_STRUCTURE
        )
        self.check_path(file_path=project_structure, verbose=verbose)
        self.check_mode(file_mode='r', verbose=verbose)
        self.check_format(
            file_path=project_structure, file_format='yaml', verbose=verbose
        )
        if self.is_file_ok():
            yml2obj = Yaml2Object(project_structure)
            self.config = yml2obj.read_configuration()
            self.pro_name = project_name

    def get_reader(self):
        '''
            Getter for template reader.

            :return: template reader object.
            :rtype: <ReadTemplate>
            :exceptions: None
        '''
        return self.__reader

    def get_writer(self):
        '''
            Getter for template writer.

            :return: template writer object.
            :rtype: <WriteTemplate>
            :exceptions: None
        '''
        return self.__writer

    def gen_pro_setup(self, verbose=False):
        '''
            Generate project structure.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: boolean status, True (success) | False.
            :rtype: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        '''
        status = False
        templates = self.__reader.read(self.config, verbose=verbose)
        if bool(templates):
            status = self.__writer.write(
                templates, self.pro_name, verbose=verbose
            )
        return status

    def __str__(self):
        '''
            Dunder method for GtkMMSetup.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2}, {3}, {4}, {5})'.format(
            self.__class__.__name__, FileChecking.__str__(self),
            ProConfig.__str__(self), ProName.__str__(self),
            str(self.__reader), str(self.__writer)
        )