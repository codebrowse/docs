"""DAO (Data-access object) for Python imports.

Inherits from `docs.visitors.node.Node`

**Warning!**: This module uses `__import__` to actively import modules into
              your current namespace.  Be sure to *only import modules you
              trust*.

### Attributes

- `source`:   Source code representation of the object.
- `_ast_obj`: Original `ast.AST` object.
- `_import`:  The object being imported
- `path`:     Python path of the import
- `alias`:    The name the import is bound to in context.

### Examples

>>> from docs.modules import Module
>>> m = Module(filename='docs/imports/_import.py')
>>> len(m.imports)
2
"""

from collections import deque
import ast
import inspect

from docs.visitors import Node

class Import(Node):
  """Wraps `ast.Import` and `ast.FromImport` objects"""

  def __init__(self, ast_node, *args, **kw):
    super(Import, self).__init__(*([ast_node._ast_obj] + list(args)), **kw)

  def __repr__(self, *args, **kw):
    return '<[%s] %s>' % (
      self._ast_obj.__class__.__name__,
      self.path
    )


  @property
  def _import(self):
    """Attempts to actually import the object in question"""

    from docs.modules import Module

    if isinstance(self._ast_obj, ast.Import):
      return __import__(self._ast_obj.names[0].name)

    elif isinstance(self._ast_obj, ast.ImportFrom):
      # Pop the modules into a queue
      name = deque(self._ast_obj.module.split('.'))
      print self._ast_obj.module
      # ...keep importing modules until there aren't any left..
      mod = __import__(name.popleft())
      while len(name):
        mod = getattr(mod, name.popleft())

      # ...and if there is a `name` component, grab it!
      if hasattr(mod, self._ast_obj.names[0].name):
        return getattr(mod, self._ast_obj.names[0].name)

      return mod


  @property
  def alias(self):
    """The name the import is bound to (in context)"""

    if self._ast_obj.names[0].asname:
      return self._ast_obj.names[0].asname

    if has_attr(self._ast_obj, 'module'):
      return '.'.join((self._ast_obj.module, self._ast_obj.names[0].name))

    return self._ast_obj.names[0].name


  @property
  def path(self):
    """The python path of the import"""

    if hasattr(self._ast_obj, 'module'):
      return '.'.join((self._ast_obj.module, self._ast_obj.names[0].name))

    return self._ast_obj.names[0].name


  @property
  def source(self):
    return inspect.getsource(self._import)
