import ast
import inspect
import unittest

from docs.classes import Class


class ClassConstructionTest(unittest.TestCase):
  def test_can_construct_class_with_ast(self):
    _class = ast.parse("""class foo(object):\n  pass""").body[0]
    assert Class(ast_node=_class)


  def test_can_construct_function_with_ast_source(self):
    assert Class(source="""class foo(object):\n  pass""")


  def test_cannot_construct_function_with_non_func(self):
    fun = ast.parse("""def foo():\n  pass""").body[0]
    self.assertRaises(TypeError, Class, ast_node=fun)


  def test_cannot_contruct_function_with_non_func_source(self):
    f = Class(source="""def foo():\n  pass""")
    self.failUnlessRaises(TypeError, getattr, f, 'parsed')


class ClassTest(unittest.TestCase):
  """This is a test docstring"""

  def setUp(self):
    self._source = """class foo(object):\n  pass"""
    self._ast = ast.parse(self._source).body[0]
    self._class = Class(source=self._source, ast_node=self._ast)


  def test_construct_class(self):
    assert self._class


  def test_class_name(self):
    assert self._class.name == 'foo'


  def test_class_docstring(self):
    class FooClass(object):
      """This is a test docstring"""
      pass

    _class = Class(source='\n'.join([x[4:] for x in
      inspect.getsource(FooClass).split('\n')
    ]))
    assert _class.docstring == 'This is a test docstring'

