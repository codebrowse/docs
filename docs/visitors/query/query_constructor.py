from docs.visitors.query.query import QueryVisitor

class QueryConstructor(object):
  """Wraps QueryVisitor and constructs custom query from kwargs and ast type

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

  """
  def __init__(self, ast_type, *args, **kw):
    super(QueryConstructor, self).__init__()
    self._ast_type = ast_type

    self._query = ' and '.join((
      'node.%s == %s' % (attr, value) for \
      attr, value in kw.iteritems()
    ))
    type_check = 'isinstance(node, ast.%s)' % (self._ast_type.__name__, )

    if self._query:
      self._visitor = QueryVisitor(
       ' and '.join((type_check, self._query))
      )
    else:
      self._visitor = QueryVisitor(type_check)


  def visit(self, *args, **kw):
    return self._visitor.visit(*args, **kw)

  @property
  def results(self):
    return self._visitor.results
