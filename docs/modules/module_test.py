"""Unit tests for Module class"""

import ast
import inspect
import os
import unittest

from docs.modules import Module

__author__     = ['Michael Van Veen (michael@mvanveen.net)']
__copyright__  = 'Copyright 2012, Michael Van Veen'
__license__    = 'MIT'
__version__    = '0.1'
__maintainer__ = ["Michael Van Veen (michael@mvanveen.net)"]
__credits__    = ['foo']
__email__      = "pythondocs@mvanveen.net"
__status__     = "Beta"


class TestConstructModule(unittest.TestCase):
  def test_can_construct_filenamet(self):
    mod = Module(filename=__file__)


  def test_can_construct_filenamet(self):
    mod = Module(path='docs.modules.module_test')


  def test_can_construct_filenamet(self):
    with open(__file__, 'r') as file_obj:
      source = file_obj.read()
    mod = Module(source=source)


  def test_can_construct_filenamet(self):
    with open(__file__, 'r') as file_obj:
      node = ast.parse(file_obj.read())
    mod = Module(ast_node=node)


class TestModule(unittest.TestCase):
  def setUp(self):
    self.mod = Module(filename=__file__)


  def test_can_get_authors(self):
    assert any(['Michael Van Veen' in author for author in self.mod.authors]), \
      "Expected 'Michael Van Veen' to be in AUTHORS"


  def test_can_get_docstring(self):
   """Can get a module docstring"""
   with open(__file__, 'r') as file_obj:
     assert self.mod.docstring == ast.get_docstring(
      ast.parse(file_obj.read())
    ), 'Docstring does not match!'


  def test_can_get_version(self):
    #TODO: grab top-level init/include packages
    assert self.mod.version == ['0.1'], 'Unexpected version value'


  def test_can_get_credits(self):
    assert self.mod.credits == ['foo'], 'Unexpected credits value'


  def test_can_get_maintainer(self):
    assert any(['Michael Van Veen' in x for x in self.mod.maintainer]), \
      'Did not get expected maintainer!'


  def test_can_get_email(self):
    assert self.mod.email == ['pythondocs@mvanveen.net']


  def test_can_get_status(self):
    assert self.mod.status == ['Beta']


  def test_str(self):
    with open(__file__, 'r') as file_obj:
      assert str(self.mod) == file_obj.read()


  def test_can_get_imports(self):
    assert os in [x._import for x in self.mod.imports], \
      "Did not see os module as an import, but it is declared!"


  def test_can_get_functions(self):
    assert 'test_can_get_functions' in [x.name for x in self.mod.functions]


  def test_repr(self):
    print self.mod.__repr__()
    assert self.mod.__repr__() == \
      '<[Module] docs/modules/module_test.py>'
