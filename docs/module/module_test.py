"""Unit tests for Module class"""

import ast
import inspect
import os
import unittest

from docs.module import Module

__author__     = ['Michael Van Veen (michael@mvanveen.net)']
__copyright__  = 'Copyright 2012, Michael Van Veen'
__license__    = 'MIT'
__version__    = '0.1'
__maintainer__ = ["Michael Van Veen (michael@mvanveen.net)"]
__credits__    = ['foo']
__email__      = "pythondocs@mvanveen.net"
__status__     = "Beta"


def test_can_construct_module():
  """Module doc object can be constructed with kwargs"""
  mod = Module(name='module_test', filename=__file__)
  assert mod, 'Could not construct module!'


class TestModule(unittest.TestCase):
  def setUp(self):
    self.mod = Module(name='module_test', filename=__file__)


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
    assert self.mod.version


  def test_can_get_credits(self):
    assert self.mod.credits


  def test_can_get_maintainer(self):
    assert self.mod.maintainer


  def test_can_get_email(self):
    assert self.mod.email


  def test_can_get_status(self):
    assert self.mod.status


  def test_str(self):
    with open(__file__, 'r') as file_obj:
      assert str(self.mod) == file_obj.read()


  def test_can_get_imports(self):
    print self.mod.imports[3].names[0]._fields
    assert False
    assert os in mod.imports, \
      "Did not see os module as an import, but it is declared!"


#def test_can_get_vars():
#  assert '__author__' in self.mod.vars, \
#    "Expected '__author__' in module variables!"
#

