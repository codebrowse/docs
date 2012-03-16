import ast
import inspect
import unittest

from docs.visitors.base import VisitorBase, NoSourceCodeError
from docs.visitors.node import Node

def test_can_construct_base():
  a = ast.parse(inspect.getsource(ast))
  assert VisitorBase(a)


def test_can_construct_base_with_node():
  n = Node(ast.parse(inspect.getsource(ast)))
  assert VisitorBase(n)

class VisitorBaseTest(unittest.TestCase):

  def setUp(self):
    self.a = ast.parse(inspect.getsource(ast))
    self.v = VisitorBase(self.a)


  def test_can_get_imports(self):
    assert len(self.v.imports) == 4, 'Expected 4 imports in AST module!'


  def test_can_get_imports(self):
    assert len(self.v.functions) == 16, \
      'Espected 16 function defs in AST module!'


  def test_can_get_docstring(self):
    assert self.v.docstring.split('\n')[0] == 'ast'


  def test_can_get_docstring(self):
    with self.assertRaises(NoSourceCodeError):
      self.v.source
