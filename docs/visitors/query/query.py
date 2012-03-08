import ast

from docs.visitors.query.node import Node


def safe_eval(query, node, *args, **kw):
  """Safe evaluation helper function.

  Includes the `ast` module in global scope.  Supplied function keyword
  arguments are included as locals.

  The `node` variable
  """
  #TODO(mvv): assert node type is an ast type
  kw.update({'node': node})
  return eval(query, {'ast': ast}, kw)


class QueryVisitor(ast.NodeVisitor):
  """Queryable interface into the AST

  >>> import inspect
  >>> q = QueryVisitor('isinstance(node, ast.FunctionDef)')
  >>> q.visit(ast.parse(inspect.getsource(ast)))
  >>> len(q.results)
  16
  """
  def __init__(self, query, *args, **kw):
    super(QueryVisitor, self).__init__(*args, **kw)
    self._nodes = []
    self._query = query


  def generic_visit(self, node, *args, **kw):
    if safe_eval(self._query, node):
      self._nodes.append(Node(node))

    super(QueryVisitor, self).generic_visit(node, *args, **kw)

  @property
  def results(self):
    return self._nodes
