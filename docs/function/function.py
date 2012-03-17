import ast

from docs.visitors.base import VisitorBase

class Function(VisitorBase):
  """Wraps `ast.FunctionDef` objects"""

  def __init__(self, ast_node=None, source=None, *args, **kw):
    super(Function, self).__init__(ast_node=ast_node, source=source)


  def __repr__(self, *args, **kw):
    return '<[Function] %s>' % (self.parsed.name, )


  @property
  def name(self):
    return self.parsed.name


  @property
  def arguments(self, *args, **kw):
    args = QueryConstructor()
    args.visit(self.parsed)

    return args.results


  @property
  def docstring(self):
    """Returns the module-level docstring."""
    return ast.get_docstring(self.parsed)


  def callers(self, *args, **kw):
    """Places where this function is called"""
    raise NotImplementedError
