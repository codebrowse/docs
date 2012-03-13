"""DAO (Data-access object) for Python imports.

Inherits from `docs.visitors.node.Node`.

### Attributes:

- `module`: The module being imported, or the module from which the import
            originates.
- `name`:   The name that the import is bound to.
- `value`:  The result of the import (function, object, class, ???).

### Examples


"""
from collections import deque
import ast

from docs.visitors import Node

class Import(Node):
  """Wraps `ast.Import` and `ast.FromImport` objects

     >>> from docs.module import Module
     >>> m = Module(filename='docs/imports/_import.py')
     >>> len(m.imports)
     2

  """

  def __init__(self, ast_node, *args, **kw):
    super(Import, self).__init__(*([ast_node._ast_obj] + list(args)), **kw)

  def __repr__(self, *args, **kw):
    return '<[%s] %s>' % (
      self._ast_obj.__class__.__name__,
      self.path
    )


  @property
  def _import(self):
    from docs.module import Module

    if isinstance(self._ast_obj, ast.Import):
      return __import__(self._ast_obj.names[0].name)

    elif isinstance(self._ast_obj, ast.ImportFrom):
      name = deque(self._ast_obj.module.split('.'))
      mod = __import__(name.popleft())
      while len(name):
        mod = getattr(mod, name.popleft())

      if hasattr(mod, self._ast_obj.names[0].name):
        return getattr(mod, self._ast_obj.names[0].name)

      return mod

  @property
  def alias(self):
    if self._ast_obj.names[0].asname:
      return self._ast_obj.names[0].asname


    if has_attr(self._ast_obj, 'module'):
      return '.'.join((self._ast_obj.module, self._ast_obj.names[0].name))

    return self._ast_obj.names[0].name


  @property
  def path(self):
    if hasattr(self._ast_obj, 'module'):
      return '.'.join((self._ast_obj.module, self._ast_obj.names[0].name))

    return self._ast_obj.names[0].name
