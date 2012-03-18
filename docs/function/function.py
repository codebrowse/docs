import ast

from docs.visitors.base import VisitorBase


class Function(VisitorBase):
  """Wraps `ast.FunctionDef` objects"""

  def __init__(self, ast_node=None, source=None, *args, **kw):
    if ast_node and not isinstance(ast_node, ast.FunctionDef):
      raise TypeError('Expected an ast.FunctionDef object')

    super(Function, self).__init__(ast_node=ast_node, source=source)


  def __repr__(self, *args, **kw):
    return '<[Function] %s>' % (self.parsed.name, )


  @property
  def name(self):
    return self.parsed.name


  def parse(self):
    if not self._parsed:
      assert self._source
      self._parsed = ast.parse(self._source)

      assert len(self._parsed.body) == 1, \
        'Expected just one function definition!'

      if not isinstance(self._parsed.body[0], ast.FunctionDef):
        raise TypeError('Expected an ast.FunctionDef!')

      self._parsed = self._parsed.body[0]

    return self._parsed


  @property
  def arguments(self, *args, **kw):
    args = QueryConstructor()
    args.visit(self.parsed)

    return args.results


  @property
  def callers(self, *args, **kw):
    """Places where this function is called"""
    raise NotImplementedError
