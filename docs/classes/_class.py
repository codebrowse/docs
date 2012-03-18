import ast

from docs.visitors.base import VisitorBase

class Class(VisitorBase):
  """Wraps `ast.ClassDef` objects"""

  def __init__(self, ast_node=None, source=None, *args, **kw):
    if ast_node and not isinstance(ast_node, ast.ClassDef):
      raise TypeError('Expected an ast.ClassDef object')

    super(Class, self).__init__(ast_node=ast_node, source=source)


  def __repr__(self, *args, **kw):
    return '<[Class] %s>' % (self.name, )


  @property
  def name(self):
    return self.parsed.name


  @property
  def inherits(self):
    return [x.id for x in self.parsed.bases]


  def parse(self):
    if not self._parsed:
      assert self._source
      self._parsed = ast.parse(self._source)

      assert len(self._parsed.body) == 1, 'Expected just one function definition!'
      if not isinstance(self._parsed.body[0], ast.ClassDef):
        raise TypeError('Expected an ast.ClassDef!')

      self._parsed = self._parsed.body[0]

    return self._parsed

