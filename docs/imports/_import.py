"""DAO (Data-access object) for Python imports.

Inherits from `docs.visitors.node.Node`.

### Attributes:

- `module`: The module being imported, or the module from which the import
            originates.
- `name`:   The name that the import is bound to.
- `value`:  The result of the import (function, object, class, ???).
"""

import ast

from docs.visitors import Node

class Import(Node):
  """Wraps `ast.Import` and `ast.FromImport` objects"""

  def __init__(self, ast_node, *args, **kw):
    super(Import, self).__init__(ast_node._ast_obj, *args, **kw)


  @property
  def _import(self):
    from docs.module import Module

    if isinstance(self._ast_obj, ast.Import):
      return __import_(self._ast_obj.names[0].name)

    elif isinstance(self._ast_obj, ast.ImportFrom):
      return __import__(name=self._ast_obj.module)


  @property
  def name(self):
    if self._ast_obj.names[0].asname:
      return self._ast_obj.names[0].asname
    return self._ast_obj.names[0].name
