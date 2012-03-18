import ast
import inspect
import unittest

from docs.imports import Import
from docs.module import Module


def test_construct_mod():
  with open(__file__, 'r') as file_obj:
    source = file_obj.read()

  mod = Module(source=source, ast_node=ast.parse(source))
  assert isinstance(mod.imports[0], Import)


class TestImport(unittest.TestCase):
  def setUp(self):

    with open('test/imports/from_import_a.py', 'r') as file_obj:
      self.source = file_obj.read()
    self.mod = Module(source=self.source, ast_node=ast.parse(self.source))
    self._import = self.mod.imports[0]

  def test_from_import_a_module(self):
    assert self._import.module == 'docs', 'module name does not match'


  def test_from_import_a_import(self):
    assert self._import._import == __import__('docs').module, \
      '_import attribute is wrong'


  def test_from_import_a_path(self):
    assert self._import.path== 'docs.module', 'path is incorrect'


class TestImportAs(unittest.TestCase):
  def setUp(self):
    with open('test/imports/from_import_as_a.py', 'r') as file_obj:
      self.source = file_obj.read()

    self.mod = Module(source=self.source)
    self._import = self.mod.imports[0]


  def test_from_import_as_a_module(self):
    assert self._import.path == 'docs.module', 'path is incorrect'


  def test_from_import_as_a_alias(self):
    assert self._import.alias == 'm'


  def test_from_import_as_a_import(self):
    assert self._import._import == __import__('docs').module
