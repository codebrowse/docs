import ast

from docs.visitors.function import FunctionVisitor
from docs.visitors._import import ImportVisitor
from docs.visitors.query import Node

class Function(ImportVisitor, FunctionVisitor, Node):
  """Wraps `ast.FunctionDef` objects"""

  def __init__(self, ast_node, *args, **kw):
    super(Function, self).__init__(*([ast_node._ast_obj] + list(args)), **kw)


  def __repr__(self, *args, **kw):
    return '<[Function] %s>' % (self._ast_obj.name, )


  @property
  def arguments(self, *args, **kw):
    args = QueryConstructor()
    args.visit(self.parsed)

    return args.results


  @property
  def docstring(self):
    """Returns the module-level docstring."""
    return ast.get_docstring(self._ast_obj)


  def callers(self, *args, **kw):
    """Places where this function is called"""
    raise NotImplementedError
