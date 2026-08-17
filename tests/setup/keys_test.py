# -*- coding: UTF-8 -*-

'''
Module
    keys_test.py
Info
    Unit tests for GenGtkmmBundleKeys class.
'''

from __future__ import annotations

import unittest
from types import MappingProxyType

from gen_gtkmm.setup.keys import GenGtkmmBundleKeys


class TestGenGtkmmBundleKeys(unittest.TestCase):

    def test_get_dependency_to_type(self) -> None:
        deps = GenGtkmmBundleKeys.get_dependency_to_type()
        self.assertIsInstance(deps, MappingProxyType)
        self.assertIn(GenGtkmmBundleKeys.DEPENDENCY_BASE, deps)
        self.assertIn(GenGtkmmBundleKeys.DEPENDENCY_SERVICE, deps)
        self.assertIn(GenGtkmmBundleKeys.DEPENDENCY_SUBPROCESSOR, deps)
        self.assertIn(GenGtkmmBundleKeys.DEPENDENCY_CLI, deps)

    def test_get_option_to_type(self) -> None:
        opts = GenGtkmmBundleKeys.get_option_to_type()
        self.assertIsInstance(opts, MappingProxyType)
        self.assertIn(GenGtkmmBundleKeys.OPTION_INFO_FILE, opts)
