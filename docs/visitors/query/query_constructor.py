"""A Queryable interface into the Python AST.

Given an ast type and keyword arguments, the QueryConstructor attempts to
construct a query string which can be checked (read: eval'd (hopefully
safely?)) against a given AST.

## Examples

**Get function definitions from `ast` module**

    >>> import ast
    >>> import inspect
    >>> source = ast.parse(inspect.getsource(ast))
    >>> q = QueryConstructor(ast.FunctionDef)
    >>> q.visit(source)
    >>> len(q.results)
    16

**Get function definition from `ast` module at line 32**

    >>> q = QueryConstructor(ast.FunctionDef, lineno=32)
    >>> q.visit(source)
    >>> len(q.results)
    1

**Look for imports, find the name of the first import**

    >>> q = QueryConstructor(ast.Import)
    >>> q.visit(source)
    >>> q.results[0].names[0].name
    'inspect'

**Get the value of the `__author__` variable of module**

    >>> q = QueryConstructor(ast.Name, id='__author__')
    >>> q.visit(ast.parse(inspect.getsource(inspect)))
    >>> len(q.results)
    1
    >>> q.results[0].parent.value.s
    'Ka-Ping Yee <ping@lfw.org>'

"""

import ast

from docs.visitors.query.query import QueryVisitor


class QueryConstructor(object):
  """Wraps QueryVisitor and constructs custom query from kwargs and ast type

  """

  def __init__(self, ast_type, *args, **kw):
    super(QueryConstructor, self).__init__()
    self._ast_type = ast_type

    items = []
    for attr, value in kw.iteritems():
      if isinstance(value, basestring):
        items.append('node.%s == "%s"' % (attr, value))

      else:
        items.append('node.%s == %s' % (attr, value))


    self._query = ' and '.join(items)
    type_check = 'isinstance(node, ast.%s)' % (self._ast_type.__name__, )

    if self._query:
      self._visitor = QueryVisitor(
        ' and '.join((type_check, self._query))
      )
    else:
      self._visitor = QueryVisitor(type_check)


  def visit(self, *args, **kw):
    """Visits an ast.AST instance and its children

    Uses a `QueryVisitor` object.
    """

    return self._visitor.visit(*args, **kw)


  @property
  def results(self):
    """Results of the query"""

    return self._visitor.results
