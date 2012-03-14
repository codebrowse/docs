import ast
import inspect
import os

#from docs.classes import Class
#from docs.function import Function
from docs.imports import Import
from docs.visitors import Node
from docs.module import Module


def get(*args, **kw):
  item = kw.get('item') or len(args) and args[0] or None
  path = kw.get('path')
  filename = kw.get('filepath')

  if not len(args):
    return

  if isinstance(item, (Module, Import)):
    return item

  elif path:
    path = Import(Node(ast.parse('import %s' % (path, )).body[0]))
    return get(path._import)

  elif inspect.ismodule(item):
    file_str = item.__file__
    if file_str.endswith('.pyc'):
      file_str = file_str[:-1]
    print file_str
    return Module(filename=file_str)

  elif os.path.isdir(filename):
    return Module(filename=os.path.join(filename, '__init__.py'))

  elif isinstance(item, ast.AST):
    if isinstance(item, ast.Import):
      return Import(item)
    return Node(item)

  elif isinstance(item, (list, tuple)):
    return [get(y) for y in item]

  #elif inspect.isclass(item):
  #  return Class(item)

  #elif inspect.isfunction(item):
  #  return Function(item):

  return item


def imports(node):
  #TODO(mvv): add function and class
  node = get(node)
  if isinstance(node, Module):
    return node.imports
  raise TypeError('must be Module, Function, or Class')
