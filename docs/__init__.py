"""Python Docs: A Python Documentation API for Developers

Python has wonderful, first-class support for documentation. Unfortunately,
this incredibly thoughtful feature of the language is hidden behind large, monolithic
suites or outdated, unsupported pieces of spaghetti. Up until now, we haven’t had easy
programatic access to our source code and documentation.

No longer. Docs is a Python Documentation API I for Developers. Our language is dynamic.
It’s time for our documentation to start acting like it.

## Examples

** Parse a live Python object **
>>> import docs
>>> docs.get(docs)
<[Module] __init__>

** Parse file name**

>>> import docs
>>> m  = docs.get(filename='docs/module/module.py')
>>> m
<[Module] module>
>>> m.docstring
'Wrapper object for Python modules'
"""

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
  filename = kw.get('filename')

  if not len(args) and not (item or path or filename):
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
    return Module(filename=file_str)

  elif os.path.isdir(filename):
    return Module(filename=os.path.join(filename, '__init__.py'))

  elif filename:
    return Module(filename=filename)

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
