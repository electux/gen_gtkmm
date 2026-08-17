# -*- coding: UTF-8 -*-

'''
Module
    factory_test.py
Info
    Unit tests for GenGtkmmBundleFactory class.
'''

from __future__ import annotations

import unittest

from gen_gtkmm.setup.bundle import GenGtkmmBundle
from gen_gtkmm.setup.factory import GenGtkmmBundleFactory


class TestGenGtkmmBundleFactory(unittest.TestCase):

    def test_create_bundle_default(self) -> None:
        bundle = GenGtkmmBundleFactory.create_bundle()
        self.assertIsInstance(bundle, GenGtkmmBundle)

    def test_create_bundle_with_options(self) -> None:
        options = {'info_file': 'gen_gtkmm/infrastructure/config/gen_gtkmm.cfg'}
        bundle = GenGtkmmBundleFactory.create_bundle(options)
        self.assertIsInstance(bundle, GenGtkmmBundle)

    def test_create_bundle_invalid_options(self) -> None:
        options = {'info_file': 123}
        with self.assertRaises(Exception):
            GenGtkmmBundleFactory.create_bundle(options)

    def test_get_version(self) -> None:
        self.assertEqual(GenGtkmmBundleFactory.get_version(), '1.1.9')
