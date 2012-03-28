"""Python Docs: A Python Documentation API for Developers"""

import ast
import inspect
import os
import sys

from docs.classes import Class
from docs.function import Function
from docs.imports import Import
from docs.visitors import Node
from docs.modules import Module

__author__    = 'Michael Van Veen (michael@mvanveen.net)'
__copyright__ = 'Copyright 2012, Michael Van Veen'
__license__   = 'MIT'
__version__   = '0.1'
__email__     = "pythondocs@mvanveen.net"
__status__    = "Beta"

def get(*args, **kw):
  """Main accessor into Python docs

  ## Examples

  ** Parse a live Python object **
  >>> import docs
  >>> docs.get(docs)
  <[Module] docs/__init__.py>

  ** Parse file name**
  >>> import docs as d
  >>> m  = d.get(filename='docs/modules/module.py')
  >>> m
  <[Module] docs/modules/module.py>
  >>> m.docstring
  'Wrapper object for Python modules'

  """

  item = kw.get('item') or len(args) and args[0] or None
  path = kw.get('path')
  filename = kw.get('filename')

  if not len(args) and not (item or path or filename):
    return

  if isinstance(item, basestring):
    if item in sys.modules.keys():
      return get(path=item)

  if isinstance(item, (Module, Import)):
    return item

  elif path:
    path = Import(Node(ast.parse('import %s' % (path, )).body[0]))
    return get(path._import)

  elif inspect.ismodule(item):
    file_str = inspect.getsourcefile(item)
    return Module(filename=file_str)

  elif filename:
    if os.path.isdir(filename):
      return Module(filename=os.path.join(filename, '__init__.py'))
    return Module(filename=filename)

  elif isinstance(item, ast.AST):
    if isinstance(item, ast.Module):
      return Module(ast_node=item)

    elif isinstance(item, (ast.Import, ast.ImportFrom)):
      return Import(Node(item))

    elif isinstance(item, ast.ClassDef):
      return Class(item)

    elif isinstance(item, ast.FunctionDef):
      return Function(item)

    return Node(item)


  elif isinstance(item, (list, tuple)):
    return [get(y) for y in item]

  elif inspect.isclass(item):
    source = inspect.getsource(item)
    return Class(source=source)


  elif inspect.isfunction(item):
    source = inspect.getsource(item)
    return Function(source=source)

  return item


def get_imports(*args, **kw):
  """Returns the imports declared for a function, class or module"""

  node = get(*args, **kw)
  if isinstance(node, (Module, Class, Function)):
    return node.imports
  raise TypeError('must be Module, Function, or Class')


def get_functions(*args, **kw):
  """Returns the functions declared for a function, class or module"""

  node = get(*args, **kw)
  if isinstance(node, (Module, Class, Function)):
    return node.functions
  raise TypeError('must be Module, Function, or Class')


def get_classes(*args, **kw):
  """Returns the classes declared for a function, class or module"""

  node = get(*args, **kw)
  if isinstance(node, (Module, Class, Function)):
    return node.classes

  raise TypeError('must be Module, Function, or Class')

#def testget_sys_modules():
#  import sys
#  for name, value in sys.modules.iteritems():
#    print name
#    print get(value)
#
