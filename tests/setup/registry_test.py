# -*- coding: UTF-8 -*-

'''
Module
    registry_test.py
Info
    Unit tests for GenGtkmmBundleRegistry class.
'''

from __future__ import annotations

import unittest
from unittest.mock import Mock

from ats_utilities.base.setup.bundle import BaseBundle

from gen_gtkmm.core.service.iservice import IService
from gen_gtkmm.core.service.isubprocessor import ISubProcessor
from gen_gtkmm.infrastructure.cli.icli import ICLI
from gen_gtkmm.setup.bundle import GenGtkmmBundle
from gen_gtkmm.setup.registry import GenGtkmmBundleRegistry


class DummyService:

    def execute(self, *, params: object) -> object:
        return None

    def is_initialized(self) -> bool:
        return True


class DummySubProcessor:

    def run(self, *, params: object) -> dict[str, object]:
        return {}

    def is_initialized(self) -> bool:
        return True


class DummyCLI:

    def run(self) -> dict[str, object]:
        return {}

    def is_initialized(self) -> bool:
        return True


class TestGenGtkmmBundleRegistry(unittest.TestCase):

    def test_create_bundle_success(self) -> None:
        mock_base = Mock(spec=BaseBundle)
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI()

        dependencies = {
            'base': mock_base,
            'service': dummy_service,
            'subprocessor': dummy_subprocessor,
            'cli': dummy_cli
        }
        
        bundle = GenGtkmmBundleRegistry.create_bundle(dependencies)
        self.assertIsInstance(bundle, GenGtkmmBundle)
        self.assertEqual(bundle.base, mock_base)

    def test_create_bundle_invalid_dependencies(self) -> None:
        with self.assertRaises(Exception):
            GenGtkmmBundleRegistry.create_bundle(None)

    def test_get_version(self) -> None:
        self.assertEqual(GenGtkmmBundleRegistry.get_version(), '1.1.9')
