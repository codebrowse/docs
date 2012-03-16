import ast
import inspect
import unittest

from docs.visitors.base import VisitorBase
from docs.visitors.node import Node

def test_can_construct_base():
  a = ast.parse(inspect.getsource(ast))
  assert VisitorBase(a)


def test_can_construct_base_with_node():
  n = Node(ast.parse(inspect.getsource(ast)))
  assert VisitorBase(n)


def test_can_get_imports():
  a = ast.parse(inspect.getsource(ast))
  v = VisitorBase(a)
  assert len(v.imports) == 4, 'Expected 4 imports in AST module!'


def test_can_get_imports():
  a = ast.parse(inspect.getsource(ast))
  v = VisitorBase(a)
  assert len(v.functions) == 16, 'Espected 16 function defs in AST module!'


def test_can_get_docstring():
  a = ast.parse(inspect.getsource(ast))
  v = VisitorBase(a)
  assert v.docstring.split('\n')[0] == 'ast'
