import ast
import inspect
import unittest

from docs.function import Function


class FunctionConstructionTest(unittest.TestCase):
  def test_can_construct_function_with_ast(self):
    fun = ast.parse("""def foo():\n  pass""").body[0]
    assert Function(ast_node=fun)


  def test_can_construct_function_with_ast_source(self):
    assert Function(source="""def foo():\n  pass""")


  def test_cannot_construct_function_with_non_func(self):
      fun = ast.parse("""class foo(object):\n  pass""").body[0]
      self.assertRaises(TypeError, Function, ast_node=fun)


  def test_cannot_contruct_function_with_non_func_source(self):
    f = Function(source="""class foo(object):\n  pass""")

    self.assertRaises(TypeError, getattr, f, 'parsed')


class FunctionTest(unittest.TestCase):
  def setUp(self):
    self._source = """def foo():\n  pass"""
    self._ast = ast.parse(self._source).body[0]
    self._fun = Function(source=self._source, ast_node=self._ast)


  def test_construct_fun(self):
    assert self._fun


  def test_fun_name(self):
    assert self._fun.name == 'foo'


  def test_fun_docstring(self):
    """This is a test docstring"""
    fun = Function(source='\n'.join([x[2:] for x in
      inspect.getsource(self.test_fun_docstring).split('\n')
    ]))
    assert fun.docstring == 'This is a test docstring'

