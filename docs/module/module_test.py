"""Unit tests for Module class"""
import os

__author__ = ['Michael Van Veen (michael@mvanveen.net)']

def test_can_construct_module():
  """Module doc object can be constructed with kwargs"""

  mod = Module(name='module_test`', filepath=os.path.abspath(__file__))
  assert mod, 'Could not construct module!'


#is this one important? Might just need to be handled in api
def test_can_construct_module_with_mod():
  """Module doc object can be constructed with filepath"""

  mod = Module(__file__)
  assert mod, 'Could not construct module!'


def test_can_get_author():
  mod = module(__file__)
  assert any(['Michael Van Veen' in author for author in mod.authors]), \
    "Expected 'Michael Van Veen' to be in AUTHORS"


def test_can_get_version():
  #todo: grab top-level init
  pass


def test_can_get_imports():
  assert os in mod.imports, \
    "Did not see os module as an import, but it is declared!"


def test_can_get_vars():
  assert __author__ in mod.vars, \
    "Expected '__author__' in module variables!"


def test_repr():
  doc = module(__file__)

  assert str(doc) == '<[module] module_tet>', 'did not get expected repr result'


