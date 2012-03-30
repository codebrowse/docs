import ast

import docs as d
from docs.classes import Class
from docs.function import Function
from docs.modules import Module


def test_can_get_functions():
  print d
  print d.get_functions(d)

  assert len(d.get_functions(d)) == 4


def test_can_get_imports():
  assert len(d.get_imports(filename='docs/__init__.py')) == 10


def test_can_get_classes():
  assert len(d.get_classes('ast')) == 2


def test_can_get_ast_module():
  assert isinstance(d.get(item=ast.parse('from x import y')), Module)


def test_can_get_ast_function():
  from docs.function import Function
  assert isinstance(d.get(item=ast.parse('def foo():\n  pass').body[0]), Function)


def test_can_get_ast_class():
  from docs.classes import Class
  assert isinstance(d.get(item=ast.parse('class Foo(object):\n  pass').body[0]), Class)


def test_can_get_ast_import():
  from docs.imports import Import
  assert isinstance(d.get(item=ast.parse('import y').body[0]), Import)


def test_can_get_ast_import_from():
  from docs.imports import Import
  assert isinstance(d.get(item=ast.parse('from x import y').body[0]), Import)


def test_can_get_docs_str():
  assert d.get('ast')


def test_can_get_docs():
  assert isinstance(d.get(Module(filename='docs/modules/module.py')), Module)


def test_can_get_docs_str():
  assert d.get('ast')


def test_can_get_docs_local_path():
  assert d.get(path='docs.modules')


def test_can_get_docs_str():
  assert d.get(filename='docs/modules/module.py')


def test_docs_can_get_file_dir():
  assert d.get(filename='docs/modules/')


def test_can_get_class():
  class Foo(object):
    pass

  assert isinstance(d.get(Foo), Class)


def test_can_get_function():
  def foo():
    pass

  assert isinstance(d.get(foo), Function)


def test_can_get_none():
  assert not d.get()

